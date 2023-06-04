from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"



class ProfileView(TemplateView):
    template_name = "profile/profile.html"


class ServicesView(TemplateView):
    template_name = "profile/services.html"

class ServiceView(TemplateView):
    template_name = "profile/services/service.html"


class ReceiptsView(TemplateView):    
    template_name = "profile/receipts.html"

class ReceiptView(TemplateView):
    template_name = "profile/receipts/receipt.html"