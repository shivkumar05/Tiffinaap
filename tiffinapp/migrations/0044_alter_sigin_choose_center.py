# Generated by Django 4.0.6 on 2022-07-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0043_alter_sigin_choose_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sigin',
            name='choose_center',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
