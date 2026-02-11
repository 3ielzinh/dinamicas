#!/usr/bin/env python
"""
Script de inicialização do banco de dados.
Executa migrações e verifica se o banco está pronto.
"""
import os
import sys
import django

# Configurar o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import call_command
from django.db import connection
from django.db.utils import OperationalError

def check_database_connection():
    """Verifica se a conexão com o banco está OK"""
    try:
        connection.ensure_connection()
        print("✓ Conexão com o banco de dados estabelecida")
        return True
    except OperationalError as e:
        print(f"✗ Erro ao conectar com o banco: {e}")
        return False

def run_migrations():
    """Executa as migrações do Django"""
    try:
        print("\n=== Executando migrações ===")
        call_command('migrate', '--noinput', verbosity=2)
        print("✓ Migrações executadas com sucesso")
        return True
    except Exception as e:
        print(f"✗ Erro ao executar migrações: {e}")
        return False

def create_superuser():
    """Cria um superusuário se não existir"""
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        if not User.objects.filter(is_superuser=True).exists():
            admin_email = os.environ.get('ADMIN_EMAIL', 'admin@dinamicas.com')
            admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123')
            
            User.objects.create_superuser(
                email=admin_email,
                password=admin_password
            )
            print(f"✓ Superusuário criado: {admin_email}")
        else:
            print("✓ Superusuário já existe")
        return True
    except Exception as e:
        print(f"⚠ Aviso ao criar superusuário: {e}")
        return True  # Não é crítico

def main():
    """Função principal"""
    print("=" * 50)
    print("INICIALIZAÇÃO DO BANCO DE DADOS")
    print("=" * 50)
    
    # Verificar conexão
    if not check_database_connection():
        print("\n✗ Falha na inicialização do banco")
        sys.exit(1)
    
    # Executar migrações
    if not run_migrations():
        print("\n✗ Falha ao executar migrações")
        sys.exit(1)
    
    # Criar superusuário
    create_superuser()
    
    print("\n" + "=" * 50)
    print("✓ BANCO DE DADOS INICIALIZADO COM SUCESSO")
    print("=" * 50)

if __name__ == '__main__':
    main()
