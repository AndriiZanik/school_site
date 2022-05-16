from django.urls import path, include
from .views import *

urlpatterns = [
    path('', contacts_page),
    path('add-response/', add_response),
]