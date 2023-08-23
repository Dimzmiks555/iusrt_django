from django.contrib import admin

from charges.models import PackageOfReceipts, PackageOfServices, Type, DocumentOfPackageOfServices, DocumentOfPackageOfReceipts

# Register your models here.


class PackageOfReceiptsInline(admin.StackedInline):
    model = DocumentOfPackageOfReceipts
    extra = 1


class PackageOfServicesInline(admin.StackedInline):
    model = DocumentOfPackageOfServices
    extra = 1


admin.site.register(Type)
admin.site.register(PackageOfReceipts)
admin.site.register(PackageOfServices)
