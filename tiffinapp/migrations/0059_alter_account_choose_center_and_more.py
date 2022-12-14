# Generated by Django 4.0.6 on 2022-08-20 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tiffinapp', '0058_alter_account_choose_center_alter_oderitem_orderlist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='choose_center',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.center'),
        ),
        migrations.AlterField(
            model_name='add_new_manu',
            name='categery_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.category'),
        ),
        migrations.AlterField(
            model_name='add_new_manu',
            name='choose_center',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.center'),
        ),
        migrations.AlterField(
            model_name='oderitem',
            name='orderlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.orderlist'),
        ),
        migrations.AlterField(
            model_name='oderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.add_new_manu'),
        ),
        migrations.AlterField(
            model_name='oderitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='add_manu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.add_new_manu'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.sigin'),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sigin',
            name='choose_center',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tiffinapp.center'),
        ),
    ]
