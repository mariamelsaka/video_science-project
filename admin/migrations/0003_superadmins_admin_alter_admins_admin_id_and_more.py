# Generated by Django 4.0.3 on 2022-05-12 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_superadmins_rename_id_admins_admin_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='superadmins',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admins', to='admin.admins'),
        ),
        migrations.AlterField(
            model_name='admins',
            name='admin_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='admin_id'),
        ),
        migrations.AlterField(
            model_name='superadmins',
            name='superadmin_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='superadmin_id'),
        ),
    ]