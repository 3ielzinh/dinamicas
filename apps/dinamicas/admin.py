"""
Admin customizado para o app Dinamicas
"""
from django.contrib import admin
from django.db.models import Count
from .models import Dinamica


@admin.register(Dinamica)
class DinamicaAdmin(admin.ModelAdmin):
    """Configuração do admin para Dinamicas"""
    
    list_display = [
        'numero',
        'titulo',
        'categoria',
        'nivel_intensidade',
        'publico_indicado',
        'is_premium',
        'is_active',
        'total_favoritos_admin',
        'data_criacao'
    ]
    
    list_filter = [
        'categoria',
        'nivel_intensidade',
        'publico_indicado',
        'is_premium',
        'is_active',
        'data_criacao'
    ]
    
    search_fields = [
        'titulo',
        'numero',
        'descricao',
        'objetivo',
        'materiais'
    ]
    
    readonly_fields = [
        'data_criacao',
        'data_atualizacao',
        'total_favoritos_admin'
    ]
    
    fieldsets = (
        ('Identificação', {
            'fields': ('numero', 'titulo', 'categoria')
        }),
        ('Conteúdo', {
            'fields': ('descricao', 'objetivo', 'materiais', 'passo_a_passo')
        }),
        ('Informações Práticas', {
            'fields': (
                'tempo_estimado',
                'quantidade_participantes',
                'nivel_intensidade',
                'publico_indicado'
            )
        }),
        ('Espiritual', {
            'fields': ('versiculo_base',),
            'classes': ('collapse',)
        }),
        ('Monetização e Status', {
            'fields': ('is_premium', 'is_active')
        }),
        ('Metadados', {
            'fields': ('data_criacao', 'data_atualizacao', 'total_favoritos_admin'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ['numero']
    
    list_per_page = 20
    
    actions = ['marcar_como_premium', 'marcar_como_gratuito', 'ativar', 'desativar']
    
    def total_favoritos_admin(self, obj):
        """Exibe o total de favoritos no admin"""
        return obj.total_favoritos()
    total_favoritos_admin.short_description = 'Total de Favoritos'
    
    def marcar_como_premium(self, request, queryset):
        """Action para marcar dinâmicas como premium"""
        updated = queryset.update(is_premium=True)
        self.message_user(request, f'{updated} dinâmica(s) marcada(s) como premium.')
    marcar_como_premium.short_description = 'Marcar como Premium'
    
    def marcar_como_gratuito(self, request, queryset):
        """Action para marcar dinâmicas como gratuitas"""
        updated = queryset.update(is_premium=False)
        self.message_user(request, f'{updated} dinâmica(s) marcada(s) como gratuita(s).')
    marcar_como_gratuito.short_description = 'Marcar como Gratuito'
    
    def ativar(self, request, queryset):
        """Action para ativar dinâmicas"""
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} dinâmica(s) ativada(s).')
    ativar.short_description = 'Ativar dinâmicas'
    
    def desativar(self, request, queryset):
        """Action para desativar dinâmicas"""
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} dinâmica(s) desativada(s).')
    desativar.short_description = 'Desativar dinâmicas'
