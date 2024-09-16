from django.urls import path
from book.views import *


urlpatterns = [
    path('book/', BookingView.as_view(), name='book'),
]
