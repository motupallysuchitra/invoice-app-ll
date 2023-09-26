from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
   
    path("invoices",AllInvoices.as_view(),name="invoices"),
    path("invoices/new",AllInvoices.as_view(),name="newinvoices"),
    path("invoices/<int:id>",SpecificInvoices.as_view(),name="SpecificInvoices"),
    path("invoices/<int:id>/items",AddItem.as_view(),name="AddItem"),
    path("user/signup/",SignupView.as_view(),name="SignupView"),
    path("user/login/",SigninView.as_view(),name="logininView"),
   
  
    ]