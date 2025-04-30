
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('generar_factura', views.generar_factura, name='prueba'),
]