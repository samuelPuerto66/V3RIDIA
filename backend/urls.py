# backend/urls.py
from django.contrib import admin
from django.urls import path, include # <--- Asegúrate de importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # <--- Esto conecta tu api/urls.py
]