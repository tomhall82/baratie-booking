from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Booking
from .forms import BookingForm

# Create your views here.
        
class BookingView(TemplateView):
    template_name = 'book.html'

def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for your booking!')
            return redirect('booking_success')
        else:
            messages.error(request, 'Please correct the errors below.')
    
    else:
        form = BookingForm()

    return render(request, 'book.html', {'form': form})
