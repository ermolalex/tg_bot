import django
from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=50, default='Новая компания')

    def __str__(self):
        return f"{self.name}"


class UserType(models.TextChoices):
    STAFF = 'staff', 'Сотрудник'
    CLIENT = 'client', 'Клиент'
    ANONIM = 'anonim', 'Аноним'
    ADMIN = 'admin', 'Админ'


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, default="", blank=True)
    phone_number = models.CharField(max_length=20, default="", blank=True)
    tg_id = models.IntegerField()
    zulip_channel_id = models.IntegerField(default=0)
    company = models.ForeignKey(
        Company,
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    last_msg_at = models.DateTimeField(
        default=None,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        default=django.utils.timezone.now,
    )
    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.CLIENT,
    )
    pin_code = models.IntegerField(default=0)
    activated = models.BooleanField(default=True)

    @property
    def topic_name(self):
        return f"{self.fio}_{self.tg_id}"

    @property
    def fio(self):
        fio = self.first_name
        if self.last_name:
            fio += f" {self.last_name}"
        return fio

    def __str__(self):
        return f"{self.fio}, тел:{self.phone_number}, tg_id:{self.tg_id}"

