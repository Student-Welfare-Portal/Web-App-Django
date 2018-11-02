# Generated by Django 2.1.2 on 2018-11-01 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_integration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=256, null=True)),
                ('room_no', models.IntegerField(blank=True, null=True)),
                ('comp_img', models.ImageField(blank=True, null=True, upload_to='images/2018-11-02 00:12:28.779355')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_integration.Student')),
            ],
        ),
        migrations.CreateModel(
            name='MessItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=45, unique=True)),
                ('cost', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_from', models.DateField(blank=True, null=True)),
                ('leave_to', models.DateField(blank=True, null=True)),
                ('hometown', models.CharField(max_length=200)),
                ('reason', models.TextField()),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_integration.Student')),
            ],
        ),
        migrations.CreateModel(
            name='MessRefund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refund_from', models.DateField(blank=True, null=True)),
                ('refund_to', models.DateField(blank=True, null=True)),
                ('account_number', models.CharField(blank=True, max_length=18, null=True)),
                ('account_holder_name', models.CharField(blank=True, max_length=20, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=11, null=True)),
                ('ref_amount', models.IntegerField(blank=True, default=0, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_integration.Student')),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistoryMess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mess.MessItems')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_integration.Student')),
            ],
        ),
        migrations.CreateModel(
            name='OrderListMess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('modified_by', models.CharField(blank=True, max_length=45, null=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mess.MessItems')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api_integration.Student')),
            ],
        ),
    ]
