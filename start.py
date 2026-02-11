#!/usr/bin/env python
"""
Script de inicialização que executa migrações antes de iniciar o gunicorn
"""
import os
import sys
import subprocess
import time

def run_command(command, description):
    """Executa um comando e exibe o resultado"""
    print(f"\n{'=' * 60}")
    print(f">>> {description}")
    print(f">>> Comando: {command}")
    print(f"{'=' * 60}")
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=300  # 5 minutos de timeout
        )
        
        if result.stdout:
            print("STDOUT:")
            print(result.stdout)
        
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        
        if result.returncode != 0:
            print(f"\n✗ ERRO: {description} falhou com código {result.returncode}")
            return False
        
        print(f"\n✓ {description} concluído com sucesso")
        return True
        
    except subprocess.TimeoutExpired:
        print(f"\n✗ TIMEOUT: {description} demorou mais de 5 minutos")
        return False
    except Exception as e:
        print(f"\n✗ EXCEÇÃO: {description} falhou com erro: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Função principal"""
    print("\n" + "=" * 60)
    print("INICIANDO APLICAÇÃO - DINÂMICAS PARA IGREJA")
    print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Python: {sys.version}")
    print(f"Working Directory: {os.getcwd()}")
    print("=" * 60)
    
    # Verificar variáveis de ambiente importantes
    print("\n>>> Variáveis de Ambiente:")
    print(f"DATABASE_URL: {'SET' if os.environ.get('DATABASE_URL') else 'NOT SET'}")
    print(f"SITE_DOMAIN: {os.environ.get('SITE_DOMAIN', 'NOT SET')}")
    print(f"DEBUG: {os.environ.get('DEBUG', 'NOT SET')}")
    print(f"PORT: {os.environ.get('PORT', 'NOT SET')}")
    
    # Executar migrações com logs verbose
    print("\n" + "=" * 60)
    print("FASE 1: MIGRAÇÕES DO BANCO DE DADOS")
    print("=" * 60)
    
    if not run_command(
        "python manage.py migrate --noinput --verbosity=2",
        "Executando migrações do banco de dados"
    ):
        print("\n⚠ AVISO CRÍTICO: Migrações falharam!")
        print("⚠ O servidor pode não funcionar corretamente!")
        print("⚠ Continuando mesmo assim...")
        time.sleep(3)
    
    # Configurar site
    print("\n" + "=" * 60)
    print("FASE 2: CONFIGURAÇÃO DO DJANGO SITE")
    print("=" * 60)
    
    if not run_command(
        "python manage.py setup_site",
        "Configurando Django Site"
    ):
        print("\n⚠ AVISO: Configuração do site falhou!")
        print("⚠ Tentando continuar...")
        time.sleep(2)
    
    # Coletar arquivos estáticos
    print("\n" + "=" * 60)
    print("FASE 3: ARQUIVOS ESTÁTICOS")
    print("=" * 60)
    
    if not run_command(
        "python manage.py collectstatic --noinput --clear --verbosity=1",
        "Coletando arquivos estáticos"
    ):
        print("\n⚠ AVISO: Coleta de estáticos falhou!")
        print("⚠ CSS/JS podem não funcionar corretamente!")
        time.sleep(2)
    
    # Verificar se as tabelas foram criadas
    print("\n" + "=" * 60)
    print("FASE 4: VERIFICAÇÃO DO BANCO DE DADOS")
    print("=" * 60)
    
    run_command(
        "python manage.py showmigrations",
        "Verificando status das migrações"
    )
    
    print("\n" + "=" * 60)
    print("INICIANDO SERVIDOR GUNICORN")
    print("=" * 60 + "\n")
    
    # Aguardar um pouco antes de iniciar o gunicorn
    time.sleep(2)
    
    # Iniciar gunicorn
    port = os.environ.get('PORT', '10000')
    
    print(f"\nIniciando Gunicorn na porta {port}...")
    print("Argumentos:")
    args = [
        'gunicorn',
        'config.wsgi:application',
        '--bind', f'0.0.0.0:{port}',
        '--workers', '2',
        '--timeout', '120',
        '--access-logfile', '-',
        '--error-logfile', '-',
        '--log-level', 'info',
        '--capture-output',
        '--enable-stdio-inheritance'
    ]
    for arg in args:
        print(f"  {arg}")
    
    print("\n" + "=" * 60)
    print("GUNICORN ESTÁ INICIANDO...")
    print("=" * 60 + "\n")
    
    os.execvp('gunicorn', args)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("\n" + "=" * 60)
        print("ERRO FATAL NO SCRIPT DE INICIALIZAÇÃO")
        print("=" * 60)
        print(f"Erro: {e}")
        import traceback
        traceback.print_exc()
        print("\nTentando iniciar gunicorn diretamente como fallback...")
        
        port = os.environ.get('PORT', '10000')
        os.execvp('gunicorn', [
            'gunicorn',
            'config.wsgi:application',
            '--bind', f'0.0.0.0:{port}'
        ])
