from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('menu',views.menu,name='menu'),
    path('menu/gestion-machines',views.machine_gestion_form,name='gestion-machines'),
    path('menu/gestion-infra',views.infra_gestion_form,name='gestion-infra'),
    path('menu/gestion-user/',views.user_gestion_form,name='gestion-user'),
    path('menu/ajouter_machine',views.ajouter_machine,name='ajouter_machine'),
    path('menu/machines',views.machines,name='machines')
    ]