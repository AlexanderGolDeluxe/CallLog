from django.contrib import admin

from .models import ContactTypes, ContactJournal, UsersJournal

admin.site.register(ContactTypes)
admin.site.register(ContactJournal)
admin.site.register(UsersJournal)
