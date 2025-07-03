# Guia Completo de Uso - Calculadora de Orçamentos SaaS

**Versão:** 1.0  
**Autor:** Manus AI  
**Data:** Junho 2025

---

## Índice

1. [Introdução](#introdução)
2. [Primeiros Passos](#primeiros-passos)
3. [Interface da Plataforma](#interface-da-plataforma)
4. [Funcionalidades para Vendedores](#funcionalidades-para-vendedores)
5. [Funcionalidades Administrativas](#funcionalidades-administrativas)
6. [Configurações Avançadas](#configurações-avançadas)
7. [Solução de Problemas](#solução-de-problemas)
8. [Perguntas Frequentes](#perguntas-frequentes)

---

## Introdução

A Calculadora de Orçamentos SaaS é uma plataforma completa desenvolvida para facilitar a criação, gestão e acompanhamento de orçamentos comerciais. Projetada para atender tanto vendedores quanto administradores, a plataforma oferece uma interface intuitiva e funcionalidades robustas que permitem desde a criação rápida de orçamentos até a gestão completa de usuários e configurações empresariais.

### Principais Benefícios

A plataforma foi desenvolvida com foco na produtividade e eficiência operacional. Para vendedores, oferece uma interface simplificada que permite a criação rápida de orçamentos profissionais, com cálculos automáticos e geração instantânea de PDFs. Para administradores, proporciona controle total sobre usuários, materiais, preços e configurações, incluindo a capacidade de sincronizar dados com planilhas Excel externas.

### Arquitetura e Tecnologia

Construída com tecnologias modernas, a plataforma utiliza FastAPI no backend para garantir alta performance e escalabilidade, enquanto o frontend em React oferece uma experiência de usuário fluida e responsiva. A integração com o Vercel permite deploy contínuo e alta disponibilidade, enquanto o sistema de autenticação JWT garante a segurança dos dados.

---


## Primeiros Passos

### Acesso à Plataforma

O primeiro passo para utilizar a Calculadora de Orçamentos é acessar a plataforma através do navegador web. A URL será fornecida pelo administrador do sistema ou estará disponível após o deploy no Vercel. A plataforma é totalmente responsiva, funcionando perfeitamente em computadores desktop, tablets e smartphones.

### Processo de Registro

Para novos usuários, o processo de registro é simples e direto. Na página inicial, clique no link "Cadastre-se" localizado abaixo do formulário de login. Você será direcionado para um formulário de registro que solicita as seguintes informações essenciais:

**Nome de usuário**: Este será seu identificador único na plataforma. Escolha um nome que seja fácil de lembrar e profissional, pois ele aparecerá em relatórios e logs do sistema. O nome de usuário deve ser único e não pode ser alterado posteriormente.

**Endereço de e-mail**: Utilize um endereço de e-mail válido e que você tenha acesso regular. Este e-mail será usado para comunicações importantes do sistema e, futuramente, para recuperação de senha.

**Senha**: Crie uma senha forte que contenha pelo menos 8 caracteres, incluindo letras maiúsculas, minúsculas, números e símbolos especiais. A segurança da sua conta depende da qualidade da senha escolhida.

**Confirmação de senha**: Digite novamente a senha para confirmar que foi digitada corretamente.

Após preencher todos os campos obrigatórios, clique no botão "Criar Conta". O sistema processará sua solicitação e exibirá uma mensagem de confirmação informando que sua conta foi criada com sucesso, mas que está pendente de aprovação pelo administrador.

### Sistema de Aprovação

A plataforma implementa um sistema de aprovação para garantir que apenas usuários autorizados tenham acesso às funcionalidades. Após o registro, sua conta ficará em status "Pendente de Aprovação" até que um administrador revise e aprove sua solicitação. Este processo de segurança é fundamental para manter a integridade dos dados e controlar o acesso à plataforma.

Durante o período de espera, você receberá uma mensagem informativa explicando que sua conta está aguardando aprovação. O tempo de aprovação varia conforme a política da empresa, mas geralmente é processado em até 24 horas durante dias úteis.

### Primeiro Login

Uma vez que sua conta seja aprovada pelo administrador, você poderá fazer seu primeiro login na plataforma. Retorne à página inicial e utilize suas credenciais (nome de usuário e senha) para acessar o sistema. Após um login bem-sucedido, você será automaticamente redirecionado para a página principal da calculadora de orçamentos.

### Configuração Inicial do Perfil

Embora não seja obrigatório, recomenda-se que você familiarize-se com a interface da plataforma antes de criar seu primeiro orçamento. Explore o menu de navegação, que inclui as seções principais: Calculadora, Histórico e, se você for um administrador, as seções de Usuários e Configurações.

---


## Interface da Plataforma

### Layout e Navegação

A interface da Calculadora de Orçamentos foi projetada seguindo princípios de usabilidade e experiência do usuário, garantindo que tanto usuários iniciantes quanto experientes possam navegar facilmente pela plataforma. O layout é dividido em três componentes principais: a barra lateral de navegação, a barra superior e a área de conteúdo principal.

**Barra Lateral de Navegação**: Localizada no lado esquerdo da tela, a barra lateral contém os links principais para todas as funcionalidades da plataforma. O menu é contextual, exibindo diferentes opções baseadas no nível de permissão do usuário logado. Para vendedores, as opções incluem "Calculadora" e "Histórico". Para administradores, opções adicionais como "Usuários" e "Configurações" são exibidas.

**Barra Superior**: A barra superior contém informações do usuário logado, incluindo nome de usuário e função (vendedor ou administrador). Também inclui o botão de logout, que permite sair da plataforma de forma segura. Em dispositivos móveis, a barra superior inclui um botão de menu hambúrguer que permite acessar a navegação lateral.

**Área de Conteúdo Principal**: Esta é a área onde todo o conteúdo específico de cada página é exibido. O design responsivo garante que o conteúdo seja otimizado para diferentes tamanhos de tela, desde smartphones até monitores de desktop.

### Design Responsivo

A plataforma foi desenvolvida com uma abordagem mobile-first, garantindo que todas as funcionalidades sejam totalmente acessíveis em dispositivos móveis. O sistema de grid flexível se adapta automaticamente ao tamanho da tela, reorganizando elementos conforme necessário para manter a usabilidade em qualquer dispositivo.

Em telas menores, a barra lateral de navegação se transforma em um menu deslizante que pode ser acessado através do botão de menu na barra superior. Formulários e tabelas são otimizados para toque, com espaçamento adequado entre elementos interativos e campos de entrada dimensionados apropriadamente para digitação em telas sensíveis ao toque.

### Sistema de Cores e Tipografia

O esquema de cores da plataforma utiliza uma paleta profissional baseada em tons de azul e cinza, proporcionando uma aparência moderna e confiável. As cores foram escolhidas para garantir alto contraste e legibilidade, atendendo às diretrizes de acessibilidade WCAG 2.1.

A tipografia utiliza fontes sans-serif modernas que garantem excelente legibilidade em todas as resoluções de tela. Os tamanhos de fonte são escaláveis e se ajustam automaticamente baseados no dispositivo e preferências do usuário.

### Feedback Visual e Interações

A plataforma implementa um sistema abrangente de feedback visual para guiar os usuários através de suas interações. Botões mudam de cor quando clicados, campos de formulário destacam quando selecionados, e mensagens de status informam sobre o sucesso ou falha de operações.

Animações sutis são utilizadas para transições entre páginas e estados, proporcionando uma experiência fluida sem comprometer a performance. Indicadores de carregamento são exibidos durante operações que podem demorar alguns segundos, como a geração de PDFs ou sincronização de dados.

### Acessibilidade

A plataforma foi desenvolvida seguindo as melhores práticas de acessibilidade web. Todos os elementos interativos são acessíveis via teclado, permitindo navegação completa sem o uso do mouse. Textos alternativos são fornecidos para imagens e ícones, e a estrutura semântica do HTML garante compatibilidade com leitores de tela.

---


## Funcionalidades para Vendedores

### Criação de Orçamentos

A funcionalidade principal da plataforma para vendedores é a criação de orçamentos profissionais. Acessível através do menu "Calculadora", esta ferramenta oferece uma interface intuitiva que guia o usuário através de todo o processo de criação de um orçamento completo.

**Dados do Cliente**: O primeiro passo na criação de um orçamento é o preenchimento dos dados do cliente. O campo "Nome do Cliente" é obrigatório e deve conter o nome completo da empresa ou pessoa física para quem o orçamento está sendo preparado. O campo "Contato do Cliente" é opcional, mas recomendado, podendo incluir telefone, e-mail ou outras informações de contato relevantes.

**Adição de Itens**: A seção de itens é onde a maior parte do trabalho de criação do orçamento acontece. Cada item do orçamento pode ser adicionado individualmente, com campos específicos para descrição, quantidade, valor unitário e, opcionalmente, material pré-cadastrado.

O sistema permite a seleção de materiais da base de dados pré-configurada pelo administrador. Quando um material é selecionado, o sistema automaticamente preenche a descrição e o valor unitário baseado nas informações cadastradas. Isso não apenas acelera o processo de criação do orçamento, mas também garante consistência nos preços e descrições utilizadas.

Para itens personalizados que não estão na base de materiais, o vendedor pode optar por "Material personalizado" e preencher manualmente a descrição e o valor unitário. Esta flexibilidade permite que a plataforma seja utilizada para uma ampla variedade de produtos e serviços.

**Cálculos Automáticos**: Um dos grandes benefícios da plataforma é o sistema de cálculos automáticos. À medida que itens são adicionados ou modificados, o sistema recalcula automaticamente o valor total de cada item (quantidade × valor unitário) e o valor total do orçamento. Isso elimina erros de cálculo manual e proporciona feedback imediato sobre o impacto de mudanças nos valores.

**Descontos e Impostos**: A plataforma permite a aplicação de descontos e impostos ao orçamento. O campo de desconto aceita valores em reais e é subtraído do subtotal dos itens. O campo de impostos também aceita valores em reais e é adicionado ao valor final. Ambos os campos são opcionais e podem ser deixados em zero se não aplicáveis.

**Observações**: O campo de observações permite a inclusão de informações adicionais relevantes ao orçamento, como condições de pagamento, prazo de validade, condições de entrega, ou qualquer outra informação que o vendedor considere importante para o cliente.

### Gestão de Itens do Orçamento

O sistema de gestão de itens foi projetado para máxima flexibilidade e facilidade de uso. Cada orçamento começa com um item em branco, mas o vendedor pode adicionar quantos itens forem necessários usando o botão "Adicionar Item".

**Adição Dinâmica de Itens**: Novos itens podem ser adicionados a qualquer momento durante a criação do orçamento. Cada novo item inclui todos os campos necessários: seleção de material, descrição, quantidade e valor unitário. O sistema mantém a numeração automática dos itens para facilitar a organização.

**Remoção de Itens**: Itens podem ser removidos individualmente usando o botão de lixeira ao lado de cada item. O sistema sempre mantém pelo menos um item no orçamento, impedindo a remoção do último item restante. Quando um item é removido, os cálculos são automaticamente atualizados.

**Validação de Dados**: O sistema implementa validação em tempo real para garantir que todos os dados obrigatórios sejam preenchidos corretamente. Campos numéricos aceitam apenas valores válidos, e o sistema impede a submissão de orçamentos com dados incompletos ou inválidos.

### Geração de PDFs

Uma das funcionalidades mais importantes da plataforma é a capacidade de gerar PDFs profissionais dos orçamentos criados. Esta funcionalidade está integrada tanto no processo de criação quanto no histórico de orçamentos.

**Geração Automática**: Após a criação bem-sucedida de um orçamento, o sistema exibe uma mensagem de confirmação com um botão "Baixar PDF" que permite a geração imediata do documento. O PDF é gerado no lado do cliente usando a biblioteca jsPDF, garantindo rapidez e reduzindo a carga no servidor.

**Formatação Profissional**: Os PDFs gerados seguem um layout profissional que inclui cabeçalho com logo da empresa (quando configurada), informações do cliente, tabela detalhada de itens, resumo financeiro com subtotal, descontos, impostos e total final, além de observações e rodapé com informações de validade.

**Nomenclatura Automática**: Os arquivos PDF são automaticamente nomeados seguindo o padrão "orcamento_[nome_do_cliente]_[data].pdf", facilitando a organização e identificação dos documentos baixados.

### Histórico de Orçamentos

A funcionalidade de histórico permite que vendedores visualizem, gerenciem e acessem todos os orçamentos que criaram. Esta seção é acessível através do menu "Histórico" e oferece uma visão completa de toda a atividade de orçamentos do usuário.

**Listagem Completa**: O histórico exibe todos os orçamentos criados pelo vendedor em ordem cronológica reversa (mais recentes primeiro). Cada entrada na lista inclui informações essenciais como nome do cliente, número do orçamento, valor total, data de criação e número de itens.

**Funcionalidade de Busca**: Um campo de busca permite filtrar orçamentos por nome do cliente ou número do orçamento. A busca é realizada em tempo real, atualizando a lista conforme o usuário digita, facilitando a localização rápida de orçamentos específicos.

**Ações Disponíveis**: Para cada orçamento no histórico, estão disponíveis várias ações através de botões dedicados:
- **Visualizar**: Permite ver todos os detalhes do orçamento
- **Editar**: Abre o orçamento para modificação
- **Baixar PDF**: Gera e baixa o PDF do orçamento
- **Excluir**: Remove permanentemente o orçamento (com confirmação)

**Informações Detalhadas**: Cada entrada no histórico mostra informações contextuais importantes, incluindo data de criação, data da última modificação (se aplicável), informações de contato do cliente quando disponíveis, e um badge destacando o valor total do orçamento.

---


## Funcionalidades Administrativas

### Gestão de Usuários

Os administradores têm acesso completo ao sistema de gestão de usuários, permitindo controle total sobre quem pode acessar a plataforma e quais permissões cada usuário possui. Esta funcionalidade é acessível através do menu "Usuários" e oferece uma interface abrangente para todas as operações relacionadas a usuários.

**Aprovação de Novos Usuários**: Uma das responsabilidades principais dos administradores é a aprovação de novos registros. A seção "Usuários Pendentes" lista todos os usuários que se registraram na plataforma mas ainda não foram aprovados. Para cada usuário pendente, o administrador pode visualizar informações como nome de usuário, e-mail e data de registro.

O processo de aprovação é simples e direto. O administrador pode revisar as informações do usuário e, se tudo estiver correto, clicar no botão "Aprovar" para conceder acesso à plataforma. Uma vez aprovado, o usuário receberá automaticamente as permissões de vendedor e poderá fazer login normalmente.

**Gestão de Usuários Ativos**: A seção principal de usuários lista todos os usuários aprovados e ativos na plataforma. Para cada usuário, o administrador pode visualizar informações detalhadas incluindo nome de usuário, e-mail, função (vendedor ou administrador), status (ativo/inativo), data de criação e última atualização.

**Modificação de Permissões**: Administradores podem alterar as permissões de qualquer usuário, incluindo a promoção de vendedores para administradores ou o rebaixamento de administradores para vendedores. Esta flexibilidade permite que a estrutura organizacional da plataforma evolua conforme as necessidades da empresa.

**Desativação e Reativação**: Usuários podem ser temporariamente desativados sem perder seus dados. Usuários desativados não conseguem fazer login na plataforma, mas todos os seus orçamentos e informações permanecem intactos. Esta funcionalidade é útil para funcionários em licença ou situações temporárias onde o acesso precisa ser suspenso.

**Exclusão de Usuários**: Em casos extremos, administradores podem excluir permanentemente usuários da plataforma. Esta ação remove completamente o usuário e todos os dados associados, incluindo orçamentos criados. Por ser uma ação irreversível, o sistema solicita confirmação dupla antes de proceder com a exclusão.

### Gestão de Materiais e Preços

O sistema de gestão de materiais é uma funcionalidade fundamental que permite aos administradores manter uma base de dados atualizada de produtos e serviços com seus respectivos preços. Esta centralização garante consistência nos orçamentos e facilita atualizações de preços em toda a organização.

**Cadastro de Materiais**: Novos materiais podem ser adicionados através de um formulário intuitivo que inclui campos para nome do material, descrição detalhada, preço unitário, unidade de medida e status (ativo/inativo). O nome do material deve ser único no sistema para evitar duplicações e confusões.

**Edição de Materiais**: Materiais existentes podem ser editados a qualquer momento. Mudanças nos preços são aplicadas imediatamente e afetam novos orçamentos criados após a alteração. Orçamentos já existentes mantêm os preços que estavam vigentes no momento de sua criação, garantindo a integridade histórica dos dados.

**Controle de Status**: Materiais podem ser marcados como ativos ou inativos. Materiais inativos não aparecem na lista de seleção durante a criação de orçamentos, mas continuam visíveis em orçamentos históricos onde foram utilizados. Esta funcionalidade é útil para produtos descontinuados ou temporariamente indisponíveis.

**Organização e Categorização**: Embora a versão atual não inclua categorização formal, a funcionalidade de busca e filtros permite organização eficiente dos materiais. Recomenda-se o uso de convenções de nomenclatura consistentes para facilitar a localização e gestão dos materiais.

### Sincronização com Excel

Uma das funcionalidades mais avançadas da plataforma é a capacidade de sincronizar materiais e preços com planilhas Excel externas. Esta funcionalidade permite que empresas que já mantêm suas listas de preços em Excel continuem usando suas ferramentas existentes enquanto se beneficiam da automação da plataforma.

**Configuração da URL do Excel**: Administradores podem configurar a URL de uma planilha Excel hospedada online (como Google Sheets exportado como Excel ou arquivos em serviços de nuvem). A URL deve apontar para um arquivo Excel acessível publicamente ou através de autenticação configurada.

**Formato da Planilha**: A planilha Excel deve seguir um formato específico para que a sincronização funcione corretamente. As colunas obrigatórias incluem "nome" (nome do material), "preco_unitario" (preço unitário numérico), e opcionalmente "descricao" (descrição do material), "unidade_medida" (unidade de medida) e "ativo" (status ativo/inativo).

**Processo de Sincronização**: A sincronização pode ser executada manualmente através do botão "Sincronizar Materiais" no painel administrativo. O sistema baixa a planilha Excel, processa os dados e atualiza a base de materiais da plataforma. Materiais existentes são atualizados com novos preços, e novos materiais são adicionados automaticamente.

**Relatório de Sincronização**: Após cada sincronização, o sistema fornece um relatório detalhado mostrando quantos materiais foram criados, atualizados ou tiveram erros durante o processo. Este feedback permite que administradores identifiquem e corrijam problemas na planilha fonte.

### Configurações Administrativas

O painel de configurações administrativas oferece controle sobre diversos aspectos operacionais da plataforma, permitindo personalização e ajustes conforme as necessidades específicas da organização.

**Gestão de Chaves de API**: Administradores podem configurar e gerenciar chaves de API para integrações com serviços externos. Estas chaves são armazenadas de forma segura e podem ser atualizadas conforme necessário. O sistema suporta integração com diversos serviços, incluindo Monday.com e outros sistemas de gestão empresarial.

**Configurações de Segurança**: Parâmetros de segurança como tempo de expiração de tokens de autenticação, políticas de senha e configurações de CORS podem ser ajustados através desta interface. Mudanças em configurações de segurança são aplicadas imediatamente e afetam todas as sessões ativas.

**Personalização da Marca**: Embora a funcionalidade de upload de logo não esteja implementada na versão atual, o sistema está preparado para incluir elementos de marca personalizados nos PDFs gerados. Administradores podem configurar informações da empresa que aparecem nos documentos gerados.

### Dashboard Administrativo

O dashboard administrativo fornece uma visão geral abrangente da atividade e performance da plataforma, oferecendo métricas importantes para tomada de decisões e monitoramento operacional.

**Métricas de Usuários**: O dashboard exibe estatísticas detalhadas sobre usuários, incluindo número total de usuários registrados, usuários ativos, usuários pendentes de aprovação e distribuição por função (vendedores vs. administradores). Estas métricas ajudam a entender o crescimento e engajamento da base de usuários.

**Estatísticas de Orçamentos**: Informações sobre orçamentos incluem número total de orçamentos criados, valor total dos orçamentos gerados, orçamentos criados no período atual e tendências de crescimento. Estas métricas são valiosas para análise de performance de vendas e planejamento estratégico.

**Status do Sistema**: O dashboard também inclui informações sobre o status operacional da plataforma, incluindo número de materiais cadastrados, materiais ativos, última sincronização com Excel (quando aplicável) e outras métricas técnicas relevantes.

**Análise Temporal**: Embora não implementada na versão atual, o sistema está preparado para incluir análises temporais que mostram tendências ao longo do tempo, permitindo identificação de padrões sazonais e crescimento da atividade.

---


## Configurações Avançadas

### Integração com Sistemas Externos

A plataforma foi projetada com extensibilidade em mente, oferecendo capacidades de integração com diversos sistemas externos através de APIs e configurações administrativas. Estas integrações permitem que a plataforma se torne parte de um ecossistema empresarial mais amplo.

**Integração com Monday.com**: O sistema suporta integração com Monday.com através de chaves de API configuráveis. Esta integração permite sincronização de dados de projetos, clientes e outras informações relevantes que podem ser utilizadas na criação de orçamentos. A configuração é realizada através do painel administrativo, onde a chave de API do Monday.com pode ser inserida e testada.

**Webhooks e Notificações**: Embora não implementado na versão atual, o sistema está preparado para suportar webhooks que podem notificar sistemas externos sobre eventos importantes, como criação de novos orçamentos, aprovação de usuários ou atualizações de materiais.

**APIs RESTful**: Toda a funcionalidade da plataforma está exposta através de APIs RESTful bem documentadas, permitindo que desenvolvedores criem integrações personalizadas ou aplicações complementares. A documentação da API está disponível através do endpoint `/docs` da aplicação.

### Personalização e Branding

A plataforma oferece várias opções de personalização para que empresas possam adaptar a ferramenta à sua identidade visual e necessidades específicas.

**Customização de PDFs**: Os PDFs gerados podem ser personalizados com logos da empresa, cores corporativas e informações específicas da organização. Embora a funcionalidade de upload de logo não esteja implementada na interface atual, o sistema está preparado para incluir imagens corporativas nos documentos gerados.

**Configuração de Informações da Empresa**: Administradores podem configurar informações da empresa que aparecem nos PDFs, incluindo nome da empresa, endereço, telefone, e-mail e outras informações de contato relevantes. Estas informações são incluídas automaticamente em todos os orçamentos gerados.

**Personalização de Campos**: Embora não disponível na versão atual, o sistema foi projetado para suportar campos personalizados que podem ser adicionados aos orçamentos conforme necessidades específicas de diferentes tipos de negócio.

### Backup e Recuperação de Dados

A segurança e integridade dos dados são prioridades fundamentais da plataforma. Várias medidas estão implementadas para garantir que os dados estejam sempre protegidos e recuperáveis.

**Backup Automático**: Quando hospedada em serviços de nuvem como Vercel com bancos de dados gerenciados, a plataforma se beneficia de backups automáticos fornecidos pela infraestrutura. Recomenda-se a configuração de backups regulares conforme as políticas da organização.

**Exportação de Dados**: Embora não implementada na interface atual, a arquitetura da plataforma permite a implementação de funcionalidades de exportação de dados que permitiriam aos administradores baixar todos os dados em formatos padrão como CSV ou JSON.

**Recuperação de Dados**: Em caso de problemas, a arquitetura baseada em banco de dados relacional facilita a recuperação de dados através de backups. Recomenda-se a implementação de procedimentos regulares de backup e teste de recuperação.

---

## Solução de Problemas

### Problemas Comuns de Login

**Erro: "Credenciais inválidas ou usuário não aprovado"**: Este erro pode ocorrer por várias razões. Primeiro, verifique se o nome de usuário e senha estão corretos, prestando atenção a maiúsculas e minúsculas. Se as credenciais estiverem corretas, o problema pode ser que sua conta ainda não foi aprovada por um administrador. Entre em contato com o administrador do sistema para verificar o status da sua conta.

**Erro: "Token inválido"**: Este erro geralmente indica que sua sessão expirou. Faça logout e login novamente. Se o problema persistir, limpe o cache do navegador e tente novamente.

**Problemas de Carregamento da Página**: Se a página de login não carregar corretamente, verifique sua conexão com a internet e tente atualizar a página. Se o problema persistir, pode haver um problema temporário com o servidor.

### Problemas na Criação de Orçamentos

**Erro: "Erro ao criar orçamento"**: Este erro pode ocorrer se houver problemas de conectividade ou se dados obrigatórios não foram preenchidos corretamente. Verifique se todos os campos obrigatórios estão preenchidos e se os valores numéricos estão em formato correto.

**Materiais não aparecem na lista**: Se materiais cadastrados pelo administrador não aparecem na lista de seleção, pode ser que estejam marcados como inativos. Entre em contato com o administrador para verificar o status dos materiais.

**Cálculos incorretos**: Se os cálculos automáticos parecerem incorretos, verifique se os valores inseridos estão no formato correto (use ponto como separador decimal) e se não há caracteres especiais nos campos numéricos.

### Problemas com Geração de PDF

**PDF não é gerado**: Se o botão de download de PDF não funcionar, verifique se seu navegador permite downloads automáticos. Alguns navegadores bloqueiam downloads automáticos por padrão.

**PDF com formatação incorreta**: Se o PDF gerado não estiver formatado corretamente, pode ser um problema temporário. Tente gerar o PDF novamente. Se o problema persistir, entre em contato com o suporte técnico.

**Logo não aparece no PDF**: A funcionalidade de logo personalizado pode não estar configurada. Entre em contato com o administrador para configurar a logo da empresa.

### Problemas Administrativos

**Erro ao sincronizar materiais**: Se a sincronização com Excel falhar, verifique se a URL da planilha está correta e acessível. Certifique-se de que a planilha contém as colunas obrigatórias no formato correto.

**Usuários não conseguem ser aprovados**: Se houver problemas ao aprovar usuários, verifique sua conexão com a internet e tente novamente. Se o problema persistir, pode haver um problema temporário com o servidor.

---

## Perguntas Frequentes

**P: Posso usar a plataforma em dispositivos móveis?**
R: Sim, a plataforma é totalmente responsiva e funciona perfeitamente em smartphones e tablets. Todas as funcionalidades estão disponíveis em dispositivos móveis.

**P: Quantos orçamentos posso criar?**
R: Não há limite para o número de orçamentos que você pode criar. A plataforma foi projetada para suportar uso intensivo.

**P: Os dados são seguros?**
R: Sim, a plataforma implementa várias medidas de segurança, incluindo autenticação JWT, criptografia de senhas e validação de dados. Todos os dados são transmitidos através de conexões seguras HTTPS.

**P: Posso editar orçamentos após criá-los?**
R: Sim, orçamentos podem ser editados a qualquer momento através da funcionalidade de histórico. Vendedores podem editar apenas seus próprios orçamentos, enquanto administradores podem editar qualquer orçamento.

**P: Como posso recuperar minha senha?**
R: A funcionalidade de recuperação de senha não está implementada na versão atual. Entre em contato com um administrador para redefinir sua senha.

**P: Posso exportar dados da plataforma?**
R: A funcionalidade de exportação não está disponível na interface atual, mas pode ser implementada conforme necessário. Entre em contato com o suporte técnico para discutir opções de exportação.

**P: A plataforma funciona offline?**
R: Não, a plataforma requer conexão com a internet para funcionar, pois é uma aplicação web que depende de comunicação com o servidor.

**P: Posso personalizar os campos do orçamento?**
R: A versão atual oferece campos padrão que atendem à maioria das necessidades. Personalizações específicas podem ser implementadas mediante solicitação.

**P: Há limite para o número de itens em um orçamento?**
R: Não há limite técnico para o número de itens em um orçamento. A plataforma foi testada com orçamentos contendo centenas de itens sem problemas de performance.

**P: Como posso obter suporte técnico?**
R: Para suporte técnico, entre em contato com o administrador do sistema ou com a equipe de TI da sua organização. Para problemas técnicos complexos, pode ser necessário contatar o desenvolvedor da plataforma.

---

**Conclusão**

A Calculadora de Orçamentos SaaS representa uma solução completa e moderna para gestão de orçamentos comerciais. Com sua interface intuitiva, funcionalidades robustas e arquitetura escalável, a plataforma oferece todas as ferramentas necessárias para otimizar o processo de criação e gestão de orçamentos.

Este guia fornece uma base sólida para utilização efetiva da plataforma, mas lembre-se de que a melhor forma de aprender é através da prática. Explore as funcionalidades, experimente diferentes cenários e não hesite em entrar em contato com o suporte quando necessário.

A plataforma está em constante evolução, com novas funcionalidades sendo adicionadas regularmente baseadas no feedback dos usuários e nas necessidades do mercado. Mantenha-se atualizado com as novidades e aproveite ao máximo todas as capacidades que a ferramenta oferece.

---

*Este guia foi elaborado pela equipe Manus AI e está sujeito a atualizações conforme a evolução da plataforma.*

