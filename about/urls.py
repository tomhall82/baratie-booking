from django.urls import path
from about.views import *


urlpatterns = [
    path('', IndexView.as_view()),
]

