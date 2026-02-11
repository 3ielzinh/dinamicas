"""
Middleware para capturar erros de banco não migrado
"""
from django.http import HttpResponse
from django.db.utils import ProgrammingError, OperationalError


class DatabaseNotReadyMiddleware:
    """
    Middleware que captura erros de banco não pronto e exibe página amigável
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except (ProgrammingError, OperationalError) as e:
            if 'does not exist' in str(e) or 'relation' in str(e):
                html = """
                <!DOCTYPE html>
                <html lang="pt-BR">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Site em Manutenção</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            color: white;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            min-height: 100vh;
                            margin: 0;
                            padding: 20px;
                        }
                        .container {
                            background: rgba(255, 255, 255, 0.1);
                            backdrop-filter: blur(10px);
                            border-radius: 20px;
                            padding: 40px;
                            max-width: 600px;
                            text-align: center;
                            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
                        }
                        h1 {
                            font-size: 3em;
                            margin: 0 0 20px 0;
                        }
                        p {
                            font-size: 1.2em;
                            margin: 15px 0;
                        }
                        .spinner {
                            border: 4px solid rgba(255, 255, 255, 0.3);
                            border-radius: 50%;
                            border-top: 4px solid white;
                            width: 60px;
                            height: 60px;
                            animation: spin 1s linear infinite;
                            margin: 30px auto;
                        }
                        @keyframes spin {
                            0% { transform: rotate(0deg); }
                            100% { transform: rotate(360deg); }
                        }
                        .info {
                            background: rgba(255, 255, 255, 0.2);
                            padding: 15px;
                            border-radius: 10px;
                            margin-top: 20px;
                            font-size: 0.9em;
                        }
                    </style>
                    <script>
                        setTimeout(function() {
                            location.reload();
                        }, 10000);
                    </script>
                </head>
                <body>
                    <div class="container">
                        <h1>🔧</h1>
                        <h2>Site em Configuração</h2>
                        <div class="spinner"></div>
                        <p>Estamos configurando o banco de dados...</p>
                        <p>Esta página recarregará automaticamente em 10 segundos.</p>
                        <div class="info">
                            <strong>O que está acontecendo?</strong><br>
                            As migrações do banco de dados estão sendo executadas.<br>
                            Aguarde alguns instantes e tente novamente.
                        </div>
                    </div>
                </body>
                </html>
                """
                return HttpResponse(html, status=503)
            raise
