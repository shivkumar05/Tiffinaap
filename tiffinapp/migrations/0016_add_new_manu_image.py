# Generated by Django 4.0.6 on 2022-07-18 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0015_remove_add_new_manu_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_new_manu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
