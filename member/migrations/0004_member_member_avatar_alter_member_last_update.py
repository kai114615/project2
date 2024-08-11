# Generated by Django 5.0.7 on 2024-08-11 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_remove_member_member_address_member_member_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_avatar',
            field=models.CharField(default='istockphoto-2132177453-612x612.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 11, 22, 36, 58, 440423)),
        ),
    ]
