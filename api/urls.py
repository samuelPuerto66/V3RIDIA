# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('test-conexion/', views.test_supabase, name='test_supabase'),
]