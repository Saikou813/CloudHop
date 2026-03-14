from django import forms
from .models import Booking, PassengerProfile

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['passenger_name', 'seat_preference']
        widgets = {
            'passenger_name': forms.TextInput(attrs={'class': 'form-control'}),
            'seat_preference': forms.Select(attrs={'class': 'form-select'}),
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = PassengerProfile
        fields = ['passport_number', 'frequent_flyer_number']
        widgets = {
            'passport_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Passport Number'}),
            'frequent_flyer_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter FF Number'}),
        }