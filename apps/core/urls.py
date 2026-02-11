"""
URLs do app Core
"""
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sobre/', views.SobreView.as_view(), name='sobre'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
