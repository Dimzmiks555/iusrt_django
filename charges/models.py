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


class TypeOfReceipts(models.Model):
    name = models.CharField('Наименование типа', max_length=100)

    class Meta:
        verbose_name = 'Тип квитанций'
        verbose_name_plural = 'Типы квитанций'

    def __str__(self):
        return f"{self.name}"


class TypeOfServices(models.Model):
    name = models.CharField('Наименование типа', max_length=100)

    class Meta:
        verbose_name = 'Тип услуг'
        verbose_name_plural = 'Типы услуг'

    def __str__(self):
        return f"{self.name}"


class PackageOfReceipts(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name="Организация")
    type = models.ForeignKey(TypeOfReceipts, on_delete=models.PROTECT, verbose_name="Тип")
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, verbose_name="Статус")
    created_at = models.DateField('Дата создания', default=now)
    must_be_payed_at = models.DateField('Должно быть оплачено до', default=now)
    summ = models.DecimalField('Сумма', max_digits=10, decimal_places=2)
    description = models.TextField('Комментарий', blank=True)

    class Meta:
        verbose_name = 'Пакет квитанций'
        verbose_name_plural = 'Пакеты квитанций'

    def __str__(self):
        return f"Пакет квитанций № {self.id}"


class DocumentOfPackageOfReceipts(models.Model):
    file = models.FileField('Файл')
    package_of_receipts = models.ForeignKey(
        PackageOfReceipts, on_delete=models.PROTECT)
    class Meta:
        verbose_name = 'Прикрепленные файлы к пакету квитанций'
        verbose_name_plural = 'Прикрепленные файлы к пакету квитанций'


class PaymentOfPackageOfReceipts(models.Model):
    file = models.FileField('Файл')
    package_of_receipts = models.ForeignKey(
        PackageOfReceipts, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Чеки к пакету квитанций'
        verbose_name_plural = 'Чеки к пакету квитанций'


class PackageOfServices(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name="Организация")
    type = models.ForeignKey(TypeOfServices, on_delete=models.PROTECT, verbose_name="Тип")
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, verbose_name="Статус")
    created_at = models.DateField('Дата создания', default=now)
    must_be_payed_at = models.DateField('Должно быть оплачено до', default=now)
    summ = models.DecimalField('Сумма', max_digits=10, decimal_places=2)
    description = models.TextField('Комментарий', blank=True)

    class Meta:
        verbose_name = 'Пакет услуг'
        verbose_name_plural = 'Пакеты услуг'

    
    def __str__(self):
        return f"Пакет услуг № {self.id}"


class DocumentOfPackageOfServices(models.Model):
    file = models.FileField('Файл')
    package_of_services = models.ForeignKey(
        PackageOfServices, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Прикрепленные файлы к пакету услуг'
        verbose_name_plural = 'Прикрепленные файлы к пакету услуг'
    


class PaymentOfPackageOfServices(models.Model):
    file = models.FileField('Файл')
    package_of_services = models.ForeignKey(
        PackageOfServices, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Чеки к пакету услуг'
        verbose_name_plural = 'Чеки к пакету услуг'
