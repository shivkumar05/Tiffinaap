# Generated by Django 4.0.6 on 2022-08-24 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0082_rename_order_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oderitem',
            old_name='orderlist',
            new_name='cart',
        ),
    ]
