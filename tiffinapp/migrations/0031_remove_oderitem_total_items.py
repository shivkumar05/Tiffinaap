# Generated by Django 4.0.6 on 2022-07-25 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0030_orderlist_oderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oderitem',
            name='total_items',
        ),
    ]
