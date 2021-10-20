from django.urls import path
from rest_framework import views
from .views import *

urlpatterns = [
    path('prediction/', WinePredictionView.as_view())
]