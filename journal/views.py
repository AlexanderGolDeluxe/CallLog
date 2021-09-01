from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

from .decorators import unauthenticated_user
from .models import ContactTypes, UsersJournal, ContactJournal
from .forms import ContactTypesForm, UsersJournalForm, ContactJournalForm


TABLE_NAMES = {
  "orders": ContactJournal,
  "customers": UsersJournal,
  "order_types": ContactTypes
}
FORM_NAMES = {
  "orders": ContactJournalForm,
  "customers": UsersJournalForm,
  "order_types": ContactTypesForm
}


@login_required(login_url="login")
def index(request):
  users_count = UsersJournal.objects.all().count()
  types_count = ContactTypes.objects.all().count()
  contacts_count = ContactJournal.objects.all().count()
  contact_journal = ContactJournal.objects.order_by("-id")[:10:-1]
  users_journal = UsersJournal.objects.order_by("-id")[:10:-1]
  contact_types = ContactTypes.objects.order_by("-id")[:10:-1]
  
  context = {
    "users_count": users_count,
    "types_count": types_count,
    "contacts_count": contacts_count,
    "contact_journal": contact_journal,
    "users_journal": users_journal,
    "contact_types": contact_types
  }
  return render(request, "journal/journal.html", context)


@login_required(login_url="login")
def table_view(request, table, amount_items=""):
  current_table = TABLE_NAMES[table].objects.all()
  all_items_count = current_table.count()
  
  if amount_items:
    p = Paginator(current_table.order_by("id"), amount_items)
    page = request.GET.get("page")
    current_table = p.get_page(page)

  context = {
    "table_name": table,
    "table": current_table,
    "all_items_count": all_items_count
  }
  return render(request, "journal/table.html", context)


@login_required(login_url="login")
def entry_view(request, table, pk, delete=""):
  current_item = TABLE_NAMES[table].objects.get(id=pk)

  if request.method == "POST":
    current_item.delete()
    messages.success(request, "Запись была успешно удалена из базы данных")
    return redirect("/" + table)
  
  context = {
    "delete": delete,
    "table_name": table,
    "item": current_item
  }
  return render(request, "journal/entry_view.html", context)


@login_required(login_url="login")
def create_entry(request, table, pk=""):
  current_form = FORM_NAMES[table]
  current_entry = TABLE_NAMES[table].objects.get(id=pk) if pk else None

  if request.method == "POST":
    form = current_form(request.POST, instance=current_entry)
    if form.is_valid():
      form.save()
      messages.success(request, "Запись была успешно сохранена в базе данных")
      return redirect("/" + table)
    else:
      messages.error(request, "Ошибка в заполнении формы.\nПопробуйте ввести данные ещё раз.")

  context = {
    "table_name": table,
    "formset": current_form(instance=current_entry, label_suffix="")
  }
  return render(request, "journal/create_entry.html", context)


@unauthenticated_user
def sign_in(request):

  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)

    if user:
      login(request, user)
      return redirect("home_page")
    else:
      messages.info(request, "Вы ввели неправильный Логин или Пароль")
  
  return render(request, "journal/login.html")


def sign_out(request):
  logout(request)
  return redirect("login")