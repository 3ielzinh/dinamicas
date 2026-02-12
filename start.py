#!/usr/bin/env python
"""
Script de inicialização que GARANTE execução de migrações
"""
import os
import sys
import subprocess

print("\n" + "=" * 70)
print("  INICIALIZANDO APLICAÇÃO - DINÂMICAS PARA IGREJA")
print("=" * 70 + "\n")

def run_django_command(command, description):
    """Executa um comando Django"""
    print(f">>> {description}")
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        print(f"✓ {description} - OK\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ ERRO: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}\n")
        return False

# 1. Executar migrações
print("ETAPA 1/3: Migrações do Banco de Dados")
print("-" * 70)
if not run_django_command(
    "python manage.py migrate --noinput",
    "Aplicando migrações"
):
    print("⚠ AVISO: Migrações falharam, mas continuando...\n")

# 2. Configurar Site
print("ETAPA 2/3: Configuração do Django Site")
print("-" * 70)
if not run_django_command(
    "python manage.py setup_site",
    "Configurando site"
):
    print("⚠ AVISO: Setup do site falhou, mas continuando...\n")

# 3. Coletar estáticos
print("ETAPA 3/3: Arquivos Estáticos")
print("-" * 70)
if not run_django_command(
    "python manage.py collectstatic --noinput",
    "Coletando arquivos estáticos"
):
    print("⚠ AVISO: Collectstatic falhou, mas continuando...\n")

# Iniciar Gunicorn
print("=" * 70)
print("  INICIANDO SERVIDOR GUNICORN")
print("=" * 70 + "\n")

port = os.environ.get('PORT', '10000')
os.execvp('gunicorn', [
    'gunicorn',
    'config.wsgi:application',
    '--bind', f'0.0.0.0:{port}',
    '--workers', '2',
    '--timeout', '120',
    '--access-logfile', '-',
    '--error-logfile', '-'
])
