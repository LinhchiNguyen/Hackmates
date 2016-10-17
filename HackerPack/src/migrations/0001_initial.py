# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 18:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('website_url', models.URLField(max_length=50)),
                ('length', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'name', help_text=b'Enter a descriptive and unique name for your team (eg. HackPrinceton123)', max_length=64, unique=True)),
                ('description', models.TextField(default=b'a team', max_length=1024)),
                ('hackathon', models.ForeignKey(default=b'hackathon', on_delete=django.db.models.deletion.CASCADE, to='src.Hackathon')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'name', max_length=50, unique=True)),
                ('team', models.ForeignKey(default=b'team', on_delete=django.db.models.deletion.CASCADE, to='src.Team')),
                ('user', models.ForeignKey(default=b'user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default=b'images/users/default/default.png', upload_to=b'')),
                ('about', models.TextField(default=b'I am a hackmate!', max_length=500)),
                ('city', models.CharField(default=b'HackerPack Land', max_length=32)),
                ('school', models.CharField(default=b'HackerPack', max_length=50)),
                ('studies', models.CharField(default=b'Hacking', max_length=32)),
                ('platform_choices', models.CharField(choices=[(b'ANDROID', b'Android'), (b'IOS', b'iOS'), (b'WEB', b'Web Development'), (b'HARDWARE', b'Hardware')], default=b'None', max_length=50)),
                ('hackathons', models.ManyToManyField(to='src.Hackathon')),
                ('preference_tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(through='src.TeamMember', to=settings.AUTH_USER_MODEL),
        ),
    ]