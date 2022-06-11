from django.urls import path, include
from schedule.views import Schedule,ViewSchedule



urlpatterns = [
    path('', Schedule.as_view(), name='schedule'),
    path('<int:pk>/', ViewSchedule.as_view(), name='view_schedule'),
]