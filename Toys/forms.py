from django.forms import ModelForm
from .models import *

class customerForm(ModelForm):
	class Meta:
		model = customer
		fields = '__all__'