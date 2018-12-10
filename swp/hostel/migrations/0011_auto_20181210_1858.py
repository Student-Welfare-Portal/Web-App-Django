# Generated by Django 2.1.2 on 2018-12-10 13:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0010_auto_20181210_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintregister',
            name='comp_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/2018-12-10 18:58:20.440178'),
        ),
        migrations.AlterField(
            model_name='complaintregister',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 13, 28, 20, 440178, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='courrier',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 13, 28, 20, 440178, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hostelleave',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 13, 28, 20, 440178, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='selfhelpgroup',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 13, 28, 20, 440178, tzinfo=utc)),
        ),
    ]
