from django.urls import path
from info.views import InfoMain, InfoTeachers

urlpatterns = [
    path('', InfoMain.as_view(), name='info'),
    path('teachers/', InfoTeachers.as_view(), name='teachers'),
    #path('teachers/<int:pk>/', InfoTeachers.as_view(), name='teachers'),
]