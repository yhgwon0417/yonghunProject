# Generated by Django 3.1.6 on 2021-03-08 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yonghun', '0013_auto_20210308_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='create_user', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='update_user', to='auth.user'),
            preserve_default=False,
        ),
    ]
