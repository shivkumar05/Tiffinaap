# Generated by Django 4.0.6 on 2022-08-25 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0083_rename_orderlist_oderitem_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_new_manu',
            name='Offer_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='add_new_manu',
            name='Tiffin_Price',
            field=models.FloatField(null=True),
        ),
    ]