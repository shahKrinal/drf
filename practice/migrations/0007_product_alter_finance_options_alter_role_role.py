# Generated by Django 4.2 on 2023-05-09 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0006_alter_permissions_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='finance',
            options={'verbose_name': 'Accounts'},
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(choices=[('admin', 'ADMIN'), ('accountant', 'Accountant'), ('HR', 'HR'), ('client_admin', 'CLIENT_ADMIN'), ('client_staff', 'CLIENT_STAFF')], max_length=20),
        ),
    ]