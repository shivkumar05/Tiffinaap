# Generated by Django 4.0.6 on 2022-08-23 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0070_alter_account_choose_center_alter_center_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='choose_center',
        ),
    ]