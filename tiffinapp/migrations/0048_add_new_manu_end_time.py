# Generated by Django 4.0.6 on 2022-08-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0047_rename_time_add_new_manu_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_new_manu',
            name='end_time',
            field=models.TimeField(null=True),
        ),
    ]