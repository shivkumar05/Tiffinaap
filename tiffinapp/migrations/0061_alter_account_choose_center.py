# Generated by Django 4.0.6 on 2022-08-22 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0060_alter_account_choose_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='choose_center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.center'),
        ),
    ]
