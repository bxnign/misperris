from django.conf.urls import include, url

from . import views

from django.urls import path


urlpatterns = [
    
    url(r'^$', views.inicio, name="inicio"),
    url('perris/inicio', views.redirigir, name="redirigir"),
    url('perris/login', views.login , name="login"),
    url('perris/disponibles', views.perros_disponibles , name="perros_disponibles"),
    url('administrador',views.administrador, name="adm.inicio" ),
    path('agregarperro', views.agregarperro, name='new_post_perro'),
    path('eliminar/<int:pk>', views.eliminarperro, name='delete_post_perro'),
    url(r'^perro/(?P<pk>[0-9]+)/$', views.detallesperro,name='detail_post_perro'),
    path('perro/<int:pk>/editar/', views.editarperro, name='edit_post_perro'),

]

