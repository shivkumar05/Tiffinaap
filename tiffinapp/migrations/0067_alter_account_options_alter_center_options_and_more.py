# Generated by Django 4.0.6 on 2022-08-22 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0066_alter_account_choose_center'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={},
        ),
        migrations.AlterModelOptions(
            name='center',
            options={},
        ),
        migrations.AlterField(
            model_name='account',
            name='choose_center',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.center'),
        ),
    ]
