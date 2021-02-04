from django.contrib import admin
from .models import Parking,Customer,ParkingSlots,Vehicle,Payment,ContactUs

# Register your models here.


# Register your models here.
class ParkingD(admin.ModelAdmin):
    list_display = ['__str__','parking_cost_per_hour','parking_location','parking_facility','security_inclusive','carwash_available','nearby_restaurant']
    class Meta:
        model = Parking

class CustomerD(admin.ModelAdmin):
    list_display = ['__str__' , 'customer_name','customer_id_no','customer_email','customer_phone_number']
    class Meta:
        model = Customer


class ParkingSlotsD(admin.ModelAdmin):
    list_display = ['__str__' , 'booked']
    class Meta:
        model = ParkingSlots

class VehicleD(admin.ModelAdmin):
    list_display = ['__str__' , 'vehicle_model','manufacture_year','vehicle_number_plate']
    class Meta:
        model = Vehicle

class PaymentD(admin.ModelAdmin):
    list_display = ['__str__' , 'card_payment','paypal_payment','terms_condition','hours','total_payment']
    class Meta:
        model = Payment
        
class ContactUsD(admin.ModelAdmin):
    list_display = ['__str__' , 'last_name','phone_number','email','subject','your_company']
    class Meta:
        model = ContactUs
admin.site.register(Parking,ParkingD)
admin.site.register(Customer,CustomerD)

admin.site.register(ParkingSlots,ParkingSlotsD)
admin.site.register(Vehicle,VehicleD)
admin.site.register(Payment,PaymentD)
admin.site.register(ContactUs,ContactUsD)

