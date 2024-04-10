from django.shortcuts import render
from django.views.generic import TemplateView
from charges.models import PackageOfServices, PaymentOfPackageOfServices, PackageOfReceipts, TypeOfReceipts, TypeOfServices
from dictionary.models import Organization
from charges.forms import UploadPaymentForm
from django.core.paginator import Paginator
from django.db.models import Sum



# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


class ProfileView(TemplateView):
    template_name = "profile/profile.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services__summ'] = PackageOfServices.objects.filter(organization=self.request.user, status="Требуется оплата").aggregate(Sum('summ'))
        context['receipts__summ'] = PackageOfReceipts.objects.filter(organization=self.request.user, status="Требуется оплата").aggregate(Sum('summ'))
        context['services__count'] = PackageOfServices.objects.filter(organization=self.request.user, status="Требуется оплата").count()
        context['receipts__count'] = PackageOfReceipts.objects.filter(organization=self.request.user, status="Требуется оплата").count()


        return context



class ServicesView(TemplateView):
    template_name = "profile/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query = {
            "organization": self.request.user
        } 
        params = self.request.GET
        if params.get("status"):
            if int(params.get("status")) == 1:
                query["status"] = "Оплачено"
            else:
                query["status"] = "Требуется оплата"
        
        if params.get("type"):
                query["type__id"] = params.get("type")


        services_list = PackageOfServices.objects.filter(**query)

        paginator = Paginator(services_list, 2)  

        page_number = self.request.GET.get("page")
        services_obj = paginator.get_page(page_number)

        
        context['services'] = services_obj

        context['types'] = TypeOfServices.objects.filter()

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

        query = {
            "organization": self.request.user
        } 
        params = self.request.GET
        if params.get("status"):
            if int(params.get("status")) == 1:
                query["status"] = "Оплачено"
            else:
                query["status"] = "Требуется оплата"
        
        if params.get("type"):
                query["type__id"] = params.get("type")


        receipts_list = PackageOfReceipts.objects.filter(**query)

        paginator = Paginator(receipts_list, 2)  

        page_number = self.request.GET.get("page")
        receipts_obj = paginator.get_page(page_number)

        
        context['receipts'] = receipts_obj

        context['types'] = TypeOfReceipts.objects.filter()

        return context


class ReceiptView(TemplateView):
    template_name = "profile/receipts/receipt.html"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.createPayment()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['receipt'] = PackageOfReceipts.objects.get(
            pk=kwargs['id'])

        context['receipt_values'] = PackageOfReceipts._meta.get_fields()



        if self.request.POST:
            form = UploadPaymentForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                uploaded_file = self.request.FILES["file"]
                PaymentOfPackageOfServices.save(file=uploaded_file)

        else:
            form = UploadPaymentForm()

        context['form'] = UploadPaymentForm()

        return context
