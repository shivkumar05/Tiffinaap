# Generated by Django 4.0.6 on 2022-07-22 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0026_remove_add_new_manu_categery_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_new_manu',
            name='categery_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.category'),
        ),
    ]