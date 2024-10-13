from django import forms
from .models import Booking
from datetime import time


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_name',
                  'booking_date',
                  'booking_time',
                  'party_size',
                  'booking_message']
        widgets = {
            'booking_name': forms.TextInput(attrs={'placeholder': ' '}),
            'booking_time': forms.TimeInput(attrs={
                'type': 'time',
                'step': 900,  # 15-minute intervals
                'min': '08:00',  # Set minimum time to 08:00
                'max': '23:00'  # Set maximum time to 23:00
            }),
            'booking_message': forms.Textarea(attrs={'placeholder': ' '}),
        }

    def clean_booking_time(self):
        booking_time = self.cleaned_data.get('booking_time')
        if booking_time:
            if booking_time < time(8, 0) or booking_time > time(23, 00):
                raise forms.ValidationError(
                    "Bookings must be during opening hours (08:00-23:00)")
        return booking_time
