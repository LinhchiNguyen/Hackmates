# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_hackathon_hackathon_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='hackathons',
            field=models.ManyToManyField(blank=True, to='src.Hackathon'),
        ),
    ]
