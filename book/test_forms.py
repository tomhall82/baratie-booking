from django.test import TestCase
from .forms import BookingForm
from datetime import time, date

class BookingFormTest(TestCase):
    def test_form_with_valid_data(self):
        form_data = {
            'booking_name': 'Luffy',
            'booking_date': date.today(),
            'booking_time': time(12, 0),
            'party_size': 4,
            'booking_message': '',
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_missing_required_fields(self):
        form_data = {
            'booking_name': '',  # Empty name
            'booking_date': date.today(),
            'booking_time': time(), # No time specified
            'party_size': 2,
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('booking_name', form.errors)
        self.assertIn('booking_time', form.errors)
