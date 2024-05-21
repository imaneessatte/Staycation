from django.forms import ModelForm
from django import forms    
from .models import House , Reservation ,User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','role']

class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'
        exclude = ['owner']

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'startDate':DateInput(),
            'endDate':DateInput(),
        }

