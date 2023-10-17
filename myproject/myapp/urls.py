from django.urls import path
from . import views

# URLS
urlpatterns = [
    path('', views.index, name='index'),
    path('es-mx/', views.es_mx, name='es-mx'),
    path('generate/', views.generate_password, name='generate_password'),
]