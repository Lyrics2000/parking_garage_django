from django.db import models
from django.db.models.query import ModelIterable
from django.db import models
import random
import os
from django.db.models import Q
from datetime import datetime
from django.utils.timezone import now
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from mainapp.utils import unique_slug_generator,category_unique_slug_generator
import uuid

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "parking/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )


class Parking(models.Model):
    CHOICES = (
        ('PR', 'Parking Facility'),
        ('OS', 'Open Space'),
        
    )
  


    parking_area_name  = models.CharField(max_length=100)
    parking_cost_per_hour = models.IntegerField()
    parking_location = models.CharField(max_length=150)
    parking_facility = models.CharField(max_length=300, choices = CHOICES)
    security_inclusive  = models.BooleanField(default=False)
    carwash_available = models.BooleanField(default=False)
    nearby_restaurant = models.BooleanField(default=False)
    parking_picture = models.FileField(upload_to = upload_image_path ,null=True,blank=False)
    parking_overview = models.TextField(blank=True,null= True)
    
    slug = models.SlugField(blank=True,unique=True,default=uuid.uuid4)

    def __str__(self):
        return self.parking_area_name

    def get_absolute_url(self):
        return reverse("mainapp:parkingdetail", kwargs={
            'slug': self.slug
        })






class ParkingSlots(models.Model):
    CHOICES2 = (
        ('PR', 'Parking Facility'),
        ('OS', 'Open Space'),
        
    )
  

    parking_id = models.ForeignKey(Parking, on_delete=models.CASCADE)
    parking_picture = models.FileField(upload_to = upload_image_path ,null=True,blank=False)
    booked = models.BooleanField(default=False)
    

    def __str__(self):
        return self.parking_id.parking_area_name


class Customer(models.Model):
    parking_id = models.ForeignKey(ParkingSlots, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=150)
    customer_id_no = models.CharField(max_length=150)
    customer_email = models.EmailField()
    customer_phone_number = models.CharField(max_length=150)

    def __str__(self):
        return self.customer_name


class Vehicle(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle_model = models.CharField(max_length=150)
    manufacture_year = models.CharField(max_length=150)
    vehicle_number_plate = models.CharField(max_length=150)

    def __str__(self):
        return self.customer_id.customer_name
    


class Payment(models.Model):
     
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    card_payment = models.BooleanField(default=False)
    paypal_payment = models.BooleanField(default=False)
    terms_condition = models.BooleanField(default=False)
    hours = models.IntegerField()
    total_payment = models.DecimalField(max_digits=90,decimal_places=2,blank=True,null=True)

    def __str__(self):
        return self.vehicle_id.customer_id.customer_name



class ContactUs(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    your_company = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.first_name
    
    


    
    

    



