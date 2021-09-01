from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ContactTypes(models.Model):
  # "Повторный звонок"
  # "Обращение для получения информации",
  # "Обращение с целью оформить заказ",
  # "Деловое предложение",
  # "Жалобы и предложения"
  type_name = models.CharField("Название обращения", max_length=200, null=True, unique=True)

  def __str__(self) -> str:
    return self.type_name

  class Meta:
    verbose_name = "Тип обращений"
    verbose_name_plural = "Типы обращений"


class UsersJournal(models.Model):
  full_user_name = models.CharField("ФИО", max_length=100, null=True)
  user_phone = models.CharField("Номер телефона", max_length=20, null=True, unique=True)
  user_email = models.EmailField("Электронная почта", max_length=50, null=True, blank=True)
  amount_orders = models.PositiveIntegerField("Количество заказов", default=0)
  user_info = models.TextField("Сведения о пользователе", null=True, blank=True)

  def __str__(self) -> str:
      return self.full_user_name

  class Meta:
    verbose_name = "Пользователь"
    verbose_name_plural = "Журнал пользователей"


class ContactJournal(models.Model):
  STATUSES = (
    ("Не зарегистрирован", "Не зарегистрирован"),
    ("Новый клиент", "Новый клиент"),
    ("Постоянный клиент", "Постоянный клиент")
  )
  
  staff_name = models.CharField("Пользователь который принял обращение", max_length=50, choices=User.objects.exclude(username="admin").values_list("username", "username"), null=True)
  user_name = models.ForeignKey(UsersJournal, verbose_name="Пользователь который обратился", null=True, on_delete=models.SET_NULL)
  user_status = models.CharField("Статус пользователя", max_length=200, choices=STATUSES, null=True)
  contact_type = models.ForeignKey(ContactTypes, verbose_name="Тип обращения", null=True, on_delete=models.SET_NULL)
  description = models.TextField("Описание обращения", null=True, blank=True)
  contact_date = models.DateTimeField("Дата обращения", default=timezone.now, db_index = True)

  def __str__(self) -> str:
      return self.user_name

  class Meta:
    verbose_name = "Обращение"
    verbose_name_plural = "Журнал обращений"