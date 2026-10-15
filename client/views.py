from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from charges.models import PaymentOfPackageOfReceipts
from charges.models import PackageOfServices, PaymentOfPackageOfServices, PackageOfReceipts, TypeOfReceipts, TypeOfServices
from dictionary.models import Organization
from charges.forms import UploadPaymentForm
from django.core.paginator import Paginator
from django.db.models import Sum



# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile/profile.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services__summ'] = PackageOfServices.objects.filter(organization=self.request.user, status="Требуется оплата").aggregate(Sum('summ'))
        context['receipts__summ'] = PackageOfReceipts.objects.filter(organization=self.request.user, status="Требуется оплата").aggregate(Sum('summ'))
        context['services__count'] = PackageOfServices.objects.filter(organization=self.request.user, status="Требуется оплата").count()
        context['receipts__count'] = PackageOfReceipts.objects.filter(organization=self.request.user, status="Требуется оплата").count()


        return context



class ServicesView(LoginRequiredMixin, TemplateView):
    template_name = "profile/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query = {
            "organization": self.request.user
        } 
        params = self.request.GET
        if params.get("status") in ["0", "1"]:
            if int(params.get("status")) == 1:
                query["status"] = "Оплачено"
            else:
                query["status"] = "Требуется оплата"
        
        if params.get("type", "").isdigit():
                query["type__id"] = params.get("type")


        services_list = PackageOfServices.objects.filter(**query).order_by("-created_at", "-pk")

        paginator = Paginator(services_list, 20)  

        page_number = self.request.GET.get("page")
        services_obj = paginator.get_page(page_number)

        
        context['services'] = services_obj
        context['page_numbers'] = paginator.get_elided_page_range(services_obj.number, on_each_side=1, on_ends=1)
        context['filter_query'] = self.request.GET.copy()
        context['filter_query'].pop('page', None)
        context['filter_query'] = context['filter_query'].urlencode()

        context['types'] = TypeOfServices.objects.filter()

        return context


class ReceiptsView(LoginRequiredMixin, TemplateView):
    template_name = "profile/receipts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query = {
            "organization": self.request.user
        } 
        params = self.request.GET
        if params.get("status") in ["0", "1"]:
            if int(params.get("status")) == 1:
                query["status"] = "Оплачено"
            else:
                query["status"] = "Требуется оплата"
        
        if params.get("type", "").isdigit():
                query["type__id"] = params.get("type")


        receipts_list = PackageOfReceipts.objects.filter(**query).order_by("-created_at", "-pk")

        paginator = Paginator(receipts_list, 20)  

        page_number = self.request.GET.get("page")
        receipts_obj = paginator.get_page(page_number)

        
        context['receipts'] = receipts_obj
        context['page_numbers'] = paginator.get_elided_page_range(receipts_obj.number, on_each_side=1, on_ends=1)
        context['filter_query'] = self.request.GET.copy()
        context['filter_query'].pop('page', None)
        context['filter_query'] = context['filter_query'].urlencode()

        context['types'] = TypeOfReceipts.objects.filter()

        return context


class PackageDetailView(LoginRequiredMixin, TemplateView):
    def get_package(self):
        return get_object_or_404(self.model, pk=self.kwargs['id'], organization=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        package = self.get_package()
        context[self.context_name] = package
        context['documents'] = getattr(package, self.document_relation).all()
        context['payments'] = getattr(package, self.payment_relation).all()
        context.setdefault('form', UploadPaymentForm())
        return context

    def post(self, request, *args, **kwargs):
        package = self.get_package()
        form = UploadPaymentForm(request.POST, request.FILES)
        if form.is_valid():
            self.payment_model.objects.create(**{self.package_field: package, 'file': form.cleaned_data['file']})
            return redirect(request.path + '?uploaded=1')
        return self.render_to_response(self.get_context_data(form=form))

class ServiceView(PackageDetailView):
    template_name = 'profile/services/service.html'
    model = PackageOfServices
    context_name = 'service'
    document_relation = 'documentofpackageofservices_set'
    payment_relation = 'paymentofpackageofservices_set'
    payment_model = PaymentOfPackageOfServices
    package_field = 'package_of_services'

class ReceiptView(PackageDetailView):
    template_name = 'profile/receipts/receipt.html'
    model = PackageOfReceipts
    context_name = 'receipt'
    document_relation = 'documentofpackageofreceipts_set'
    payment_relation = 'paymentofpackageofreceipts_set'
    payment_model = PaymentOfPackageOfReceipts
    package_field = 'package_of_receipts'
