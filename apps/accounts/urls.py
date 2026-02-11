"""
URLs do app Accounts
"""
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.PerfilView.as_view(), name='perfil'),
    path('editar/', views.EditarPerfilView.as_view(), name='editar_perfil'),
    path('favoritos/', views.FavoritosView.as_view(), name='favoritos'),
]
