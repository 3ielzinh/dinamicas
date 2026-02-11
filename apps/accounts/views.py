"""
Views do app Accounts
"""
from django.views.generic import TemplateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import UserProfile


class PerfilView(LoginRequiredMixin, TemplateView):
    """Visualização do perfil do usuário"""
    template_name = 'accounts/perfil.html'
    login_url = '/accounts/login/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        context['total_favoritos'] = self.request.user.dinamicas_favoritas.count()
        return context


class EditarPerfilView(LoginRequiredMixin, UpdateView):
    """Edição do perfil do usuário"""
    model = UserProfile
    fields = ['nome_igreja', 'cargo', 'telefone', 'receber_emails']
    template_name = 'accounts/editar_perfil.html'
    success_url = reverse_lazy('accounts:perfil')
    login_url = '/accounts/login/'
    
    def get_object(self):
        return self.request.user.profile
    
    def form_valid(self, form):
        messages.success(self.request, 'Perfil atualizado com sucesso!')
        return super().form_valid(form)


class FavoritosView(LoginRequiredMixin, ListView):
    """Lista de dinâmicas favoritas do usuário"""
    template_name = 'accounts/favoritos.html'
    context_object_name = 'dinamicas'
    paginate_by = 12
    login_url = '/accounts/login/'
    
    def get_queryset(self):
        return self.request.user.dinamicas_favoritas.filter(is_active=True)
