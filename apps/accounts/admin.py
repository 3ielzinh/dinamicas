"""
Admin customizado para o app Accounts
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    """Inline para editar o perfil junto com o usuário"""
    model = UserProfile
    can_delete = False
    verbose_name = 'Perfil'
    verbose_name_plural = 'Perfil'
    
    fieldsets = (
        ('Informações da Igreja', {
            'fields': ('nome_igreja', 'cargo', 'telefone')
        }),
        ('Assinatura', {
            'fields': (
                'is_assinante',
                'data_inicio_assinatura',
                'data_fim_assinatura',
                'stripe_customer_id',
                'stripe_subscription_id'
            )
        }),
        ('Preferências', {
            'fields': ('receber_emails',)
        }),
    )


class UserAdmin(BaseUserAdmin):
    """Administração customizada do User com perfil integrado"""
    inlines = (UserProfileInline,)
    
    list_display = [
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_assinante_display',
        'date_joined'
    ]
    
    list_filter = [
        'is_staff',
        'is_superuser',
        'is_active',
        'profile__is_assinante',
        'date_joined'
    ]
    
    def is_assinante_display(self, obj):
        """Exibe se o usuário é assinante"""
        return obj.profile.is_assinante if hasattr(obj, 'profile') else False
    is_assinante_display.short_description = 'Assinante'
    is_assinante_display.boolean = True


# Re-registrar UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Administração direta dos perfis"""
    
    list_display = [
        'user',
        'nome_igreja',
        'cargo',
        'is_assinante',
        'data_criacao'
    ]
    
    list_filter = [
        'is_assinante',
        'receber_emails',
        'data_criacao'
    ]
    
    search_fields = [
        'user__email',
        'user__first_name',
        'user__last_name',
        'nome_igreja',
        'cargo'
    ]
    
    readonly_fields = ['data_criacao', 'data_atualizacao']
    
    fieldsets = (
        ('Usuário', {
            'fields': ('user',)
        }),
        ('Informações da Igreja', {
            'fields': ('nome_igreja', 'cargo', 'telefone')
        }),
        ('Assinatura', {
            'fields': (
                'is_assinante',
                'data_inicio_assinatura',
                'data_fim_assinatura',
                'stripe_customer_id',
                'stripe_subscription_id'
            )
        }),
        ('Preferências', {
            'fields': ('receber_emails',)
        }),
        ('Metadados', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )
