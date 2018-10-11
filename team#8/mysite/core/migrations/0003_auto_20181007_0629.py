# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-07 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_email_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='abc@gxyz.com', help_text='Required. Inform a valid email address.', max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='timeSpent',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]