from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    booking_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    party_size = models.IntegerField()
    booking_message = models.TextField(max_length=100, blank=True)

    def clean(self):
        if self.party_size < 1:
            raise ValidationError('Party size must be at least 1.')
        if self.booking_date < timezone.now().date():
            raise ValidationError('Booking date cannot be in the past.')

    class Meta:
        ordering = ['booking_date', 'booking_time']
        unique_together = ('user', 'booking_date', 'booking_time')
        # Ensure unique booking for a user at a specific date and time

    def __str__(self):
        return f"{self.booking_name} on {self.booking_date} at \
            {self.booking_time} for {self.party_size} guests."
