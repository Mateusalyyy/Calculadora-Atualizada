# Calculadora de Orçamentos - SaaS

Uma plataforma SaaS completa para criação e gestão de orçamentos, desenvolvida com FastAPI (backend) e React (frontend).

## Funcionalidades

### Para Vendedores
- ✅ Criação de orçamentos com múltiplos itens
- ✅ Seleção de materiais pré-cadastrados
- ✅ Cálculo automático de totais, descontos e impostos
- ✅ Geração de PDFs profissionais
- ✅ Histórico de orçamentos criados
- ✅ Edição de orçamentos existentes

### Para Administradores
- ✅ Gestão de usuários (aprovação, desativação)
- ✅ Visualização de todos os orçamentos
- ✅ Configuração de materiais e preços
- ✅ Sincronização com planilhas Excel
- ✅ Configurações administrativas em tempo real
- ✅ Dashboard com métricas

## Tecnologias Utilizadas

### Backend
- **FastAPI** - Framework web moderno e de alta performance
- **SQLAlchemy** - ORM para interação com banco de dados
- **PostgreSQL/SQLite** - Banco de dados relacional
- **JWT** - Autenticação e autorização
- **Pydantic** - Validação de dados

### Frontend
- **React** - Biblioteca para interfaces de usuário
- **Tailwind CSS** - Framework CSS utilitário
- **shadcn/ui** - Componentes de interface
- **React Router** - Roteamento
- **Axios** - Cliente HTTP
- **jsPDF** - Geração de PDFs

### Deploy
- **Vercel** - Plataforma de deploy
- **GitHub** - Controle de versão

## Estrutura do Projeto

```
budget-calculator-saas/
├── backend/                 # Código do servidor
│   ├── app/
│   │   ├── routes/         # Rotas da API
│   │   ├── models/         # Modelos de dados
│   │   ├── schemas/        # Schemas de validação
│   │   ├── services/       # Lógica de negócio
│   │   └── core/           # Configurações
│   └── requirements.txt    # Dependências Python
├── frontend/               # Código do cliente
│   ├── src/
│   │   ├── components/     # Componentes React
│   │   ├── pages/          # Páginas da aplicação
│   │   ├── lib/            # Utilitários
│   │   └── assets/         # Recursos estáticos
│   └── package.json        # Dependências Node.js
├── api/                    # Ponto de entrada para Vercel
├── vercel.json             # Configuração de deploy
├── .env.example            # Exemplo de variáveis de ambiente
└── README.md               # Este arquivo
```

## Configuração Local

### Pré-requisitos
- Python 3.11+
- Node.js 18+
- pnpm ou npm

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
pnpm install
pnpm run dev --host
```

## Deploy no Vercel

1. **Criar repositório no GitHub**
   - Faça upload de todos os arquivos para um repositório GitHub

2. **Conectar ao Vercel**
   - Acesse [vercel.com](https://vercel.com)
   - Conecte sua conta GitHub
   - Importe o repositório

3. **Configurar variáveis de ambiente**
   ```
   DATABASE_URL=sua_url_do_banco
   SECRET_KEY=sua_chave_secreta
   ADMIN_EMAIL=admin@exemplo.com
   ADMIN_PASSWORD=senha_admin
   ```

4. **Deploy automático**
   - O Vercel fará o deploy automaticamente
   - Atualizações no GitHub disparam novos deploys

## Uso da Plataforma

### Primeiro Acesso (Administrador)
1. Acesse a plataforma
2. Registre-se com as credenciais de administrador
3. Configure materiais e preços
4. Aprove novos usuários

### Vendedores
1. Registre-se na plataforma
2. Aguarde aprovação do administrador
3. Acesse a calculadora de orçamentos
4. Crie e gerencie seus orçamentos

### Configurações Administrativas
- **Materiais**: Cadastre materiais com preços
- **Excel**: Sincronize com planilhas externas
- **Usuários**: Gerencie vendedores
- **APIs**: Configure integrações

## Segurança

- Autenticação JWT
- Senhas criptografadas
- Validação de dados
- Controle de acesso por roles
- Variáveis de ambiente para secrets

## Suporte

Para dúvidas ou problemas:
1. Verifique a documentação
2. Consulte os logs de erro
3. Entre em contato com o administrador

---

Desenvolvido com ❤️ pela equipe Manus AI

