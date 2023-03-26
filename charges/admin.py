from django.contrib import admin

from charges.models import PackageOfReceipts, PackageOfServices, Type

# Register your models here.



admin.site.register(Type)
admin.site.register(PackageOfReceipts)
admin.site.register(PackageOfServices)