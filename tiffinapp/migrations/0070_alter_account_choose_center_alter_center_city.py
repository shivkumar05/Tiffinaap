# Generated by Django 4.0.6 on 2022-08-23 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0069_alter_account_choose_center_alter_center_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='choose_center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.center'),
        ),
        migrations.AlterField(
            model_name='center',
            name='city',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]