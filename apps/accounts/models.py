"""
Models do app Accounts
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Perfil estendido do usuário para gerenciar assinaturas e preferências.
    """
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Usuário'
    )
    
    # Informações do perfil
    nome_igreja = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Nome da Igreja',
        help_text='Igreja onde o usuário serve'
    )
    
    cargo = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Cargo/Função',
        help_text='Ex: Líder de Jovens, Pastor, Coordenador'
    )
    
    telefone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Telefone'
    )
    
    # Monetização
    is_assinante = models.BooleanField(
        default=False,
        verbose_name='É Assinante?',
        help_text='Usuário com acesso premium'
    )
    
    data_inicio_assinatura = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Data de Início da Assinatura'
    )
    
    data_fim_assinatura = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Data de Fim da Assinatura'
    )
    
    stripe_customer_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Stripe Customer ID',
        help_text='ID do cliente no Stripe (para integração futura)'
    )
    
    stripe_subscription_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Stripe Subscription ID',
        help_text='ID da assinatura no Stripe'
    )
    
    # Preferências
    receber_emails = models.BooleanField(
        default=True,
        verbose_name='Receber E-mails',
        help_text='Receber notificações e novidades por e-mail'
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
        verbose_name = 'Perfil de Usuário'
        verbose_name_plural = 'Perfis de Usuários'
    
    def __str__(self):
        return f"Perfil de {self.user.email}"
    
    def tem_acesso_premium(self):
        """Verifica se o usuário tem acesso a conteúdo premium"""
        return self.is_assinante
    
    def total_favoritos(self):
        """Retorna o total de dinâmicas favoritadas pelo usuário"""
        return self.user.dinamicas_favoritas.count()


@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    """Signal para criar automaticamente um perfil quando um usuário é criado"""
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def salvar_perfil_usuario(sender, instance, **kwargs):
    """Signal para salvar o perfil quando o usuário é salvo"""
    if hasattr(instance, 'profile'):
        instance.profile.save()
