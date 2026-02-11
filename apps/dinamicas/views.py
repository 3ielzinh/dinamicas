"""
Views do app Dinamicas
"""
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q, Count
from django.http import JsonResponse
from .models import Dinamica, Categoria


class DinamicaListView(LoginRequiredMixin, ListView):
    """
    Lista todas as dinâmicas com paginação, busca e filtros.
    Apenas usuários autenticados podem acessar.
    """
    model = Dinamica
    template_name = 'dinamicas/lista.html'
    context_object_name = 'dinamicas'
    paginate_by = 12
    login_url = '/accounts/login/'
    
    def get_queryset(self):
        queryset = Dinamica.objects.filter(is_active=True)
        
        # Busca por palavra-chave
        search_query = self.request.GET.get('q', '')
        if search_query:
            queryset = queryset.filter(
                Q(titulo__icontains=search_query) |
                Q(descricao__icontains=search_query) |
                Q(objetivo__icontains=search_query) |
                Q(materiais__icontains=search_query)
            )
        
        # Filtro por categoria
        categoria = self.request.GET.get('categoria', '')
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        
        # Filtro por nível de intensidade
        nivel = self.request.GET.get('nivel', '')
        if nivel:
            queryset = queryset.filter(nivel_intensidade=nivel)
        
        # Filtro por público
        publico = self.request.GET.get('publico', '')
        if publico:
            queryset = queryset.filter(publico_indicado=publico)
        
        # Ordenação
        ordem = self.request.GET.get('ordem', 'numero')
        if ordem == 'titulo':
            queryset = queryset.order_by('titulo')
        elif ordem == 'recentes':
            queryset = queryset.order_by('-data_criacao')
        elif ordem == 'populares':
            queryset = queryset.annotate(
                num_favoritos=Count('usuarios_favoritaram')
            ).order_by('-num_favoritos')
        else:
            queryset = queryset.order_by('numero')
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.choices
        context['search_query'] = self.request.GET.get('q', '')
        context['categoria_selecionada'] = self.request.GET.get('categoria', '')
        context['nivel_selecionado'] = self.request.GET.get('nivel', '')
        context['publico_selecionado'] = self.request.GET.get('publico', '')
        context['ordem_selecionada'] = self.request.GET.get('ordem', 'numero')
        context['total_resultados'] = self.get_queryset().count()
        return context


class DinamicaDetailView(LoginRequiredMixin, DetailView):
    """
    Exibe os detalhes completos de uma dinâmica.
    Verifica se o usuário tem acesso (premium ou não).
    """
    model = Dinamica
    template_name = 'dinamicas/detalhe.html'
    context_object_name = 'dinamica'
    login_url = '/accounts/login/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dinamica = self.get_object()
        user = self.request.user
        
        # Verifica se o usuário favoritou esta dinâmica
        context['usuario_favoritou'] = dinamica.usuario_favoritou(user)
        
        # Verifica acesso premium
        context['tem_acesso'] = True
        if dinamica.is_premium and not user.profile.tem_acesso_premium():
            context['tem_acesso'] = False
        
        # Dinâmicas relacionadas (mesma categoria)
        context['dinamicas_relacionadas'] = Dinamica.objects.filter(
            categoria=dinamica.categoria,
            is_active=True
        ).exclude(id=dinamica.id)[:4]
        
        return context


class DinamicaPorCategoriaView(LoginRequiredMixin, ListView):
    """Lista dinâmicas filtradas por categoria"""
    model = Dinamica
    template_name = 'dinamicas/categoria.html'
    context_object_name = 'dinamicas'
    paginate_by = 12
    login_url = '/accounts/login/'
    
    def get_queryset(self):
        self.categoria = self.kwargs.get('categoria')
        return Dinamica.objects.filter(
            categoria=self.categoria,
            is_active=True
        ).order_by('numero')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = self.categoria
        context['categoria_display'] = dict(Categoria.choices).get(self.categoria, '')
        context['total_dinamicas'] = self.get_queryset().count()
        return context


@login_required
def toggle_favorito(request, pk):
    """
    View para adicionar/remover uma dinâmica dos favoritos.
    Retorna JSON para requisições AJAX.
    """
    dinamica = get_object_or_404(Dinamica, pk=pk)
    user = request.user
    
    if dinamica.usuario_favoritou(user):
        # Remove dos favoritos
        dinamica.usuarios_favoritaram.remove(user)
        favoritado = False
        mensagem = f'"{dinamica.titulo}" removida dos favoritos.'
    else:
        # Adiciona aos favoritos
        dinamica.usuarios_favoritaram.add(user)
        favoritado = True
        mensagem = f'"{dinamica.titulo}" adicionada aos favoritos!'
    
    # Se for requisição AJAX, retorna JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'favoritado': favoritado,
            'total_favoritos': dinamica.total_favoritos(),
            'mensagem': mensagem
        })
    
    # Se não for AJAX, redireciona com mensagem
    messages.success(request, mensagem)
    return redirect('dinamicas:detalhe', pk=pk)


class BuscaAvancadaView(LoginRequiredMixin, ListView):
    """Busca avançada com múltiplos filtros"""
    model = Dinamica
    template_name = 'dinamicas/busca_avancada.html'
    context_object_name = 'dinamicas'
    paginate_by = 12
    login_url = '/accounts/login/'
    
    def get_queryset(self):
        queryset = Dinamica.objects.filter(is_active=True)
        
        # Aplica todos os filtros da busca avançada
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(
                Q(titulo__icontains=q) |
                Q(descricao__icontains=q) |
                Q(objetivo__icontains=q)
            )
        
        categoria = self.request.GET.get('categoria', '')
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        
        nivel = self.request.GET.get('nivel', '')
        if nivel:
            queryset = queryset.filter(nivel_intensidade=nivel)
        
        publico = self.request.GET.get('publico', '')
        if publico:
            queryset = queryset.filter(publico_indicado=publico)
        
        tempo = self.request.GET.get('tempo', '')
        if tempo:
            queryset = queryset.filter(tempo_estimado__icontains=tempo)
        
        return queryset.order_by('numero')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.choices
        context['filtros_ativos'] = any([
            self.request.GET.get('q'),
            self.request.GET.get('categoria'),
            self.request.GET.get('nivel'),
            self.request.GET.get('publico'),
            self.request.GET.get('tempo'),
        ])
        return context
