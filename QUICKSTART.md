# Guia de Início Rápido - +100 Dinâmicas Para Retiro

## ⚡ Setup em 5 Minutos

### Windows

```powershell
# 1. Criar ambiente virtual
python -m venv venv
venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar ambiente
copy .env.example .env
# Edite .env com suas configurações

# 4. Preparar banco de dados
python manage.py migrate

# 5. Criar admin
python manage.py createsuperuser

# 6. Popular com dinâmicas
python manage.py shell < populate_dinamicas.py

# 7. Iniciar servidor
python manage.py runserver
```

### Linux/Mac

```bash
# 1. Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar ambiente
cp .env.example .env
# Edite .env com suas configurações

# 4. Preparar banco de dados
python manage.py migrate

# 5. Criar admin
python manage.py createsuperuser

# 6. Popular com dinâmicas
python manage.py shell < populate_dinamicas.py

# 7. Iniciar servidor
python manage.py runserver
```

## 🎯 Acessos

- **Site**: http://localhost:8000
- **Admin**: http://localhost:8000/admin
- **Dashboard**: http://localhost:8000/dashboard/

## 📝 Configuração Mínima do .env

```env
SECRET_KEY=django-insecure-development-key-change-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

## 🧪 Testando

1. Acesse http://localhost:8000
2. Clique em "Criar Conta"
3. Cadastre-se com seu email
4. Faça login
5. Explore as dinâmicas!

## 🚨 Problemas Comuns

### Erro: "No module named 'django'"
```bash
pip install -r requirements.txt
```

### Erro: "ERRORS: ... migrations"
```bash
python manage.py migrate
```

### Porta 8000 em uso
```bash
python manage.py runserver 8001
```

## 📚 Próximos Passos

1. Customize as dinâmicas no admin
2. Adicione suas próprias dinâmicas
3. Configure email para recuperação de senha
4. Deploy no Render (veja DEPLOY.md)

## 🎓 Estrutura de Arquivos Importantes

```
manage.py              # CLI do Django
config/settings.py     # Configurações principais
apps/dinamicas/        # App de dinâmicas
  - models.py          # Modelos do banco
  - views.py           # Lógica das páginas
  - admin.py           # Painel admin
templates/             # HTML das páginas
requirements.txt       # Dependências Python
```

## 💡 Dicas

- Use o admin em `/admin` para gerenciar tudo
- O script `populate_dinamicas.py` adiciona 15+ dinâmicas de exemplo
- Todos os templates usam Bootstrap 5
- Sistema de favoritos já funcional
- Busca e filtros implementados

## 🔗 Links Úteis

- [Documentação Django](https://docs.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Deploy Guide](DEPLOY.md)
- [README Completo](README.md)

---

**Boa sorte com seu projeto! 🚀**
