from django.urls import path
from .views import BookingCreateView
from django.views.generic import TemplateView

urlpatterns = [
    path('book/', BookingCreateView.as_view(), name='book'),
    path('booking-success/', TemplateView.as_view(template_name="booking_success.html"), name='booking_success'),
]
