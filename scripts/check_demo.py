import os, tempfile
os.environ.setdefault('DJANGO_SETTINGS_MODULE','app.local_settings')
import django
django.setup()
from django.test import Client, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from charges.models import PackageOfServices, PackageOfReceipts, PaymentOfPackageOfServices, PaymentOfPackageOfReceipts
from dictionary.models import Organization
c=Client(HTTP_HOST='localhost')
assert c.get('/profile/').status_code==302
c.force_login(Organization.objects.get(username='demo'))
for path in ['/', '/login/', '/profile/', '/profile/services/', '/profile/receipts/', '/profile/services/?status=1', '/profile/receipts/?status=0', '/profile/services/?page=2']:
 assert c.get(path).status_code==200,path
u=Organization.objects.get(username='demo')
assert PackageOfServices.objects.filter(organization=u).count()>=3
assert PackageOfReceipts.objects.filter(organization=u).count()>=3
for model,pay_model,kind,fk in [(PackageOfServices,PaymentOfPackageOfServices,'services','package_of_services'),(PackageOfReceipts,PaymentOfPackageOfReceipts,'receipts','package_of_receipts')]:
 p=model.objects.filter(organization=u).first()
 url=f'/profile/{kind}/{p.pk}/'
 assert c.get(url).status_code==200
 with tempfile.TemporaryDirectory() as media, override_settings(MEDIA_ROOT=media):
  before=set(pay_model.objects.values_list('pk',flat=True))
  response=c.post(url,{'file':SimpleUploadedFile('test.txt',b'demo payment',content_type='text/plain')})
  assert response.status_code==302 and 'uploaded=1' in response.url
  new=pay_model.objects.exclude(pk__in=before)
  assert new.count()==1
  assert c.get(url).status_code==200
  new.delete()
 assert c.post(url,{'file':SimpleUploadedFile('test.html',b'<html>test</html>')}).status_code==200
other,_=Organization.objects.get_or_create(username='access-check-local')
c.force_login(other)
assert c.get(f'/profile/services/{PackageOfServices.objects.filter(organization=u).first().pk}/').status_code==404
other.delete()
print('PASS: login, totals data, lists, details, upload and ownership checks')
