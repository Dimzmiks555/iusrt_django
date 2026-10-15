import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','app.local_settings')
import django
django.setup()
from datetime import date, timedelta
from dictionary.models import Organization, TaxSystem
from charges.models import PackageOfServices, PackageOfReceipts, TypeOfServices, TypeOfReceipts, DocumentOfPackageOfServices, DocumentOfPackageOfReceipts
from django.core.files.base import ContentFile
u=Organization.objects.get(username='demo')
u.tax_system,_=TaxSystem.objects.get_or_create(name='УСН «Доходы»')
u.save()
today=date(2026,10,13)
for model, type_model, doc_model, fk, rows in [
 (PackageOfServices,TypeOfServices,DocumentOfPackageOfServices,'package_of_services',[
 ('Бухгалтерское сопровождение','8500.00','Требуется оплата','Сопровождение за октябрь: обработка первичных документов и ведение учёта.'),
 ('Подготовка отчётности','3200.00','Требуется оплата','Подготовка квартальной отчётности. Данные демонстрационные.'),
 ('Расчёт зарплаты','2500.00','Оплачено','Расчёт зарплаты и подготовка расчётных листков за сентябрь.')]),
 (PackageOfReceipts,TypeOfReceipts,DocumentOfPackageOfReceipts,'package_of_receipts',[
 ('Аванс по УСН','15400.00','Требуется оплата','Тестовая квитанция по авансовому платежу за третий квартал. Не для реальной оплаты.'),
 ('Страховые взносы','7800.00','Требуется оплата','Демонстрационная квитанция по страховым взносам.'),
 ('НДФЛ','4100.00','Оплачено','Тестовый оплаченный пакет. Не для реальной оплаты.')])]:
 for i,(name,total,status,description) in enumerate(rows):
  kind,_=type_model.objects.get_or_create(name=name)
  package,_=model.objects.update_or_create(organization=u,type=kind,description=description,defaults=dict(summ=total,status=status,created_at=today-timedelta(days=i*7),must_be_payed_at=today+timedelta(days=10-i*7)))
  if not doc_model.objects.filter(**{fk:package}).exists():
   doc=doc_model(**{fk:package})
   doc.file.save(f'demo-{model.__name__}-{package.pk}.txt',ContentFile(f'ДЕМОНСТРАЦИОННЫЙ ДОКУМЕНТ\n{name}\nСумма: {total} руб.\n{description}\nНе предназначен для реальной оплаты.'.encode('utf-8')),save=True)
print('Added 3 services and 3 receipt packages for demo.')
