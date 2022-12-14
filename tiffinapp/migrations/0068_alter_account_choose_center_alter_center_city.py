# Generated by Django 4.0.6 on 2022-08-23 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0067_alter_account_options_alter_center_options_and_more'),
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
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
