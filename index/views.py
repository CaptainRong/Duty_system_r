import os
# from plistlib import Data

import openpyxl
from django.http import StreamingHttpResponse, FileResponse, Http404
from django.shortcuts import render, HttpResponse
from time import strftime
import datetime
import numpy as np
from django.utils.encoding import escape_uri_path
from django.db.models import Avg, Max, Min, F, Q
from index.models import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def get_week_type(date_str):
    """获取单双周"""
    date_object = datetime.datetime.strptime(date_str, "%Y-%m-%d")

    # 获取ISO周数
    iso_week_number = date_object.isocalendar()[1]

    # 判断单周还是双周
    week_type = 1 if iso_week_number % 2 == 1 else 0

    return week_type


def get_name(data):
    """获取当日下姓名"""
    week = data.weekday()
    oe_week = get_week_type(data.strftime('%Y-%m-%d'))
    name = MyUsers.objects.filter(Q(work_week=week) & Q(oe_week=oe_week))
    return name


# Create your views here.
def index(request):
    """
    :param request:
    :return: date,users
    洗牌：
        # >>>np.random.permutation(10)
    """
    data_u = MyUsers.objects.all()
    print(data_u)
    if request.method == 'GET':
        context = {
            'method': 'GET',
            'data': data_u
        }
        return render(request, 'index/index.html', context)

    date_start_f = request.POST['date_start']
    date_end_f = request.POST['date_end']
    date_start = datetime.datetime.strptime(date_start_f, "%Y-%m-%d")
    date_end = datetime.datetime.strptime(date_end_f, "%Y-%m-%d")
    delta = (date_end - date_start).days

    if delta <= 0:
        msg = "日期距离不能少于1天！"
        return render(request, 'index/index.html', locals())
    elif delta >= 32:
        msg = "日期距离不能大于31天！"
        return render(request, 'index/index.html', locals())

    relation = {

    }
    # 获取时间范围
    date_range = [date_start + datetime.timedelta(days=x) for x in range((date_end - date_start).days + 1)]

    for i in date_range:
        relation[i.strftime('%Y%m%d')] = get_name(i)
    context = {
        'method': 'POST',
        'data': relation,
        'week': date_range
    }
    for k, v in relation.items():
        print(k)
        for i in v:
            print(f"{i}: hxkc")
        print(".....")
    print(relation)
    return render(request, 'index/index.html', context)


def download(request):
    data = request.GET.get("list")
    data = eval(data)
    date_s = request.GET.get("date_s")
    date_e = request.GET.get("date_e")
    xlsx_write(data, date_s, date_e)

    the_file_name = '值班表.xlsx'  # 显示在弹出对话框中的默认的下载文件名
    filename = os.path.join(BASE_DIR, 'test2.xlsx')  # 要下载的文件路径

    try:
        response = FileResponse(open(filename, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(the_file_name)
        response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(the_file_name))
        return response
    except Exception:
        raise Http404


def xlsx_write(data: list, date_s: str, date_e: str):
    filename = os.path.join(BASE_DIR, 'index/test.xlsx')  # 要下载的文件路径
    wb = openpyxl.load_workbook(filename)
    sheet = wb['test']
    sheet['A1'] = f"喀什地区财政局2023年{data[0]['date']}-2023年{data[-1]['date']}值班安排表"
    for i, item in enumerate(data):  # 3,21
        sheet['A' + str(i + 3)] = item['date']
        sheet['B' + str(i + 3)] = item['bai_ban']['ban_yuan']['name']
        sheet['D' + str(i + 3)] = item['bai_ban']['dai_ban']['name']
        sheet['F' + str(i + 3)] = item['bao_an_1']['name']
        sheet['G' + str(i + 3)] = item['wan_ban']['ban_yuan']['name']
        sheet['I' + str(i + 3)] = item['wan_ban']['ban_yuan']['name']
        sheet['K' + str(i + 3)] = item['bao_an_2']['name']

        # 计数器
        # user
        user = Users.objects.get(id=item['bai_ban']['ban_yuan']['id'])
        user.counter = F("counter") + 1
        user.save()

        user = Users.objects.get(id=item['wan_ban']['ban_yuan']['id'])
        user.counter = F("counter") + 1
        user.save()
        # user_dai
        user = Users_dai_ban.objects.get(id=item['bai_ban']['dai_ban']['id'])
        user.counter = F("counter") + 1
        user.save()
        user = Users_dai_ban.objects.get(id=item['wan_ban']['dai_ban']['id'])
        user.counter = F("counter") + 1
        user.save()
        # bao_an
        user = Users_bao_an.objects.get(id=item['bao_an_1']['id'])
        user.counter = F("counter") + 1
        user.save()
        user = Users_bao_an.objects.get(id=item['bao_an_2']['id'])
        user.counter = F("counter") + 1
        user.save()

    wb.save('test2.xlsx')
