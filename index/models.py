from django.db import models


# Create your models here.
class Users(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    name = models.CharField(verbose_name="姓名", max_length=33, default='', null=True)
    Gender = [
        (0, '男'),
        (1, '女'),
        (2, '未知')
    ]
    gender = models.SmallIntegerField(default=2, verbose_name='性别', choices=Gender)
    # post = models.ForeignKey(verbose_name="职务", to='Post', on_delete=models.CASCADE, default='')
    department = models.ForeignKey(verbose_name="科室", to="Department", on_delete=models.CASCADE, null=True)
    counter = models.IntegerField(verbose_name="值班次数", default=0)
    phone = models.CharField(verbose_name="手机号", max_length=32, null=True)
    time = models.DateTimeField(verbose_name="创建日期", auto_now=True)
    Active = [
        (1, "正常"),
        (2, "请假"),
        (3, "出差"),
        (4, "禁用"),
    ]
    is_active = models.SmallIntegerField(verbose_name="状态", default=1, choices=Active)

    def __str__(self):
        return self.name

    class Meta:
        # 数据库列表名
        db_table = 'Users'
        # 后台管理名
        verbose_name_plural = '成员管理'
        verbose_name = "成员管理"


class Users_dai_ban(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    name = models.CharField(verbose_name="姓名", max_length=33, default='', null=True)
    Gender = [
        (0, '男'),
        (1, '女'),
        (2, '未知')
    ]
    gender = models.SmallIntegerField(default=2, verbose_name='性别', choices=Gender)
    # post = models.ForeignKey(verbose_name="职务", to="Post", on_delete=models.CASCADE, default='')
    department = models.ForeignKey(verbose_name="科室", to="Department", on_delete=models.CASCADE, null=True)
    counter = models.IntegerField(verbose_name="值班次数", default=0)
    phone = models.CharField(verbose_name="手机号", max_length=32, null=True)
    time = models.DateTimeField(verbose_name="创建日期", auto_now=True)
    Active = [
        (1, "正常"),
        (2, "请假"),
        (3, "出差"),
        (4, "禁用"),
    ]
    is_active = models.SmallIntegerField(verbose_name="状态", default=1, choices=Active)

    def __str__(self):
        return self.name

    class Meta:
        # 数据库列表名
        db_table = 'Users_dai'
        # 后台管理名
        verbose_name_plural = '带班管理'
        verbose_name = "带班管理"


class Users_bao_an(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    name = models.CharField(verbose_name="姓名", max_length=33, default='', null=True)
    Gender = [
        (0, '男'),
        (1, '女'),
        (2, '未知')
    ]
    gender = models.SmallIntegerField(default=2, verbose_name='性别', choices=Gender)
    counter = models.IntegerField(verbose_name="值班次数", default=0)
    phone = models.CharField(verbose_name="手机号", max_length=32, null=True)
    time = models.DateTimeField(verbose_name="创建日期", auto_now=True)
    Active = [
        (1, "正常"),
        (2, "请假"),
        (3, "出差"),
        (4, "禁用"),
    ]
    is_active = models.SmallIntegerField(verbose_name="状态", default=1, choices=Active)

    def __str__(self):
        return self.name

    class Meta:
        # 数据库列表名
        db_table = 'Users_bao_an'
        # 后台管理名
        verbose_name_plural = '值班保安管理'
        verbose_name = "值班保安管理"


class Log(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    numbers_s = models.IntegerField(verbose_name="开始用户ID", default=-1)
    numbers_e = models.IntegerField(verbose_name="结束用户ID", default=-1)
    log = models.TextField(verbose_name="内容")
    time = models.DateTimeField(verbose_name="创建日期", auto_now=True)
    Active = [
        (1, "正常"),
        (2, "删除"),
    ]
    is_active = models.SmallIntegerField(verbose_name="状态", default=1, choices=Active)

    def __str__(self):
        return self.id

    class Meta:
        # 数据库列表名
        db_table = 'Log'
        # 后台管理名
        verbose_name_plural = '日志'
        verbose_name = "日志"


# 科室
class Department(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    name = models.CharField(verbose_name="科室名称", max_length=33, default='', null=True)
    time = models.DateTimeField(verbose_name="创建日期", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        # 数据库列表名
        db_table = 'Department'
        # 后台管理名
        verbose_name_plural = '科室管理'
        verbose_name = "科室管理"


class Matching(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    user = models.OneToOneField(verbose_name="班员", to="Users", on_delete=models.CASCADE, default='')
    user_dai = models.OneToOneField(verbose_name="带班", to="Users_dai_ban", on_delete=models.CASCADE, default='')
    counter = models.IntegerField(verbose_name="值班次数", default=0)
    Type = [
        (1, '白班'),
        (2, '晚班'),
    ]
    type = models.SmallIntegerField(verbose_name="类别", default=2, choices=Type)
    time = models.DateTimeField(verbose_name="创建日期", auto_now=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        # 数据库列表名
        db_table = 'Matching'
        # 后台管理名
        verbose_name_plural = '值班匹配'
        verbose_name = "值班匹配"




class MyUsers(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    user = models.CharField(verbose_name="姓名", max_length=33, default='', null=True)
    Gender = [
        (0, '男'),
        (1, '女'),
    ]
    gender = models.SmallIntegerField(default=0, verbose_name='性别', choices=Gender)
    department = models.ForeignKey(verbose_name="科室", to="Department", on_delete=models.CASCADE, null=True)
    Active = [
        (1, "正常"),
        (2, "请假"),
        (3, "出差"),
        (4, "禁用"),
    ]
    is_active = models.SmallIntegerField(verbose_name="状态", default=1, choices=Active)
    # 属于第几周
    week = [
        (0, '星期一'),
        (1, '星期二'),
        (2, '星期三'),
        (3, '星期四'),
        (4, '星期五'),
        (5, '星期六'),
        (6, '星期日')
    ]
    work_week = models.SmallIntegerField(default=0, verbose_name='周数', choices=week)
    # 值班时间：早上，下午，晚上
    work_time_choice = [
        (0, '早上'),
        (1, '下午'),
        (2, '晚上')
    ]
    work_time = models.SmallIntegerField(default=0, verbose_name='早上', choices=work_time_choice)
    # 单/双周 "Odd Week" "Even Week"。
    oe_week_choice = [
        (0, '双周'),
        (1, '单周')
    ]
    oe_week = models.SmallIntegerField(default=0, verbose_name='单双周', choices=oe_week_choice)

    def __str__(self):
        return self.user

# class Post(models.Model):
#     id = models.AutoField(verbose_name="id", primary_key=True)
#     name = models.CharField(verbose_name="职务", max_length=33, default='', null=True)
#
#     time = models.DateTimeField(verbose_name="创建日期", auto_now=True)
#     Active = [
#         (1, "正常"),
#         (4, "禁用"),
#     ]
#     is_active = models.SmallIntegerField(verbose_name="状态", default=1, choices=Active)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         # 数据库列表名
#         db_table = 'Post'
#         # 后台管理名
#         verbose_name_plural = '职务管理'
#         verbose_name = "职务管理"
