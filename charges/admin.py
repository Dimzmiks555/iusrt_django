from django.contrib import admin

from charges.models import PackageOfReceipts, PackageOfServices, TypeOfReceipts, TypeOfServices, DocumentOfPackageOfServices, DocumentOfPackageOfReceipts, PaymentOfPackageOfReceipts, PaymentOfPackageOfServices

# Register your models here.


class PackageOfReceiptsInline(admin.StackedInline):
    model = DocumentOfPackageOfReceipts
    extra = 1


class PackageOfServicesInline(admin.StackedInline):
    model = DocumentOfPackageOfServices
    extra = 1


class PaymentOfReceiptsInline(admin.StackedInline):
    model = PaymentOfPackageOfReceipts
    extra = 1


class PaymentOfServicesInline(admin.StackedInline):
    model = PaymentOfPackageOfServices
    extra = 1


class PackageOfReceiptsAdmin(admin.ModelAdmin):
    inlines = [PackageOfReceiptsInline, PaymentOfReceiptsInline]


class PackageOfServicesAdmin(admin.ModelAdmin):
    inlines = [PackageOfServicesInline, PaymentOfServicesInline]


admin.site.register(TypeOfReceipts)
admin.site.register(TypeOfServices)
admin.site.register(PackageOfReceipts, PackageOfReceiptsAdmin)
admin.site.register(PackageOfServices, PackageOfServicesAdmin)
