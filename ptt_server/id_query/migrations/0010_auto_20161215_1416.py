# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('id_query', '0009_auto_20161215_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='graphs',
        ),
        migrations.RemoveField(
            model_name='node',
            name='graphs',
        ),
        migrations.DeleteModel(
            name='Graph',
        ),
        migrations.DeleteModel(
            name='Link',
        ),
        migrations.DeleteModel(
            name='Node',
        ),
    ]