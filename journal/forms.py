from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Textarea, DateTimeInput, Select

from .models import ContactTypes, UsersJournal, ContactJournal


class ContactTypesForm(ModelForm):
  class Meta:
    model = ContactTypes
    fields = "__all__"

    widgets = {
			"type_name": TextInput(attrs = {
				'id': 'type-name',
        'class': 'form-control'
			})
		}


class UsersJournalForm(ModelForm):
  class Meta:
    model = UsersJournal
    fields = "__all__"

    widgets = {
			"full_user_name": TextInput(attrs = {
				'id': 'full-user-name',
        'class': 'form-control mb-2'
			}),
      "user_phone": TextInput(attrs = {
				'id': 'user-phone',
        'class': 'form-control mb-2',
        "type": "tel"
			}),
      "user_email": EmailInput(attrs = {
				'id': 'user-email',
        'class': 'form-control mb-2',
        "placeholder": "you@example.com"
			}),
      "amount_orders": NumberInput(attrs = {
				'id': 'amount-orders',
        'class': 'form-control mb-2'
			}),
      "user_info": Textarea(attrs = {
				'id': 'user-info',
        'class': 'form-control mb-2'
			})
		}


class ContactJournalForm(ModelForm):
  class Meta:
    model = ContactJournal
    fields = "__all__"

    widgets = {
			"user_name": Select(attrs = {
				'id': 'user-name',
        'class': 'form-control mb-2'
			}),
      "user_status": Select(attrs = {
				'id': 'user-status',
        'class': 'form-control mb-2'
			}),
      "staff_name": Select(attrs = {
				'id': 'staff-name',
        'class': 'form-control mb-2',
			}),
      "contact_type": Select(attrs = {
				'id': 'contact-type',
        'class': 'form-control mb-2'
			}),
      "description": Textarea(attrs = {
				'id': 'description',
        'class': 'form-control mb-2'
			}),
      "contact_date": DateTimeInput(attrs = {
				'id': 'contact-date',
        'class': 'form-control mb-2',
        "type": "datetime-local"
			}, format='%Y-%m-%dT%H:%M')
    }