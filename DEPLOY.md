# Guia de Deploy no Render - +100 Dinâmicas Para Retiro

## 📋 Pré-requisitos

- Conta no GitHub
- Conta no Render (render.com)
- Código do projeto no GitHub
- PostgreSQL configurado

## 🚀 Passo a Passo Completo

### 1. Preparar Repositório GitHub

```bash
# Inicialize o Git (se ainda não fez)
git init

# Adicione todos os arquivos
git add .

# Faça o commit
git commit -m "Initial commit - MicroSaaS Dinâmicas"

# Adicione o remote do GitHub
git remote add origin https://github.com/seu-usuario/dinamicas-igreja.git

# Envie para o GitHub
git push -u origin main
```

### 2. Criar PostgreSQL Database no Render

1. Acesse [Render Dashboard](https://dashboard.render.com)
2. Clique em **"New +"** → **"PostgreSQL"**
3. Configure:
   - **Name**: `dinamicas-igreja-db`
   - **Database**: `dinamicas_igreja`
   - **User**: `dinamicas_user`
   - **Region**: `Oregon (US West)`
   - **Plan**: Free (para teste) ou Starter
4. Clique em **"Create Database"**
5. **IMPORTANTE**: Copie e salve a **Internal Database URL**

### 3. Criar Web Service no Render

1. No Dashboard, clique em **"New +"** → **"Web Service"**
2. Conecte seu repositório GitHub
3. Configure:

#### Build & Deploy Settings

```
Name: dinamicas-igreja
Region: Oregon (US West)
Branch: main
Runtime: Python 3

Build Command:
./build.sh

Start Command:
gunicorn config.wsgi:application
```

#### Environment Variables

Adicione as seguintes variáveis:

```
SECRET_KEY=<gere-em-djecrety.ir>
DEBUG=False
ALLOWED_HOSTS=.onrender.com
DATABASE_URL=<cole-a-URL-do-postgres>
PYTHON_VERSION=3.12.1

# Opcional - Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=senha-app-gmail

# Opcional - Stripe (futuro)
STRIPE_PUBLIC_KEY=
STRIPE_SECRET_KEY=
```

4. Clique em **"Create Web Service"**

### 4. Verificar Build e Deploy

1. Aguarde o build automático (3-5 minutos)
2. Verifique os logs em tempo real
3. Procure por:
   - ✅ `Build successful`
   - ✅ `Migrations completed`
   - ✅ `Static files collected`

### 5. Criar Superusuário

Após deploy bem-sucedido:

1. No Render Dashboard, vá até seu Web Service
2. Clique em **"Shell"** (terminal)
3. Execute:

```bash
python manage.py createsuperuser
```

4. Preencha:
   - Email: seu@email.com
   - Password: (senha segura)
   - Password confirmation: (mesma senha)

### 6. Popular com Dinâmicas

No mesmo Shell do Render:

```bash
python manage.py shell < populate_dinamicas.py
```

### 7. Acessar a Aplicação

Seu site estará disponível em:
```
https://dinamicas-igreja.onrender.com
```

Admin:
```
https://dinamicas-igreja.onrender.com/admin
```

## 🔧 Configurações Avançadas

### Custom Domain (Domínio Próprio)

1. Compre um domínio (ex: Registro.br, GoDaddy)
2. No Render Dashboard → Settings → Custom Domains
3. Adicione seu domínio
4. Configure DNS com os registros fornecidos pelo Render

### HTTPS/SSL

✅ Automático no Render! SSL gratuito com Let's Encrypt.

### Continuous Deployment

✅ Já configurado! Cada push para `main` faz deploy automático.

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError"

**Solução**: Verifique se `requirements.txt` está correto
```bash
# No Shell do Render
pip list
```

### Erro: "Database connection failed"

**Solução**: Verifique `DATABASE_URL`
1. Copie novamente a Internal URL do PostgreSQL
2. Atualize a variável de ambiente
3. Faça novo deploy manual

### Erro: "Static files not found"

**Solução**: Execute manualmente
```bash
python manage.py collectstatic --noinput
```

### Site muito lento

**Problema**: Plano Free do Render hiberna após 15 min de inatividade

**Soluções**:
1. Upgrade para plano Starter ($7/mês)
2. Use serviço de "ping" para manter ativo
3. Implemente cache com Redis

## 📊 Monitoramento

### Logs em Tempo Real

```bash
# No Render Dashboard → Logs
# Ou pela CLI:
render logs dinamicas-igreja
```

### Métricas

- CPU Usage
- Memory Usage
- Response Time
- Request Count

Disponível em: Dashboard → Metrics

## 🔐 Segurança em Produção

### Checklist Obrigatório

- [x] `DEBUG=False`
- [x] `SECRET_KEY` forte e única
- [x] `ALLOWED_HOSTS` configurado
- [x] HTTPS ativo
- [x] Database com senha forte
- [x] Variáveis sensíveis em Environment Variables

### Backup do Banco

No PostgreSQL do Render:
1. Settings → Backups
2. Ative backups automáticos
3. Configure retenção (7, 14, 30 dias)

## 💰 Custos Estimados

### Plano Gratuito (Free Tier)
- **Web Service**: Free (hibernação após 15 min)
- **PostgreSQL**: Free (90 dias, depois $7/mês)
- **Total**: R$ 0 (teste) ou R$ 35/mês

### Plano Inicial (Starter)
- **Web Service**: $7/mês
- **PostgreSQL**: $7/mês
- **Custom Domain**: Grátis
- **SSL**: Grátis
- **Total**: R$ 70/mês (aproximado)

### Plano Profissional
- **Web Service**: $25/mês (2GB RAM)
- **PostgreSQL**: $25/mês (8GB)
- **Total**: R$ 250/mês

## 🔄 Atualizações e Manutenção

### Atualizar Código

```bash
# Local
git add .
git commit -m "Nova funcionalidade"
git push origin main

# Render faz deploy automático!
```

### Executar Migrações Novas

```bash
# Adicione ao build.sh (já está configurado)
python manage.py migrate
```

### Adicionar Nova Dependência

1. Adicione ao `requirements.txt`
2. Commit e push
3. Render reinstala automaticamente

## 📞 Suporte Render

- Documentação: https://render.com/docs
- Comunidade: https://community.render.com
- Status: https://status.render.com

## ✅ Checklist Final

Antes de lançar para usuários:

- [ ] Deploy bem-sucedido
- [ ] Banco populado com dinâmicas
- [ ] Superusuário criado
- [ ] Todas as páginas carregando
- [ ] Login funcionando
- [ ] Cadastro funcionando
- [ ] Favoritos funcionando
- [ ] Busca funcionando
- [ ] Admin acessível
- [ ] SSL ativo (HTTPS)
- [ ] Email configurado
- [ ] Backup ativo
- [ ] Monitoramento configurado

## 🎉 Pronto para Produção!

Seu MicroSaaS está no ar! 🚀

Próximos passos:
1. Divulgue nas redes sociais
2. Colete feedback dos primeiros usuários
3. Implemente melhorias
4. Ative sistema de pagamento
5. Escale conforme crescimento

---

**Dúvidas?** Entre em contato pelo suporte.
