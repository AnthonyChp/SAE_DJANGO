from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('menu',views.menu,name='menu'),
    path('machines/', views.machine_list_view, name='machines'),
    path('machine/<pk>', views.machine_detail_view, name='machine-detail'),
    path('menu/gestion-machines',views.machine_gestion_form,name='gestion-machines'),
    path('menu/gestion-infra',views.infra_gestion_form,name='gestion-infra'),
    path('menu/gestion-user/',views.user_gestion_form,name='gestion-user'),
    path('menu/test/',views.add_machine, name='add_machine'),
    path('menu/ajouter_machine',views.ajouter_machine,name='ajouter_machine')
    ]