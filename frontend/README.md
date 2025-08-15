# Calculadora D'Coratto - Frontend

Esta é a interface frontend da calculadora inteligente para marmorarias D'Coratto.

## Arquivos Incluídos

- `index.html` - Página principal com formulário de cliente e calculadora
- `style.css` - Estilos responsivos e design profissional
- `script.js` - Lógica JavaScript para cálculos e interações
- `assets/images/Logo-02.jpg` - Logotipo da D'Coratto

## Funcionalidades

### 1. Dados do Cliente
- Nome, celular, email, CPF/CNPJ
- Endereço completo com CEP
- Máscaras automáticas para formatação

### 2. Calculadora de Materiais
- 22 tipos de materiais disponíveis
- Campos para medidas em centímetros
- Cálculo automático de área em m²
- Preços por m² configuráveis

### 3. Cálculo de Mão de Obra
- **Mogi das Cruzes**: R$ 200 fixo até 1m², R$ 200/m² acima
- **Capital SP**: R$ 280 fixo até 1m², R$ 200/m² acima

### 4. Recursos Visuais
- Design responsivo para desktop e mobile
- Animações e transições suaves
- Feedback visual em tempo real
- Logotipo da empresa integrado

## Como Usar

1. **Preencher dados do cliente** na primeira seção
2. **Selecionar local da mão de obra** (Mogi das Cruzes ou Capital SP)
3. **Marcar os itens de material** desejados
4. **Inserir medidas** em centímetros nos campos que aparecem
5. **Clicar em "Calcular Orçamento"** para ver o valor total

## Integração com Backend

O frontend está preparado para integração com a API backend:

- Função `fetchMondayPrices()` para buscar preços do Monday.com
- Função `saveQuote()` para salvar orçamentos
- Configuração de API em `CONFIG.apiUrl`

## Preços Padrão (por m²)

- Bancada: R$ 350
- Fechamento lateral: R$ 280
- Frontão: R$ 320
- Saia: R$ 250
- Rodabase: R$ 180
- Tabeira: R$ 200
- Baguete: R$ 150
- Soleira: R$ 220
- Pingadeira: R$ 190
- Virada: R$ 300
- Borda de Piscina: R$ 400
- Divisória: R$ 350
- Escada Pisada: R$ 380
- Escada Espelho: R$ 320
- Lavatório Esculpido: R$ 800
- Lavatório com Cuba: R$ 450
- Mesa: R$ 500
- Painel: R$ 380
- Painel de Parede: R$ 350
- Patamar: R$ 400
- Peitoril: R$ 250
- Rodapé: R$ 120

## Próximos Passos

1. Integrar com API do Monday.com para preços em tempo real
2. Implementar salvamento de orçamentos
3. Adicionar geração de PDF dos orçamentos
4. Configurar deploy no Vercel

## Tecnologias Utilizadas

- HTML5 semântico
- CSS3 com Flexbox e Grid
- JavaScript ES6+
- Design responsivo
- Animações CSS

## Suporte

Para dúvidas ou suporte, entre em contato com a equipe de desenvolvimento.

