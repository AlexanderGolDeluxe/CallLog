# Generated by Django 3.2.6 on 2021-08-29 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0015_auto_20210828_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersjournal',
            name='amount_orders',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество заказов'),
        ),
    ]
