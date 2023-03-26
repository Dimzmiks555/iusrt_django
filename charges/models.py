from django.db import models
from datetime import datetime
from dictionary.models import Organization
from django.utils.timezone import now

# Create your models here.

SUCCESS = 'Оплачено'
REQUIRE = 'Требуется оплата'
STATUS_CHOICES = (
    (SUCCESS, "Оплачено"),
    (REQUIRE, "Требуется оплата"),
)

class Type(models.Model):
    name = models.CharField('Наименование типа', max_length=100)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Тип'


class Document(models.Model):
    file = models.FileField('Файл')

class PackageOfReceipts(models.Model):
    documents = models.ManyToManyField(Document)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES)
    created_at = models.DateField('Дата создания', default=now)
    must_be_payed_at = models.DateField('Должно быть оплачено до', default=now)
    summ = models.DecimalField('Сумма', max_digits=10, decimal_places=2)
    description = models.TextField('Комментарий')

    class Meta:
        verbose_name = 'Пакет квитанций'
        verbose_name_plural = 'Пакеты квитанций'


class PackageOfServices(models.Model):
    documents = models.ManyToManyField(Document)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES)
    created_at = models.DateField('Дата создания', default=now)
    must_be_payed_at = models.DateField('Должно быть оплачено до', default=now)
    summ = models.DecimalField('Сумма', max_digits=10, decimal_places=2)
    description = models.TextField('Комментарий')

    class Meta:
        verbose_name = 'Пакет услуг'
        verbose_name_plural = 'Пакеты услуг'