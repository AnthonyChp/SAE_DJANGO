from django.urls import path
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('menu',views.menu,name='menu'),
    path('menu/gestion-machines',views.machine_gestion_form,name='gestion-machines'),
    path('menu/gestion-infra',views.infra_gestion_form,name='gestion-infra'),
    path('changement_statut_infra/<int:infra_id>/', views.changement_statut_infra, name='changement_statut_infra'),
    path('changement_entretient_infra/<int:infra_id>/', views.changement_entretient_infra, name='changement_entretient_infra'),
    path('menu/gestion-user/',views.user_gestion_form,name='gestion-user'),
    path('menu/machines', views.machines,name='machines'),
    path('changement_statut/<int:machine_id>/', views.changement_statut, name='changement_statut'),
    path('changement_entretient/<int:machine_id>/', views.changement_entretient, name='changement_entretient'),
    path('menu/profils', views.profils,name='profils'),
    ]