from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    booking_party_size = models.IntegerField()
    booking_message = models.TextField()
