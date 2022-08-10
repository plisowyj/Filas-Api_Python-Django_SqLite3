from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('admin_turnos.urls')),
    path('', include('anuncio_turnos.urls')),
    path('', include('emision_turnos.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
