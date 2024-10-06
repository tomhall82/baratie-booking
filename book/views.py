from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Class-based view for handling the booking form
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'book.html'  # The template for rendering the form
    success_url = reverse_lazy('booking_success')  # Redirect to a success page after form submission

    def form_valid(self, form):
        # If the form is valid, show a success message and save the form
        form.instance.user = self.request.user
        messages.success(self.request, 'Thanks for your booking!')
        return super().form_valid(form)

    def form_invalid(self, form):
        # If the form is invalid, show an error message
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)

# Class-based view for editing the booking form
class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_edit.html'
    success_url = reverse_lazy('booking_list')  # Redirect to the list of bookings after editing

    def test_func(self):
        # Ensure that the booking being edited belongs to the logged-in user
        booking = self.get_object()
        return self.request.user == booking.user

    def handle_no_permission(self):
        # If the user is not authorized, redirect to the bookings list
        messages.error(self.request, "You don't have permission to edit this booking.")
        return redirect('booking_list')
    
# Class-based view to delete bookings
class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    success_url = reverse_lazy('booking_list')  # Redirect to the list after deletion

    def test_func(self):
        # Ensure the user deleting the booking is the owner
        booking = self.get_object()
        return self.request.user == booking.user

# List view to show all bookings for the logged-in user
class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'
    paginate_by = 10

    def get_queryset(self):
        # Check if the user is a staff member
        if self.request.user.is_staff:
            # If staff, return all bookings
            return Booking.objects.all().order_by('booking_date')
        else:
            # If not staff, return only the bookings for the logged-in user
            return Booking.objects.filter(user=self.request.user).order_by('booking_date')
