# Generated by Django 4.0.6 on 2022-07-21 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiffinapp', '0022_alter_add_new_manu_categery_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_new_manu',
            name='categery_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.category'),
        ),
    ]
