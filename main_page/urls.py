from django.urls import path, include

import contact
import info
from contact import urls
from info import urls
from .views import *

urlpatterns = [
    path('', MainNews.as_view(), name='main_page'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('author/<int:pk>/', ViewAuthor.as_view(), name='view_author'),
    path('contacts/', include(contact.urls)),
    path('info/', include(info.urls))
]
