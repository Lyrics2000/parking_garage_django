
from django.contrib import admin
from django.urls import path
from .views import (index,ItemView,customer_details,register_customer
,vehicle_form,
save_vehicle,
payment_form,
payment_save_details,contact_us,save_contact_us)

app_name = 'mainapp'


urlpatterns = [
    path('',index, name = "index_page"),
    path('parking/<slug>/', ItemView.as_view(), name='parkingdetail'),
    path('payment/customer_details/', customer_details, name='customerdetails'),
    path('payment/register_customer/',register_customer, name= "register_customer"),
    path('payment/register_vehicle/',vehicle_form, name= "vehicle_register"),
    path('payment/save_vehicle/',save_vehicle, name= "vehicle_save"),
    path('payment/form/',payment_form, name= "payment_form"),
    path('payment/form/save/',payment_save_details, name= "payment_save_details"),
    path('contact_us/',contact_us, name= "contact_us"),
    path('contact_us/save/',save_contact_us, name= "save_contact_us"),


    
   
]