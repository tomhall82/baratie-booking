from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_name', 'booking_date', 'booking_time', 'party_size', 'booking_message']
