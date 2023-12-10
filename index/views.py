import os
import openpyxl
from django.http import StreamingHttpResponse, FileResponse, Http404
from django.shortcuts import render, HttpResponse
from time import strftime
import datetime
import numpy as np
from django.utils.encoding import escape_uri_path
from django.db.models import Avg, Max, Min, F
from index.models import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.
def index(request):
    """
    :param request:
    :return: date,users
    洗牌：
        >>>np.random.permutation(10)
    """
    if request.method == 'GET':
        return render(request, 'index/index.html', locals())
    elif request.method == "POST":
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
        # 白晚班列表
        bai_ban_list = []
        wan_ban_list = []
        list_he = []
        # 存在匹配对象进行添加白班列
        not_pi = []
        in_pi = []
        bai_ban = Users.objects.filter(gender=1, is_active=1).order_by('counter')
        for i in bai_ban:

            try:
                bai_ban_dai = Matching.objects.get(user__id=i.id).user_dai
                new_dict = {"ban_yuan": {"id": i.id, "name": i.name},
                            "dai_ban": {"id": bai_ban_dai.id, "name": bai_ban_dai.name}}
                in_pi.append(bai_ban_dai.id)
                bai_ban_list.append(new_dict)
            except Matching.DoesNotExist:
                not_pi.append(i.id)
        # 没有白班对象处理
        not_pi_user_list = Users.objects.in_bulk(id_list=not_pi).values()
        user_dai_list = Users_dai_ban.objects.filter(gender=1, is_active=1).order_by('counter')
        not_pi_user_dai_list = []
        #
        user_dai_min_counter = Users_dai_ban.objects.filter(is_active=1, gender=1).order_by('counter')
        user_min_counter = Users.objects.filter(is_active=1, gender=1).order_by('counter')
        for i in user_dai_list:
            if i not in in_pi:
                not_pi_user_dai_list.append(i)
        # 查看带班和班员的数量

        if len(not_pi_user_dai_list) < len(not_pi_user_list):
            for index, item in enumerate(not_pi_user_dai_list):
                new_dict = {'ban_yuan': {"id": user_min_counter[index].id, "name": user_min_counter[index].name},
                            'dai_ban': {"id": item.id, "name": item.name}}
                bai_ban_list.append(new_dict)
        else:

            for index, item in enumerate(not_pi_user_list):
                new_dict = {'ban_yuan': {"id": item.id, "name": item.name},
                            'dai_ban': {"id": user_dai_min_counter[index].id, "name": user_dai_min_counter[index].name}}
                bai_ban_list.append(new_dict)

        # 晚班处理
        # 存在匹配对象进行添加白班列
        not_pi = []
        in_pi = []
        bai_ban = Users.objects.filter(gender=0, is_active=1).order_by('counter')
        for i in bai_ban:

            try:
                bai_ban_dai = Matching.objects.get(user_id=i.id)

                new_dict = {"ban_yuan": {"id": i.id, "name": i.name},
                            "dai_ban": {"id": bai_ban_dai.id, "name": bai_ban_dai.name}}
                in_pi.append(bai_ban_dai.id)
                wan_ban_list.append(new_dict)
            except:
                not_pi.append(i.id)

        # 没有白班对象处理
        not_pi_user_list = Users.objects.in_bulk(id_list=not_pi).values()
        user_dai_list = Users_dai_ban.objects.filter(gender=0, is_active=1).order_by('counter')
        not_pi_user_dai_list = []
        #
        user_dai_min_counter = Users_dai_ban.objects.filter(is_active=1, gender=0).order_by('counter')
        user_min_counter = Users.objects.filter(is_active=1, gender=0).order_by('counter')
        for i in user_dai_list:
            if i not in in_pi:
                not_pi_user_dai_list.append(i)
        # 查看带班和班员的数量

        if len(not_pi_user_dai_list) < len(not_pi_user_list):

            for index, item in enumerate(not_pi_user_dai_list):
                new_dict = {'ban_yuan': {"id": user_min_counter[index].id, "name": user_min_counter[index].name},
                            'dai_ban': {"id": item.id, "name": item.name}}
                wan_ban_list.append(new_dict)
        else:

            for index, item in enumerate(not_pi_user_list):
                new_dict = {'ban_yuan': {"id": item.id, "name": item.name},
                            'dai_ban': {"id": user_dai_min_counter[index].id, "name": user_dai_min_counter[index].name}}
                wan_ban_list.append(new_dict)

        # 合一，随机处理
        if not bai_ban_list or not wan_ban_list or len(Users_bao_an.objects.all()) > 3:
            msg = "带班人员或值班人员为空(包括值班保安)！"
            return render(request, 'index/index.html', locals())
        bai_ban_list = list(np.random.permutation(bai_ban_list))
        wan_ban_list = list(np.random.permutation(wan_ban_list))
        a = 1
        for i in range(delta + 1):
            new = {}

            if len(bai_ban_list) <= i + 1:
                bai_ban_list += bai_ban_list
            if len(wan_ban_list) <= i + 1:
                wan_ban_list += wan_ban_list


            new_delta = datetime.timedelta(days=1)

            new['date'] = (date_start + new_delta * i).strftime("%m月%d日")
            new['bai_ban'] = bai_ban_list[i]
            new['wan_ban'] = wan_ban_list[i]

            list_he.append(new)
        data = list_he
        return render(request, 'index/index.html', locals())


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
