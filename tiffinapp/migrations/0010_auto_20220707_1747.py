# Generated by Django 2.1 on 2022-07-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0009_edit_manu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='add_new_manu',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='add_new_manu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AlterField(
            model_name='edit_manu',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='edit_manu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AlterField(
            model_name='sigin',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
