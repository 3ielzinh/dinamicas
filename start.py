#!/usr/bin/env python
"""
Script de inicialização simplificado
"""
import os
import sys

def main():
    """Função principal"""
    print("\n" + "=" * 60)
    print("STARTING WEB SERVER")
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
    try:
        main()
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
