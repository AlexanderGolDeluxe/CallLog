# Generated by Django 3.2.6 on 2021-08-22 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_alter_usersjournal_user_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactJournal',
        ),
        migrations.DeleteModel(
            name='ContactTypes',
        ),
        migrations.DeleteModel(
            name='UsersJournal',
        ),
    ]
