from django.urls import path
from .views import analyze_csv

urlpatterns = [
    path('', analyze_csv, name='index'),
]
