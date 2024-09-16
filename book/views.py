from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

# Create your views here.
class BookingView(TemplateView):
    template_name = 'book.html'
