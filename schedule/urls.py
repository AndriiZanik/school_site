from django.urls import path, include
from schedule.views import Shedule

urlpatterns = [
    path('', Shedule.as_view(), name='main_page'),
]