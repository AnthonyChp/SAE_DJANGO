from django.urls import path
from django.contrib.auth.decorators import permission_required
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_view, name='login'),
    path('menu',permission_required('accès_menu')(views.menu),name='menu'),
    path('menu/gestion-machines',views.machine_gestion_form,name='gestion-machines'),
    path('menu/gestion-infra',views.infra_gestion_form,name='gestion-infra'),
    path('menu/gestion-user/',views.user_gestion_form,name='gestion-user'),
    path('menu/machines', views.machines,name='machines'),
    path('menu/profils', views.profils,name='profils'),
    ]