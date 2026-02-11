@echo off
echo ========================================
echo   +100 Dinamicas Para Retiro na Igreja
echo   Iniciando servidor de desenvolvimento
echo ========================================
echo.

cd /d %~dp0
call venv\Scripts\activate.bat

echo Ambiente virtual ativado!
echo Iniciando servidor em http://127.0.0.1:8000
echo.
echo Pressione CTRL+C para parar o servidor
echo ========================================
echo.

python manage.py runserver

pause
