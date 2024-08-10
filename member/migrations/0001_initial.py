# Generated by Django 5.0.7 on 2024-08-10 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('member_name', models.CharField(max_length=20, unique=True)),
                ('member_password', models.CharField(max_length=128)),
                ('member_birth', models.DateField()),
                ('member_address', models.CharField(max_length=200, null=True)),
                ('last_update', models.DateTimeField(default=datetime.datetime(2024, 8, 10, 12, 6, 59, 489730))),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]
