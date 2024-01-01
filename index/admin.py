from django.contrib import admin
from import_export import resources
from index.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

"""     ==========  班员 ==============  """
admin.site.site_title = "值班管理系统"
admin.site.site_header = "值班管理系统"
admin.site.index_title = "值班管理"


# django-import-export
class UsersResource(resources.ModelResource):
    class Meta:
        model = MyUsers


class UsersAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'department', 'gender', 'is_active')
    list_display_links = ['id', 'user']
    resource_classes = [UsersResource]
    search_fields = ('user', 'department')
    ordering = ['id']
    list_filter = ['gender']
    # list_per_page = 20
    list_editable = ['gender', 'department', 'is_active']


admin.site.register(Users, UsersAdmin)

"""     ==========  带班 ==============  """

# class Users_daiResource(resources.ModelResource):
#     class Meta:
#         model = Users_dai_ban
#
#
# class Users_daiAdmin(ImportExportModelAdmin):
#     list_display = ['id', 'name', 'department', 'counter', 'gender', 'phone', 'is_active']
#     list_display_links = ['id', 'name']
#     resource_classes = [Users_daiResource]
#     search_fields = ('name', 'phone')
#     ordering = ['id']
#     list_filter = ['gender']
#     # list_per_page = 20
#     list_editable = ['gender', 'department', 'is_active']
#
#
# admin.site.register(Users_dai_ban, Users_daiAdmin)

"""     ==========  科室 ==============  """


class DepartmentsResource(resources.ModelResource):
    class Meta:
        model = Department


class DepartmentsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    resource_classes = [DepartmentsResource]
    # search_fields = ('name')
    ordering = ['name']
    # list_filter = ['name']
    list_per_page = 20
    # list_editable = [ 'gender', 'is_active']


admin.site.register(Department, DepartmentsAdmin)

"""     ==========  值班匹配 ==============  """

# class MatchingResource(resources.ModelResource):
#     class Meta:
#         model = Matching
#
#
# class MatchingAdmin(ImportExportModelAdmin):
#     list_display = ['id', 'user', 'user_dai', 'counter', "type"]
#     list_display_links = ['id']
#     resource_classes = [MatchingResource]
#     search_fields = ('user', 'user_dai')
#     # ordering = ['name']
#     # list_filter = ['user', 'user_id']
#     # list_per_page = 20
#     list_editable = ['user', 'user_dai', 'type']
#
#
# admin.site.register(Matching, MatchingAdmin)

"""     ==========  保安 ==============  """

# class Users_bao_anResource(resources.ModelResource):
#     class Meta:
#         model = Users_bao_an


# class Users_bao_anAdmin(ImportExportModelAdmin):
#     list_display = ['id', 'name', 'counter', 'gender', 'phone', 'is_active']
#     list_display_links = ['id']
#     resource_classes = [Users_bao_anResource]
#     search_fields = ('name', 'phone')
#     # ordering = ['name']
#     # list_filter = ['user', 'user_id']
#     # list_per_page = 20
#     list_editable = ['is_active']
#
#
# admin.site.register(Users_bao_an, Users_bao_anAdmin)
"""     ==========  日志 ==============  """

# class LogResource(resources.ModelResource):
#     class Meta:
#         model = MyUsers
#
#
# class LogAdmin(ImportExportModelAdmin):
#     list_display = ['id', 'user', 'department', 'is_active']
#     list_display_links = ['id']
#     resource_classes = [LogResource]
#     # search_fields = ('name', 'phone')
#     # ordering = ['name']
#     # list_filter = ['user', 'user_id']
#     # list_per_page = 20
#     list_editable = ['is_active']
#
#
# admin.site.register(Log, LogAdmin)
