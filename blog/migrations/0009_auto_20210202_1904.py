# Generated by Django 3.1.5 on 2021-02-02 16:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210202_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 2, 16, 4, 49, 379664, tzinfo=utc)),
        ),
    ]
