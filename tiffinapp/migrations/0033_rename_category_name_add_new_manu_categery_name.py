# Generated by Django 4.0.6 on 2022-07-26 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0032_remove_add_new_manu_categery_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_new_manu',
            old_name='category_name',
            new_name='categery_name',
        ),
    ]
