"""
Comando para configurar o Site do Django após as migrações
"""
from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
import os


class Command(BaseCommand):
    help = 'Configura o Site do Django para o django-allauth'

    def handle(self, *args, **options):
        domain = os.environ.get('SITE_DOMAIN', 'dinamicas.onrender.com')
        site_name = os.environ.get('SITE_NAME', 'Dinâmicas para Igreja')
        
        try:
            # Tentar obter o site com ID 1
            site = Site.objects.get(pk=1)
            site.domain = domain
            site.name = site_name
            site.save()
            self.stdout.write(
                self.style.SUCCESS(f'✓ Site atualizado: {domain}')
            )
        except Site.DoesNotExist:
            # Se não existir, criar
            Site.objects.create(
                pk=1,
                domain=domain,
                name=site_name
            )
            self.stdout.write(
                self.style.SUCCESS(f'✓ Site criado: {domain}')
            )
