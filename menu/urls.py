from django.urls import path
from menu.views import *


urlpatterns = [
    path('menu/', MenuView.as_view(), name='menu'),
]
