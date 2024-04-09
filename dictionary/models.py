from django.db import models
from django.contrib.auth.models import AbstractUser

INN_COPY = 'Копия ИНН'
OGRN_COPY = 'Копия ОГРНИП'
DOCUMENT_TYPE_CHOICES = [
    (INN_COPY, 'Копия ИНН'),
    (OGRN_COPY, 'Копия ОГРНИП'),
]



IP = 'ИП'
OOO = 'ООО'
ORGANIZATION_TYPE_CHOICES = [
    (IP, 'ИП'),
    (OOO, 'ООО'),
]


class TaxSystem(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Система налогообложения'
        verbose_name_plural = 'Системы налогообложения'

    def __str__(self):
        return "Система налогообложения " + self.name


class Organization(AbstractUser):
    
    organization_type = models.CharField(
        max_length=10,
        choices=ORGANIZATION_TYPE_CHOICES,
        blank=True,
        verbose_name="Организационно-правовая форма",
    )


    title = models.CharField("Наименование организации без ОПФ", max_length=255, blank=True)
    middle_name = models.CharField("Отчество", max_length=255, blank=True)
    inn = models.CharField("ИНН", max_length=255)
    ogrn = models.CharField("ОГРН", max_length=255)
    tax_system = models.ForeignKey(TaxSystem, on_delete=models.PROTECT, verbose_name="Система налогообложения", default=None, blank=True, null=True)
    phone = models.CharField("Телефон", max_length=255, blank=True)
    email = models.CharField("Email", max_length=255)
  
    def __str__(self):
        return self.organization_type + " " + self.title
    
    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
    
class Document(models.Model):
    name = models.CharField(max_length=255,choices=DOCUMENT_TYPE_CHOICES, verbose_name="Наименование")
    file = models.FileField('Файл')
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name="Организация", default=None, blank=True, )

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'