# Generated by Django 4.0.6 on 2022-07-28 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0038_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='choose_center',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.center'),
        ),
    ]
