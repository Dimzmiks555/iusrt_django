from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
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
    autocomplete_fields = ['organization']

    list_display = ("name", "organization", "summ", 'type', 'status', 'created_at', 'must_be_payed_at')
    search_fields = ['organization', 'summ']
    list_filter = ["status", "type__name", ("created_at", DateFieldListFilter)]

    def name(self, obj):
        return f'Пакет квитанций № {obj.id}'

    name.short_description = ""


class PackageOfServicesAdmin(admin.ModelAdmin):
    inlines = [PackageOfServicesInline, PaymentOfServicesInline]
    autocomplete_fields = ['organization']

    list_display = ("name", "organization", "summ", 'type', 'status', 'created_at', 'must_be_payed_at')
    search_fields = ['organization', 'summ']
    list_filter = ["status", "type__name", ("created_at", DateFieldListFilter)]

    def name(self, obj):
        return f'Пакет услуг № {obj.id}'

    name.short_description = ""


admin.site.register(TypeOfReceipts)
admin.site.register(TypeOfServices)
admin.site.register(PackageOfReceipts, PackageOfReceiptsAdmin)
admin.site.register(PackageOfServices, PackageOfServicesAdmin)
