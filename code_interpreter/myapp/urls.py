# file_reader/urls.py

from django.urls import path
from .views import  generate_and_execute_code

urlpatterns = [
    
    path('generate_code/', generate_and_execute_code, name='generate_and_execute_code'),
]
