# Generated by Django 3.1.6 on 2021-04-23 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yonghun', '0009_auto_20210423_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
