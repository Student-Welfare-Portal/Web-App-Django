# Generated by Django 2.1.2 on 2018-11-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_integration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
