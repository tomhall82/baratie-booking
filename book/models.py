from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    
    booking_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    party_size = models.IntegerField()
    booking_message = models.TextField()

    class Meta:
        ordering = ['booking_date']

    def __str__(self):
        return f"Table for {self.booking_name} booked on {self.booking_date} at {self.booking_time} for {self.party_size} people. Message: {self.booking_message}"
