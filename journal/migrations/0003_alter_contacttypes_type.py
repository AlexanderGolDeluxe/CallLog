# Generated by Django 3.2.6 on 2021-08-22 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20210823_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacttypes',
            name='type',
            field=models.CharField(max_length=200, null=True, verbose_name='Тип обращения'),
        ),
    ]
