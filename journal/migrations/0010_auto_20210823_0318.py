# Generated by Django 3.2.6 on 2021-08-23 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0009_contactjournal_contact_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersjournal',
            name='amount_orders',
            field=models.IntegerField(default=0, verbose_name='Количество заказов'),
        ),
        migrations.AlterField(
            model_name='contactjournal',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journal.usersjournal', verbose_name='Пользователь который обратился'),
        ),
    ]
