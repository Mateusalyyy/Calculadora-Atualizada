# Guia de Upload para o GitHub via Git

Este guia detalha como fazer o upload do projeto completo para um repositório GitHub usando a linha de comando Git. Este método é o mais recomendado para projetos com muitos arquivos, pois contorna as limitações de upload da interface web do GitHub.

## Pré-requisitos

- **Git instalado**: Certifique-se de ter o Git instalado em seu computador. Você pode baixá-lo em [git-scm.com](https://git-scm.com/downloads).
- **Conta GitHub**: Você precisará de uma conta no GitHub.
- **Projeto local**: Tenha o projeto `budget-calculator-saas` descompactado em seu computador.

## Passo 1: Criar um Novo Repositório no GitHub

1. Acesse o GitHub e faça login em sua conta.
2. No canto superior direito, clique no ícone `+` e selecione `New repository`.
3. **Repository name**: Digite `budget-calculator-saas` (ou o nome que preferir para o seu projeto).
4. **Description (optional)**: Adicione uma breve descrição do seu projeto.
5. Escolha `Public` ou `Private` conforme sua preferência.
6. **NÃO** marque as opções para adicionar `README file`, `.gitignore` ou `license`. Você já tem esses arquivos no seu projeto local.
7. Clique em `Create repository`.

Após a criação, o GitHub exibirá uma página com instruções para configurar seu repositório. Mantenha esta página aberta, pois você precisará da URL do repositório.

## Passo 2: Inicializar o Repositório Git Local

1. Abra o terminal ou prompt de comando em seu computador.
2. Navegue até a pasta raiz do seu projeto `budget-calculator-saas`.
   ```bash
   cd /caminho/para/sua/pasta/budget-calculator-saas
   ```
   (Substitua `/caminho/para/sua/pasta/` pelo caminho real onde você descompactou o projeto.)

3. Inicialize um novo repositório Git:
   ```bash
   git init
   ```
   Você verá uma mensagem como `Initialized empty Git repository in /caminho/para/sua/pasta/budget-calculator-saas/.git/`.

## Passo 3: Adicionar e Commitar os Arquivos

1. Adicione todos os arquivos do projeto ao stage (área de preparação) do Git. O comando `.` significa todos os arquivos e pastas no diretório atual:
   ```bash
   git add .
   ```
   Este comando pode levar alguns segundos, dependendo do número de arquivos.

2. Crie o primeiro commit com uma mensagem descritiva:
   ```bash
   git commit -m "Initial commit: Full Budget Calculator SaaS project"
   ```
   Você verá uma lista de todos os arquivos adicionados e uma confirmação do commit.

## Passo 4: Conectar ao Repositório Remoto e Enviar os Arquivos

1. Adicione o repositório remoto do GitHub ao seu repositório local. Substitua `YOUR_REPOSITORY_URL` pela URL HTTPS do seu repositório GitHub (ex: `https://github.com/seu-usuario/budget-calculator-saas.git`). Você pode copiar esta URL da página do seu repositório no GitHub.
   ```bash
   git remote add origin YOUR_REPOSITORY_URL
   ```

2. Renomeie sua branch principal para `main` (se ainda não for):
   ```bash
   git branch -M main
   ```

3. Envie os arquivos do seu repositório local para o GitHub:
   ```bash
   git push -u origin main
   ```
   - Se for a primeira vez que você usa o Git com o GitHub, ele pode pedir seu nome de usuário e senha do GitHub. Se você usa autenticação de dois fatores, precisará gerar um Personal Access Token (PAT) no GitHub e usá-lo como senha.
   - Para gerar um PAT: Vá em `Settings` > `Developer settings` > `Personal access tokens` > `Tokens (classic)` > `Generate new token`. Dê as permissões necessárias (repo, workflow) e copie o token gerado.

## Passo 5: Verificar no GitHub

Após o `git push` ser concluído com sucesso, retorne à página do seu repositório no GitHub e atualize a página. Você deverá ver todos os arquivos do seu projeto lá!

## Próximos Passos

Com o projeto no GitHub, você pode seguir o `DEPLOY_GUIDE.md` para configurar o deploy contínuo no Vercel. Qualquer alteração que você fizer no seu projeto local e enviar para o GitHub (`git add .`, `git commit -m "mensagem"`, `git push origin main`) será automaticamente refletida no Vercel.

