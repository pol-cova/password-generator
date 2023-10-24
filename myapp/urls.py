from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls import static

# URLS
urlpatterns = [
    path('', views.index, name='index'),
    path('es-mx/', views.es_mx, name='es-mx'),
    path('generate/', views.generate_password, name='generate_password'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)