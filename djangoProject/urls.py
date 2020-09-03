
from django.contrib import admin
from django.urls import path,include
from wallpaper import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('wallpaper.urls'))
]
