from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    url(r'^client-detail/$', views.client_detail, name='cliente'),
    url(r'^formulario-buscar/$', views.formulario_buscar),
    url(r'^buscar/$', views.buscar),
    url(r'^client-detail/(?P<pk>\d+)$', views.client_detail, name='cliente'),

]
