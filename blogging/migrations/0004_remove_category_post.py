# Generated by Django 2.1.11 on 2020-09-21 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0003_auto_20200921_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='post',
        ),
    ]
