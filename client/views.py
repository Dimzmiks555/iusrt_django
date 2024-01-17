from django.shortcuts import render
from django.views.generic import TemplateView
from charges.models import PackageOfServices, PaymentOfPackageOfServices, PackageOfReceipts
from dictionary.models import Organization
from charges.forms import UploadPaymentForm


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

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.createPayment()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['service'] = PackageOfServices.objects.get(
            pk=kwargs['id'])

        context['service_values'] = PackageOfServices._meta.get_fields()

        if self.request.POST:
            form = UploadPaymentForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                uploaded_file = self.request.FILES["file"]
                PaymentOfPackageOfServices.save(file=uploaded_file)

        else:
            form = UploadPaymentForm()

        context['form'] = UploadPaymentForm()

        return context


class ReceiptsView(TemplateView):
    template_name = "profile/receipts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receipts'] = PackageOfReceipts.objects.filter(
            organization=self.request.user)
        return context


class ReceiptView(TemplateView):
    template_name = "profile/receipts/receipt.html"
