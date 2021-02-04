from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from .models import Parking,ParkingSlots,Customer,Vehicle
from .forms import CustomerForm,VehicleForm,PaymentForm,ContactUsForm
from django.views.generic import DetailView,View,ListView

# Create your views here.

def index(request):
    parking = Parking.objects.all()
    context = {
        'parking' : parking
    }
    return render(request,'index.html',context)


class ItemView(DetailView):
    model = Parking
    template_name = "index_detailed.html"
    def get_context_data(self, **kwargs):
        parking_slots = ParkingSlots.objects.all()
        context = super().get_context_data(**kwargs)
        context["parking_slots"] = parking_slots
        return context

def customer_details(request):
    form = CustomerForm()
    parking_id = request.POST.get("product_id")
    request.session["parking_slot_id"] = parking_id
    context = {
        'form' : form
    }
    
    return render(request,'customer_booking.html',context)


def register_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid:
        instance = form.save(commit=False)
        parking_id_jj = request.session.get("parking_slot_id")
        parking_slot = ParkingSlots.objects.get(id = parking_id_jj )
        instance.parking_id = parking_slot
        instance.save()
        request.session["customer_id_registered"] = instance.id
        return redirect("mainapp:vehicle_register")
    return redirect("/")


def vehicle_form(request):
    form = VehicleForm()
    context = {
        "form":form
    }
    return render(request,'vehicle_details.html',context)

def save_vehicle(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid:
        instance   =  form.save(commit=False)
        registered_customer = request.session.get("customer_id_registered")
        customer = Customer.objects.get(id = registered_customer)
        instance.customer_id = customer
        instance.save()
        request.session["vehicle_id"] = instance.id
        return redirect("mainapp:payment_form")
    return redirect("/")


def payment_form(request):
    form = PaymentForm()
    context = {
        'form': form
    }
    return render(request,'checkin_details.html',context)

def payment_save_details(request):
    form =  PaymentForm(request.POST or None)
    if form.is_valid:
        instance   =  form.save(commit=False)
        parking_id_jj = request.session.get("parking_slot_id")
        parking_slot = ParkingSlots.objects.get(id = parking_id_jj )
        vehicle_id = request.session.get("vehicle_id")
        vehicle = Vehicle.objects.get(id = vehicle_id)
        instance.vehicle_id = vehicle
        instance.total_payment = float(parking_slot.parking_id.parking_cost_per_hour) * float(instance.hours)
        instance.save()
        parking_slot.booked = True
        parking_slot.save()
        del request.session["parking_slot_id"]
        del request.session["vehicle_id"]
        del request.session["customer_id_registered"]
        return redirect("/")

    return redirect("/")


def contact_us(request):
    form = ContactUsForm()
    context = {
        "form" : form
    }
    return render(request,'contact_us.html',context)

def save_contact_us(request):
    #checking contact if submited
    form =  ContactUsForm(request.POST or None)
    print("contact submited ", form.data)
    if form.is_valid:
        form.save()
        print(".....form saved......")
        return redirect("/")
    return redirect("/")






