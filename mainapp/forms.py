from .models import Customer,Vehicle,Payment,ContactUs
from django import forms



class CustomerForm(forms.ModelForm):
    class Meta:
        model =  Customer
        fields = ['customer_name','customer_id_no','customer_email','customer_phone_number']
        widgets = {
            'customer_name' : forms.TextInput(
                attrs={
                    "type":"text", "class":"form-control"
                }
            ),
            'customer_phone_number' : forms.TextInput(
                attrs={
                    "type":"text", "class":"form-control"
                }
            ),
             'customer_id_no' : forms.TextInput(
                attrs={
                    "type":"text", "class":"form-control"
                }
            ),
            'customer_email' : forms.TextInput(
                attrs={
                    "type":"email", "class":"form-control"
                }
            ),

            

        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_model','manufacture_year','vehicle_number_plate']
        widgets = {
            'vehicle_model' : forms.TextInput(
                attrs={
                    "type":"text", "class":"form-control"
                }
            ),
            'manufacture_year' : forms.TextInput(
                attrs={
                    "type":"text", "class":"form-control"
                }
            ),
             'vehicle_number_plate' : forms.TextInput(
                attrs={
                    "type":"text", "class":"form-control"
                }
            )
            

            

        }
    

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['hours','card_payment','paypal_payment','terms_condition']
        widgets = {
            'hours' : forms.TextInput(
                attrs={
                    "type":"number", "class":"form-control"
                }
            ),
            'card_payment' : forms.CheckboxInput(
                attrs={
                    "class":"form-check-input", "type":"checkbox"
                }
            ),
            "paypal_payment" : forms.CheckboxInput(
                attrs={
                   "class":"form-check-input", "type":"checkbox"
                }
            ),
             "terms_condition" : forms.CheckboxInput(
                attrs={
                    "class":"form-check-input", "type":"checkbox"
                }
            ),

        }


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name','last_name','phone_number','email','subject','your_company','message']
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    " type":"text", "class":"form-control" ,"required":""
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                   " type":"text", "class":"form-control" ,"required":""  
                }
            ),
             'phone_number' : forms.TextInput(
                attrs={
                   " type":"text", "class":"form-control" ,"required":""  
                }
            ),

             'subject' : forms.TextInput(
                attrs={
                   " type":"text", "class":"form-control" ,"required":""  
                }
            ),

              'subject' : forms.TextInput(
                attrs={
                   " type":"text", "class":"form-control" ,"required":""  
                }
            ),

                'your_company' : forms.TextInput(
                attrs={
                   " type":"text", "class":"form-control" ,"required":""  
                }
            ),

            'message' : forms.Textarea(
                attrs={
                   "class":"form-control", "rows":"3","required":""  
                }
            ),

             'email' : forms.EmailInput(
                attrs={
                   " type":"email", "class":"form-control" ,"required":""  
                }
            ),
            
            

        }
        


