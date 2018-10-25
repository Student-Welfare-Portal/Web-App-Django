# Generated by Django 2.1.2 on 2018-10-24 17:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('hostel', '0002_selfhelpgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintRegister',
            fields=[
                ('idcomplaint_register', models.IntegerField(primary_key=True, serialize=False)),
                ('complaint', models.CharField(blank=True, max_length=200, null=True)),
                ('room_no', models.IntegerField(blank=True, null=True)),
                ('comp_img', models.ImageField(default=datetime.datetime(2018, 10, 24, 17, 21, 32, 799829), upload_to='images/')),
                ('completed', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Student')),
            ],
        ),
    ]