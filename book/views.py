from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from .models import Booking
from .forms import BookingForm

# Class-based view for handling the booking form
class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'book.html'  # The template for rendering the form
    success_url = reverse_lazy('booking_success')  # Redirect to a success page after form submission

    def form_valid(self, form):
        # If the form is valid, show a success message and save the form
        messages.success(self.request, 'Thanks for your booking!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # If the form is invalid, show an error message
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)
