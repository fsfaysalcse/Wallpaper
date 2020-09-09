
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from wallpaper.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('wallpaper.urls')),
    path('insert/',insert_view)

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)