"""
URLs do app Dinamicas
"""
from django.urls import path
from . import views

app_name = 'dinamicas'

urlpatterns = [
    # Lista e busca
    path('', views.DinamicaListView.as_view(), name='lista'),
    path('busca/', views.BuscaAvancadaView.as_view(), name='busca_avancada'),
    
    # Detalhe
    path('<int:pk>/', views.DinamicaDetailView.as_view(), name='detalhe'),
    
    # Categoria
    path('categoria/<str:categoria>/', views.DinamicaPorCategoriaView.as_view(), name='categoria'),
    
    # Favoritos
    path('<int:pk>/favorito/', views.toggle_favorito, name='toggle_favorito'),
]
