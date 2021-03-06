# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-21 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, help_text='用户报名后请改为真实姓名', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(help_text="<a href='password/'>修改密码</a>", max_length=128, verbose_name='password'),
        ),
    ]
