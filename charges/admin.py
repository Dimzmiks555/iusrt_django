from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from django.utils.html import format_html
from charges.models import PackageOfReceipts, PackageOfServices, TypeOfReceipts, TypeOfServices, DocumentOfPackageOfServices, DocumentOfPackageOfReceipts, PaymentOfPackageOfReceipts, PaymentOfPackageOfServices
import datetime

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

    list_display = ("name", "organization", "summ", 'type', 'colored_status', 'created_at', 'pay_date')
    search_fields = ['organization__title', 'summ', 'id']
    list_filter = ["status", "type__name", ("created_at", DateFieldListFilter)]

    def name(self, obj):
        return f'Пакет квитанций № {obj.id}'

    def colored_status(self, obj):

        color = ''

        if obj.status == 'Оплачено':
            color = '00aa00'
        else:
            color = 'aa0000'

        return format_html(
            u'<span style="background: #{}; padding: 2px 20px 4px ; color: #ffffff; border-radius: 4px">{}</span>', color, obj.status
        )

    def pay_date(self, obj):

        html = ''

        d = datetime.datetime.combine(obj.must_be_payed_at, datetime.time.min)

        if d < datetime.datetime.now() and obj.status != 'Оплачено':
            html = u'<span style="background: #aa0000; padding: 2px 20px 4px ; color: #ffffff; border-radius: 4px">{}</span>'
        else:
            html = u'<span style="background: #; padding: 2px 20px 4px ; color: #333; border-radius: 4px">{}</span>'
        return format_html(html, obj.must_be_payed_at)

    name.short_description = ""
    colored_status.short_description = "Статус"
    pay_date.short_description = "Крайний срок"


class PackageOfServicesAdmin(admin.ModelAdmin):
    inlines = [PackageOfServicesInline, PaymentOfServicesInline]
    autocomplete_fields = ['organization']

    list_display = ("name", "organization", "summ", 'type', 'colored_status', 'created_at', 'pay_date')
    search_fields = ['organization__title', 'summ', 'id']
    list_filter = ["status", "type__name", ("created_at", DateFieldListFilter)]

    def name(self, obj):
        return f'Пакет услуг № {obj.id}'

    def colored_status(self, obj):

        color = ''

        if obj.status == 'Оплачено':
            color = '00aa00'
        else:
            color = 'aa0000'

        return format_html(
            u'<span style="background: #{}; padding: 2px 20px 4px ; color: #ffffff; border-radius: 4px">{}</span>', color, obj.status
        )

    def pay_date(self, obj):

        html = ''

        d = datetime.datetime.combine(obj.must_be_payed_at, datetime.time.min)

        if d < datetime.datetime.now() and obj.status != 'Оплачено':
            html = u'<span style="background: #aa0000; padding: 2px 20px 4px ; color: #ffffff; border-radius: 4px">{}</span>'
        else:
            html = u'<span style="background: #; padding: 2px 20px 4px ; color: #333; border-radius: 4px">{}</span>'
        return format_html(html, obj.must_be_payed_at)

    name.short_description = ""
    colored_status.short_description = "Статус"
    pay_date.short_description = "Крайний срок"


admin.site.register(TypeOfReceipts)
admin.site.register(TypeOfServices)
admin.site.register(PackageOfReceipts, PackageOfReceiptsAdmin)
admin.site.register(PackageOfServices, PackageOfServicesAdmin)
