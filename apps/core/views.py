"""
Views do app Core
"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from apps.dinamicas.models import Dinamica, Categoria


class HomeView(TemplateView):
    """Página inicial do site"""
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_dinamicas'] = Dinamica.objects.filter(is_active=True).count()
        context['categorias'] = Categoria.choices
        return context


class SobreView(TemplateView):
    """Página sobre o sistema"""
    template_name = 'core/sobre.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    """Dashboard do usuário autenticado"""
    template_name = 'core/dashboard.html'
    login_url = '/accounts/login/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Estatísticas do usuário
        context['total_favoritos'] = user.dinamicas_favoritas.count()
        context['total_dinamicas'] = Dinamica.objects.filter(is_active=True).count()
        
        # Dinâmicas recentes
        context['dinamicas_recentes'] = Dinamica.objects.filter(
            is_active=True
        ).order_by('-data_criacao')[:6]
        
        # Favoritos do usuário
        context['favoritos_recentes'] = user.dinamicas_favoritas.all()[:6]
        
        # Categorias com contagem
        context['categorias_info'] = [
            {
                'nome': cat[1],
                'valor': cat[0],
                'count': Dinamica.objects.filter(categoria=cat[0], is_active=True).count()
            }
            for cat in Categoria.choices
        ]
        
        return context
