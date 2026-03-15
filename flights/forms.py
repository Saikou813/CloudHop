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

from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'How can we help?', 'rows': 4}),
        }
