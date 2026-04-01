from django.urls import path

from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',       views.login_view,      name='login'),
    path('register/',    views.register,        name='register'),
    path('logout/',      views.logout_view,     name='logout'),
    path('panel/',       views.panel,           name='panel'),
    path('productos/',   views.productos_admin, name='productos_admin'),
]