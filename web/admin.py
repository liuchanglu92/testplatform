from django.contrib import admin

# Register your models here.
from web.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    #决定了model怎么显示
    list_display = ("id","name","status","run_datatime","report_url","log_url")

    #要显示的字段
    def report_url(self,obj):
        return obj.get_url('report')
    report_url.short_description = '测试报告'

    def log_url(self,obj):
        return obj.get_url('url')
    log_url.short_description = '执行日志'