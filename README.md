# +100 Dinâmicas Para Retiro na Igreja 🙏

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Sobre o Projeto

**+100 Dinâmicas Para Retiro na Igreja** é um MicroSaaS completo desenvolvido em Django para ajudar líderes de igreja a organizar e acessar uma biblioteca de mais de 120 dinâmicas para retiros, encontros e eventos.

### ✨ Funcionalidades Principais

- ✅ **Sistema de Autenticação Completo** (Login, Cadastro, Recuperação de Senha)
- 📚 **Biblioteca com +120 Dinâmicas Organizadas**
- 🔍 **Busca Avançada e Filtros**
- ⭐ **Sistema de Favoritos**
- 🎯 **6 Categorias de Dinâmicas**
- 📊 **Dashboard Personalizado**
- 👤 **Perfis de Usuário**
- 💎 **Sistema Premium Preparado** (Stripe)
- 📱 **Design Responsivo com Bootstrap 5**
- 🚀 **Pronto para Deploy no Render**

## 🗂️ Estrutura do Projeto

```
Dinamicas_Igreja/
├── apps/
│   ├── core/               # App principal (home, dashboard)
│   ├── dinamicas/          # Gerenciamento de dinâmicas
│   └── accounts/           # Perfis de usuário
├── config/                 # Configurações Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/              # Templates HTML
│   ├── base.html
│   ├── core/
│   ├── dinamicas/
│   └── accounts/
├── static/                 # Arquivos estáticos
├── media/                  # Upload de arquivos
├── requirements.txt        # Dependências Python
├── manage.py
├── .env.example            # Exemplo de variáveis de ambiente
├── .gitignore
├── Procfile               # Render deploy
├── render.yaml            # Render config
├── build.sh               # Script de build
└── populate_dinamicas.py  # Script de população
```

## 🚀 Instalação Local

### Pré-requisitos

- Python 3.12+
- PostgreSQL (ou SQLite para desenvolvimento)
- Git

### Passo a Passo

1. **Clone o repositório**
```bash
git clone <seu-repositorio>
cd Dinamicas_Igreja
```

2. **Crie e ative ambiente virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure variáveis de ambiente**
```bash
# Copie o arquivo de exemplo
copy .env.example .env

# Edite o .env com suas configurações
# Gere uma SECRET_KEY em: https://djecrety.ir/
```

5. **Execute as migrações**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crie um superusuário**
```bash
python manage.py createsuperuser
```

7. **Popule o banco com dinâmicas de exemplo**
```bash
python manage.py shell < populate_dinamicas.py
```

8. **Colete arquivos estáticos**
```bash
python manage.py collectstatic --noinput
```

9. **Execute o servidor**
```bash
python manage.py runserver
```

10. **Acesse a aplicação**
- Frontend: http://localhost:8000
- Admin: http://localhost:8000/admin

## 🌐 Deploy no Render

### Preparação

1. **Crie conta no Render**: https://render.com

2. **Configure PostgreSQL**
   - No Render Dashboard, crie um novo PostgreSQL Database
   - Anote a URL de conexão

3. **Configure o Web Service**
   - Conecte seu repositório GitHub
   - Configure as variáveis de ambiente:
     - `SECRET_KEY` (gere uma nova)
     - `DEBUG=False`
     - `ALLOWED_HOSTS=.onrender.com`
     - `DATABASE_URL` (do PostgreSQL criado)

4. **Deploy Automático**
   - O `render.yaml` está configurado para deploy automático
   - O `build.sh` executa as migrações e coleta estáticos

### Variáveis de Ambiente Necessárias

```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=.onrender.com,seudominio.com
DATABASE_URL=postgresql://user:password@host:port/database

# Email (Opcional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=sua-senha-app

# Stripe (Futuro)
STRIPE_PUBLIC_KEY=
STRIPE_SECRET_KEY=
```

## 📊 Categorias de Dinâmicas

1. **Quebra-Gelo (1-20)** - Atividades para iniciar o retiro
2. **Autoconhecimento (21-40)** - Reflexões pessoais profundas
3. **Trabalho em Equipe (41-60)** - Fortalecer união do grupo
4. **Espirituais (61-80)** - Conexão com Deus
5. **Diversão e Energia (81-100)** - Atividades animadas
6. **Profundas (101-120)** - Momentos marcantes

## 💻 Tecnologias Utilizadas

### Backend
- **Django 5.0** - Framework web
- **Python 3.12** - Linguagem
- **PostgreSQL** - Banco de dados
- **Django Allauth** - Autenticação
- **Gunicorn** - Servidor WSGI
- **WhiteNoise** - Arquivos estáticos

### Frontend
- **Bootstrap 5** - Framework CSS
- **Bootstrap Icons** - Ícones
- **JavaScript Vanilla** - Interatividade

### DevOps
- **Render** - Hospedagem
- **Git** - Controle de versão

## 🔐 Segurança

- ✅ HTTPS obrigatório em produção
- ✅ Cookies seguros
- ✅ CSRF protection
- ✅ XSS protection
- ✅ Senhas hasheadas com PBKDF2
- ✅ Variáveis de ambiente para dados sensíveis

## 📈 Escalabilidade e Melhorias Futuras

### Fase 1 - Monetização (Stripe)
```python
# Já preparado no código:
- Campo is_premium nas dinâmicas
- Campo is_assinante nos usuários
- UserProfile com stripe_customer_id e stripe_subscription_id

# Próximos passos:
1. Integrar Stripe Checkout
2. Criar página de planos e preços
3. Webhook para renovações
4. Portal de gerenciamento de assinatura
```

### Fase 2 - Recursos Adicionais
- [ ] Exportar dinâmicas em PDF
- [ ] Sistema de comentários e avaliações
- [ ] Upload de imagens para dinâmicas
- [ ] Versão mobile (PWA)
- [ ] Notificações por email
- [ ] Sistema de tags customizadas

### Fase 3 - Social e Comunidade
- [ ] Compartilhar dinâmicas entre usuários
- [ ] Criar e salvar dinâmicas personalizadas
- [ ] Fórum de discussão
- [ ] Blog com dicas de retiros
- [ ] Planos para equipes/igrejas

### Fase 4 - Analytics e IA
- [ ] Dashboard de métricas de uso
- [ ] Recomendação de dinâmicas por IA
- [ ] Gerador de roteiro de retiro
- [ ] Relatórios de engajamento

## 🎯 Estratégia de Monetização

### Modelo Freemium

**Plano Gratuito** (R$ 0/mês)
- Acesso a 60 dinâmicas básicas
- Busca e filtros limitados
- 10 favoritos máximo

**Plano Premium** (R$ 29,90/mês)
- Acesso a todas as 120+ dinâmicas
- Dinâmicas exclusivas
- Favoritos ilimitados
- Exportar PDF
- Sem anúncios
- Suporte prioritário

**Plano Igreja** (R$ 89,90/mês)
- Tudo do Premium
- 10 contas de usuário
- Dinâmicas personalizadas
- API de integração
- Consultoria mensal

### Projeção Financeira

- **Ano 1**: 100 usuários pagantes = R$ 2.990/mês
- **Ano 2**: 500 usuários pagantes = R$ 14.950/mês
- **Ano 3**: 2.000 usuários pagantes = R$ 59.800/mês

## 🛠️ Comandos Úteis

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Executar servidor
python manage.py runserver

# Coletar estáticos
python manage.py collectstatic

# Shell Django
python manage.py shell

# Testes
python manage.py test

# Popular banco
python manage.py shell < populate_dinamicas.py
```

## 📝 Administração

Acesse `/admin` para gerenciar:
- ✏️ Criar/Editar dinâmicas
- 👥 Gerenciar usuários
- 💎 Ativar/Desativar assinaturas
- 📊 Visualizar estatísticas

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Desenvolvedor

Desenvolvido com ❤️ e ☕ para a glória de Deus

## 📞 Suporte

- Email: contato@dinamicas.com
- WhatsApp: (11) 99999-9999
- Instagram: @dinamicas_igreja

---

**"Não deixem de se reunir como igreja." - Hebreus 10:25** 🙏
