# Generated by Django 3.2.6 on 2021-08-27 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0013_alter_contactjournal_staff_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactjournal',
            name='contact_date',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Дата обращения'),
        ),
    ]