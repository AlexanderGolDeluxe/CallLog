# Generated by Django 3.2.6 on 2021-09-01 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0016_alter_usersjournal_amount_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacttypes',
            name='type_name',
            field=models.CharField(max_length=200, null=True, unique=True, verbose_name='Название обращения'),
        ),
    ]