# Generated by Django 4.0.3 on 2022-05-12 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperAdmins',
            fields=[
                ('superadmin_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='user_id')),
                ('fisrt_name', models.TextField(max_length=50)),
                ('last_name', models.TextField(max_length=50)),
                ('phone_number', models.TextField(default='', max_length=11)),
                ('address', models.TextField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
                ('username', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(default=datetime.datetime)),
                ('updated_at', models.DateTimeField(default=datetime.datetime)),
                ('dateofbirth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default=None, max_length=10)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='admins',
            old_name='id',
            new_name='admin_id',
        ),
        migrations.AlterField(
            model_name='admins',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='admins',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime),
        ),
    ]
