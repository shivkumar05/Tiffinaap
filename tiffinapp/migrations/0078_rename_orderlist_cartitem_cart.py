# Generated by Django 4.0.6 on 2022-08-24 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0077_rename_orderlist_cart_rename_oderitem_cartitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='orderlist',
            new_name='cart',
        ),
    ]
