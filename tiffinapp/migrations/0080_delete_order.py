# Generated by Django 4.0.6 on 2022-08-24 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0079_oderitem_rename_cart_orderlist_delete_cartitem_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='order',
        ),
    ]