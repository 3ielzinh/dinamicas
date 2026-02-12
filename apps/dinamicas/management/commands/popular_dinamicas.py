"""
Comando para popular o banco com dinâmicas
"""
from django.core.management.base import BaseCommand
import os
import sys

# Adicionar o diretório raiz ao path para importar o script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, BASE_DIR)


class Command(BaseCommand):
    help = 'Popula o banco de dados com dinâmicas'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando população do banco...'))
        
        # Executar o script de população
        try:
            exec(open(os.path.join(BASE_DIR, 'populate_dinamicas_completo.py')).read())
            self.stdout.write(self.style.SUCCESS('✓ Banco populado com sucesso!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Erro ao popular banco: {e}'))
            raise
