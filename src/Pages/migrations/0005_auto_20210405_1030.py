# Generated by Django 2.1.5 on 2021-04-05 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0004_learningpage_pageonecomplete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filestore',
            name='user',
        ),
        migrations.RemoveField(
            model_name='learningpage',
            name='user',
        ),
        migrations.DeleteModel(
            name='FileStore',
        ),
        migrations.DeleteModel(
            name='LearningPage',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
