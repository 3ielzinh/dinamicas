#!/usr/bin/env python
"""
Script de inicialização que executa migrações antes de iniciar o gunicorn
"""
import os
import sys
import subprocess

def run_command(command, description):
    """Executa um comando e exibe o resultado"""
    print(f"\n{'=' * 60}")
    print(f">>> {description}")
    print(f"{'=' * 60}")
    
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    if result.returncode != 0:
        print(f"✗ ERRO: {description} falhou com código {result.returncode}")
        return False
    
    print(f"✓ {description} concluído com sucesso")
    return True

def main():
    """Função principal"""
    print("\n" + "=" * 60)
    print("INICIANDO APLICAÇÃO")
    print("=" * 60)
    
    # Executar migrações
    if not run_command(
        "python manage.py migrate --noinput",
        "Executando migrações do banco de dados"
    ):
        print("\n⚠ AVISO: Migrações falharam, mas continuando...")
    
    # Configurar site
    if not run_command(
        "python manage.py setup_site",
        "Configurando Django Site"
    ):
        print("\n⚠ AVISO: Configuração do site falhou, mas continuando...")
    
    # Coletar arquivos estáticos (se necessário)
    if not run_command(
        "python manage.py collectstatic --noinput --clear",
        "Coletando arquivos estáticos"
    ):
        print("\n⚠ AVISO: Coleta de estáticos falhou, mas continuando...")
    
    print("\n" + "=" * 60)
    print("INICIANDO SERVIDOR GUNICORN")
    print("=" * 60 + "\n")
    
    # Iniciar gunicorn
    port = os.environ.get('PORT', '10000')
    os.execvp('gunicorn', [
        'gunicorn',
        'config.wsgi:application',
        '--bind', f'0.0.0.0:{port}',
        '--workers', '2',
        '--timeout', '120',
        '--access-logfile', '-',
        '--error-logfile', '-',
        '--log-level', 'info'
    ])

if __name__ == '__main__':
    main()
