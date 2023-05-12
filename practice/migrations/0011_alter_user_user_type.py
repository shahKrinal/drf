# Generated by Django 4.2 on 2023-05-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0010_alter_permissions_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[(1, 'System_Admin'), (2, 'System_staff'), (3, 'CLIENT_ADMIN'), (4, 'CLIENT_STAFF'), (5, 'CLIENT_PREMIUM_STAFF')], max_length=50, null=True),
        ),
    ]