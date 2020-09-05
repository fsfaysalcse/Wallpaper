from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index_view),
    path('details/<int:id>',details_view),
]
