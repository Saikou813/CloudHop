from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['passenger_name', 'seat_preference']
        widgets = {
            'passenger_name': forms.TextInput(attrs={'class': 'form-control'}),
            'seat_preference': forms.Select(attrs={'class': 'form-select'}),
        }