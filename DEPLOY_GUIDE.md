# Guia de Deploy - Calculadora de Orçamentos SaaS

Este guia fornece instruções passo a passo para fazer o deploy da plataforma no Vercel.

## Pré-requisitos

- Conta no GitHub
- Conta no Vercel
- Todos os arquivos do projeto

## Passo 1: Preparar o Repositório GitHub

### 1.1 Criar Repositório
1. Acesse [github.com](https://github.com)
2. Clique em "New repository"
3. Nome sugerido: `budget-calculator-saas`
4. Marque como "Public" ou "Private" conforme preferir
5. Clique em "Create repository"

### 1.2 Upload dos Arquivos
1. Na página do repositório criado, clique em "uploading an existing file"
2. Arraste e solte TODOS os arquivos do projeto, incluindo:
   - Pasta `backend/`
   - Pasta `frontend/`
   - Pasta `api/`
   - Arquivo `vercel.json`
   - Arquivo `requirements.txt`
   - Arquivo `.env.example`
   - Arquivo `README.md`
   - Arquivo `.gitignore`
3. Adicione uma mensagem de commit: "Initial commit - Budget Calculator SaaS"
4. Clique em "Commit changes"

## Passo 2: Configurar Deploy no Vercel

### 2.1 Conectar ao Vercel
1. Acesse [vercel.com](https://vercel.com)
2. Clique em "Sign up" ou "Log in"
3. Escolha "Continue with GitHub"
4. Autorize o Vercel a acessar sua conta GitHub

### 2.2 Importar Projeto
1. No dashboard do Vercel, clique em "New Project"
2. Encontre seu repositório `budget-calculator-saas`
3. Clique em "Import"

### 2.3 Configurar Variáveis de Ambiente
Antes de fazer o deploy, configure as seguintes variáveis:

1. Na tela de configuração do projeto, vá para "Environment Variables"
2. Adicione as seguintes variáveis:

```
DATABASE_URL = sqlite:///./budget_calculator.db
SECRET_KEY = sua-chave-secreta-super-forte-aqui-mude-em-producao
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALLOWED_ORIGINS = ["*"]
ADMIN_EMAIL = seu-email@exemplo.com
ADMIN_PASSWORD = sua-senha-admin-segura
ENVIRONMENT = production
```

**⚠️ IMPORTANTE**: 
- Substitua `sua-chave-secreta-super-forte-aqui-mude-em-producao` por uma chave aleatória de pelo menos 32 caracteres
- Substitua `seu-email@exemplo.com` pelo seu email de administrador
- Substitua `sua-senha-admin-segura` por uma senha forte para o administrador

### 2.4 Fazer Deploy
1. Após configurar as variáveis, clique em "Deploy"
2. Aguarde o processo de build e deploy (pode levar alguns minutos)
3. Quando concluído, você receberá uma URL da sua aplicação

## Passo 3: Configuração Inicial da Plataforma

### 3.1 Primeiro Acesso
1. Acesse a URL fornecida pelo Vercel
2. Clique em "Cadastre-se"
3. Use as credenciais de administrador configuradas nas variáveis de ambiente
4. Após o cadastro, você será o primeiro usuário administrador

### 3.2 Configurações Iniciais
1. Acesse o painel administrativo
2. Configure materiais e preços iniciais
3. Teste a criação de um orçamento
4. Verifique a geração de PDF

## Passo 4: Configurações Avançadas (Opcional)

### 4.1 Banco de Dados PostgreSQL
Para produção, recomenda-se usar PostgreSQL:

1. Crie uma conta em um provedor como:
   - [Supabase](https://supabase.com) (gratuito)
   - [Railway](https://railway.app)
   - [PlanetScale](https://planetscale.com)

2. Obtenha a URL de conexão do banco

3. No Vercel, atualize a variável `DATABASE_URL`:
   ```
   DATABASE_URL = postgresql://usuario:senha@host:porta/database
   ```

### 4.2 Domínio Personalizado
1. No dashboard do Vercel, vá para "Settings" > "Domains"
2. Adicione seu domínio personalizado
3. Configure os DNS conforme instruções do Vercel

## Passo 5: Manutenção e Atualizações

### 5.1 Atualizações Automáticas
- Qualquer commit no repositório GitHub dispara um novo deploy automaticamente
- Monitore os logs de deploy no dashboard do Vercel

### 5.2 Backup de Dados
- Configure backups regulares do banco de dados
- Exporte configurações importantes periodicamente

### 5.3 Monitoramento
- Use o dashboard do Vercel para monitorar performance
- Configure alertas para erros ou problemas

## Solução de Problemas

### Build Falha
1. Verifique os logs de build no Vercel
2. Confirme que todos os arquivos foram enviados corretamente
3. Verifique se as dependências estão corretas

### Erro de Banco de Dados
1. Verifique a variável `DATABASE_URL`
2. Confirme que o banco está acessível
3. Verifique as credenciais de conexão

### Problemas de Autenticação
1. Verifique a variável `SECRET_KEY`
2. Confirme que as credenciais de admin estão corretas
3. Limpe o cache do navegador

## Suporte

Para problemas técnicos:
1. Consulte os logs do Vercel
2. Verifique a documentação do FastAPI e React
3. Entre em contato com o suporte técnico

---

**Parabéns!** Sua plataforma de calculadora de orçamentos está agora online e pronta para uso! 🎉

