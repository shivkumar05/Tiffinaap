# Generated by Django 4.0.6 on 2022-07-20 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0019_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_new_manu',
            name='categery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.category'),
        ),
    ]