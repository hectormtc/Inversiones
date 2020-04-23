from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    url(r'^client-list/$', views.client_list, name='cliente'),
    url(r'^client-detail/$', views.client_detail, name='cliente'),
    url(r'^formulario-buscar/$', views.formulario_buscar),
    url(r'^buscar/$', views.buscar),

    url(r'^client-detail/(?P<pk>\d+)$', views.client_detail, name='cliente'),

    url(r'^producto-lista/$', views.producto_lista, name='producto_lista'),

    url(r'^factura-lista/$', views.factura_lista, name='factura'),

    url(r'^factura-detail/$', views.factura_detail, name='factura'),
    url(r'^factura-detail/(?P<pk>\d+)$', views.factura_detail, name='factura'),
    #path('<slug:categoria_slug>/', views.producto_lista,
    #     name='producto_lista_por_categoria'),
    #path('<int:id>/<slug:slug>/', views.producto_detalle, name='producto_detalle'),

    #path('', views.sign_up, name='user_sign'),
    #path('dashboard', views.user_dashboard, name='user_dashboard'),

]
