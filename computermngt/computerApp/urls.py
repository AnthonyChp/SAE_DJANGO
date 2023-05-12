from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('menu',views.menu,name='menu'),
    path('machines/', views.machine_list_view, name='machines'),
    path('machine/<pk>', views.machine_detail_view, name='machine-detail'),
    path('add-machine',views.machine_add_form,name='add-machine'),
    path('menu/test',views.test,name='test'),
    path('menu/ajouter_machine',views.ajouter_machine,name='ajouter_machine')
    ]