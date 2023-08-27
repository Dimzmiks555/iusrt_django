from django.shortcuts import render
from django.views.generic import TemplateView
from charges.models import PackageOfServices
from dictionary.models import Organization


# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


class ProfileView(TemplateView):
    template_name = "profile/profile.html"


class ServicesView(TemplateView):
    template_name = "profile/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = PackageOfServices.objects.filter(
            organization=self.request.user)
        return context


class ServiceView(TemplateView):
    template_name = "profile/services/service.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['service'] = PackageOfServices.objects.get(
            pk=kwargs['id'])

        context['service_values'] = PackageOfServices._meta.get_fields()
        return context


class ReceiptsView(TemplateView):
    template_name = "profile/receipts.html"


class ReceiptView(TemplateView):
    template_name = "profile/receipts/receipt.html"
