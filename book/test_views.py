from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking
from datetime import time, date

class BookingCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_booking_success(self):
        response = self.client.post(reverse('book'), {
            'booking_name': 'Zoro',
            'booking_date': date.today(),
            'booking_time': time(18, 0),
            'party_size': 6,
            'booking_message': '',
        })
        self.assertEqual(response.status_code, 302)  # Check for redirect status code
        response = self.client.get(response.url)  # Follow the redirect to the success page

    def test_correct_booking_data(self):
        response = self.client.post(reverse('book'), {
            'booking_name': 'Nami',
            'booking_date': date.today(),
            'booking_time': time(22, 0),
            'party_size': 7,
            'booking_message': '',
        })

        # Retreives the last created booking
        booking = Booking.objects.last()

        # Check data matches the fields above
        self.assertEqual(booking.booking_name, 'Nami')
        self.assertEqual(booking.booking_time, time(22, 0))
        self.assertEqual(booking.party_size, 7)
