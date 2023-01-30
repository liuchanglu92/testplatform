# Generated by Django 3.0 on 2023-01-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='用例名称')),
                ('case', models.FileField(upload_to='tests/%Y_%m_%d_%H_%M_%S/', verbose_name='用例文件')),
                ('status', models.IntegerField(choices=[(-1, '初始化'), (0, '马上执行'), (1, '正在执行测试用例'), (2, '正在生成测试报告'), (3, '执行完毕')], default=-1, verbose_name='测试状态')),
                ('run_datatime', models.DateTimeField(blank=True, null=True, verbose_name='最近执行时间')),
            ],
            options={
                'verbose_name': '测试任务',
                'verbose_name_plural': '测试任务',
            },
        ),
    ]
