# Generated by Django 4.0.6 on 2022-07-30 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0041_sigin_choose_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sigin',
            name='choose_center',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]