# Generated by Django 4.0.6 on 2022-07-30 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0042_alter_sigin_choose_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sigin',
            name='choose_center',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.center'),
        ),
    ]
