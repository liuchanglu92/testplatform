from django.db import models
import pathlib
from django.utils import html
from datetime import datetime
class Task(models.Model):
    name = models.CharField("用例名称",max_length=20)
    case = models.FileField("用例文件",upload_to='tests/%Y_%m_%d_%H_%M_%S/')
    status = models.IntegerField(
        "测试状态",default=-1,choices=[
            (-1,'初始化'),
            (0,'马上执行'),
            (1,'正在执行测试用例'),
            (2,'正在生成测试报告'),
            (3,'执行完毕'),
        ]
    )
    run_datatime = models.DateTimeField(
        "最近执行时间",null=True,blank=True
    )
    class Meta:
        verbose_name_plural = verbose_name = "测试任务"

    def __str__(self):
        return self.name
    def get_url(self,_type):
        """生成报告或者测试日志的url"""
        if self.case and self.status == 3: #执行完毕
            case_path = pathlib.PurePosixPath(str(self.case))
            root_path = pathlib.PurePosixPath('/uploads')

            if type == 'report': #报告url
                report_path = root_path/case_path.parent/"report/index.html"
            elif type == 'log':#日志url
                report_path = root_path/case_path.parent/"pytest.txt"
            else:
                report_path = '_'

            return html.format_html(f"<a herf='{report_path}' target='_blank'>点击查看</a>")
        else:
            return '-'

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        #判断是否需要启用测试框架，执行测试用例
        if self.status==0:
            self.status = 1  #修改状态：正在执行
            self.run_datatime = datetime.datetime.now()
            super().save()

            #启用测试框架
            import pytest
            pytest.main(self.case.open)
            self.status = 3  #修改状态：执行完毕
            self.run_datatime = datetime.datetime.now()
            super().save()