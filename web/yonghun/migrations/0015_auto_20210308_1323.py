# Generated by Django 3.1.6 on 2021-03-08 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonghun', '0014_auto_20210308_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='updated_by',
        ),
    ]