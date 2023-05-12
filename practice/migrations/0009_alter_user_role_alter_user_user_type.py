# Generated by Django 4.2 on 2023-05-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0008_user_permissions_user_user_type_alter_user_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('finance', 'finance'), ('accountant', 'Accountant'), ('HR', 'HR')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[(1, 'System Admin'), (2, 'System_staff'), (3, 'CLIENT_ADMIN'), (4, 'CLIENT_STAFF'), (5, 'CLIENT_PREMIUM_STAFF')], max_length=50, null=True),
        ),
    ]