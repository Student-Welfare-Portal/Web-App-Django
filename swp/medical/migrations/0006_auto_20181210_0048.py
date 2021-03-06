# Generated by Django 2.1.2 on 2018-12-09 19:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0005_auto_20181116_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 18, 2, 181051, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicalappointment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 18, 2, 183051, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicalleave',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 18, 2, 180052, tzinfo=utc)),
        ),
    ]
