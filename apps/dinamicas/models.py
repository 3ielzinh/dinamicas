"""
Models do app Dinamicas
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Categoria(models.TextChoices):
    """Categorias das dinâmicas"""
    QUEBRA_GELO = 'QUEBRA_GELO', 'Dinâmicas de Quebra-Gelo (1-20)'
    AUTOCONHECIMENTO = 'AUTOCONHECIMENTO', 'Dinâmicas de Autoconhecimento (21-40)'
    TRABALHO_EQUIPE = 'TRABALHO_EQUIPE', 'Dinâmicas de Trabalho em Equipe (41-60)'
    ESPIRITUAIS = 'ESPIRITUAIS', 'Dinâmicas Espirituais (61-80)'
    DIVERSAO_ENERGIA = 'DIVERSAO_ENERGIA', 'Dinâmicas de Diversão e Energia (81-100)'
    PROFUNDAS = 'PROFUNDAS', 'Dinâmicas Profundas para Momentos Marcantes (101-120)'


class NivelIntensidade(models.TextChoices):
    """Nível de intensidade da dinâmica"""
    BAIXO = 'BAIXO', 'Baixo'
    MEDIO = 'MEDIO', 'Médio'
    ALTO = 'ALTO', 'Alto'


class PublicoIndicado(models.TextChoices):
    """Público indicado para a dinâmica"""
    TODOS = 'TODOS', 'Todos os Públicos'
    JOVENS = 'JOVENS', 'Jovens'
    ADULTOS = 'ADULTOS', 'Adultos'
    CASAIS = 'CASAIS', 'Casais'
    CRIANCAS = 'CRIANCAS', 'Crianças'
    ADOLESCENTES = 'ADOLESCENTES', 'Adolescentes'
    IDOSOS = 'IDOSOS', 'Idosos'
    LIDERANCA = 'LIDERANCA', 'Liderança'


class Dinamica(models.Model):
    """
    Model principal para as dinâmicas de retiro.
    Armazena todas as informações necessárias para execução de uma dinâmica.
    """
    
    # Identificação
    titulo = models.CharField(
        max_length=200,
        verbose_name='Título',
        help_text='Nome da dinâmica'
    )
    numero = models.PositiveIntegerField(
        unique=True,
        verbose_name='Número',
        help_text='Número da dinâmica (1-120)'
    )
    
    # Classificação
    categoria = models.CharField(
        max_length=20,
        choices=Categoria.choices,
        verbose_name='Categoria',
        help_text='Categoria da dinâmica'
    )
    
    # Conteúdo
    descricao = models.TextField(
        verbose_name='Descrição',
        help_text='Breve descrição da dinâmica'
    )
    objetivo = models.TextField(
        verbose_name='Objetivo',
        help_text='Objetivo principal da dinâmica'
    )
    materiais = models.TextField(
        verbose_name='Materiais Necessários',
        help_text='Lista de materiais necessários'
    )
    passo_a_passo = models.TextField(
        verbose_name='Passo a Passo',
        help_text='Instruções detalhadas de execução'
    )
    
    # Informações práticas
    tempo_estimado = models.CharField(
        max_length=50,
        verbose_name='Tempo Estimado',
        help_text='Ex: 15-20 minutos'
    )
    quantidade_participantes = models.CharField(
        max_length=50,
        verbose_name='Quantidade de Participantes',
        help_text='Ex: 10-30 pessoas'
    )
    nivel_intensidade = models.CharField(
        max_length=10,
        choices=NivelIntensidade.choices,
        default=NivelIntensidade.MEDIO,
        verbose_name='Nível de Intensidade'
    )
    publico_indicado = models.CharField(
        max_length=20,
        choices=PublicoIndicado.choices,
        default=PublicoIndicado.TODOS,
        verbose_name='Público Indicado'
    )
    
    # Espiritual
    versiculo_base = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Versículo Base',
        help_text='Versículo bíblico relacionado (opcional)'
    )
    
    # Monetização
    is_premium = models.BooleanField(
        default=False,
        verbose_name='É Premium?',
        help_text='Dinâmica disponível apenas para assinantes'
    )
    
    # Status
    is_active = models.BooleanField(
        default=True,
        verbose_name='Ativo',
        help_text='Dinâmica visível no sistema'
    )
    
    # Relacionamentos
    usuarios_favoritaram = models.ManyToManyField(
        User,
        related_name='dinamicas_favoritas',
        blank=True,
        verbose_name='Usuários que Favoritaram'
    )
    
    # Metadados
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização'
    )
    
    class Meta:
        verbose_name = 'Dinâmica'
        verbose_name_plural = 'Dinâmicas'
        ordering = ['numero']
        indexes = [
            models.Index(fields=['categoria']),
            models.Index(fields=['numero']),
            models.Index(fields=['is_active']),
        ]
    
    def __str__(self):
        return f"{self.numero}. {self.titulo}"
    
    def get_absolute_url(self):
        """URL para a página de detalhe da dinâmica"""
        return reverse('dinamicas:detalhe', kwargs={'pk': self.pk})
    
    def total_favoritos(self):
        """Retorna o total de usuários que favoritaram esta dinâmica"""
        return self.usuarios_favoritaram.count()
    
    def usuario_favoritou(self, user):
        """Verifica se um usuário específico favoritou esta dinâmica"""
        return self.usuarios_favoritaram.filter(id=user.id).exists()
    
    def get_categoria_display_short(self):
        """Retorna apenas o nome da categoria sem o range de números"""
        categoria_dict = {
            'QUEBRA_GELO': 'Quebra-Gelo',
            'AUTOCONHECIMENTO': 'Autoconhecimento',
            'TRABALHO_EQUIPE': 'Trabalho em Equipe',
            'ESPIRITUAIS': 'Espirituais',
            'DIVERSAO_ENERGIA': 'Diversão e Energia',
            'PROFUNDAS': 'Momentos Marcantes',
        }
        return categoria_dict.get(self.categoria, self.get_categoria_display())
