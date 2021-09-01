# Generated by Django 3.2.6 on 2021-08-22 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_contactjournal_contacttypes_usersjournal'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactjournal',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание обращения'),
        ),
        migrations.AddField(
            model_name='contactjournal',
            name='staff_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Пользователь который принял обращение'),
        ),
        migrations.AddField(
            model_name='contactjournal',
            name='user_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Пользователь который обратился'),
        ),
        migrations.AddField(
            model_name='contactjournal',
            name='user_status',
            field=models.CharField(choices=[('Не зарегистрирован', 'Не зарегистрирован'), ('Новый клиент', 'Новый клиент'), ('Постоянный клиент', 'Постоянный клиент')], max_length=200, null=True, verbose_name='Статус пользователя'),
        ),
        migrations.AddField(
            model_name='usersjournal',
            name='full_user_name',
            field=models.CharField(max_length=100, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='usersjournal',
            name='user_email',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='Электронная почта'),
        ),
        migrations.AddField(
            model_name='usersjournal',
            name='user_phone',
            field=models.CharField(max_length=20, null=True, unique=True, verbose_name='Номер телефона'),
        ),
    ]