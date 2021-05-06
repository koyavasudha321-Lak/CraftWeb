from django.forms import ModelForm, forms
from .models import *

class customerForm(ModelForm):
	class Meta:
		model = customer
		fields = '__all__'




class HotelForm(ModelForm):
  
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']
