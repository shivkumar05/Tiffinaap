# Generated by Django 4.0.6 on 2022-07-06 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0004_delete_signup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login',
        ),
    ]