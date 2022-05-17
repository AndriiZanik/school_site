from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ContactForm.as_view()),
    #path('add-response/', add_response),
]