// Aguarda o carregamento completo do HTML para iniciar o script
document.addEventListener('DOMContentLoaded', initializeApp);

// --- CONFIGURAÇÕES GLOBAIS ---
const CONFIG = {
    maoDeObra: {
        mogi: { valorMinimo: 200, valorMetroLinear: 200 },
        'capital-sp': { valorMinimo: 280, valorMetroLinear: 200 }
    },
    // A URL da API agora é relativa, o Vercel saberá para onde direcionar.
    apiUrl: '/api' 
};

// --- ESTADO DA APLICAÇÃO ---
// Centraliza todos os dados dinâmicos da calculadora
let state = {
    materiaisSelecionados: [],
    precosPorM2: {},
    areaTotal: 0,
    custoTotal: 0
};

/**
 * Função principal que inicializa a aplicação
 */
function initializeApp() {
    setupEventListeners();
    loadMaterialPrices();
    // Não é mais necessário validar o formulário de cliente aqui,
    // pois ele não faz parte do cálculo inicial.
}

/**
 * Configura todos os "ouvintes" de eventos da página
 */
function setupEventListeners() {
    // Delegação de eventos para os itens de material para melhor performance
    const materialItemsContainer = document.getElementById('material-items');
    materialItemsContainer.addEventListener('change', handleMaterialChange);
    materialItemsContainer.addEventListener('input', handleMeasurementChange);

    document.getElementById('local-mao-de-obra').addEventListener('change', calculateTotal);
    document.getElementById('calculate-btn').addEventListener('click', handleQuoteGeneration);

    // Máscaras para os campos de input
    document.getElementById('cpf-cnpj').addEventListener('input', applyMask(maskCpfCnpj));
    document.getElementById('cep').addEventListener('input', applyMask(maskCep));
    document.getElementById('celular').addEventListener('input', applyMask(maskCelular));
}

/**
 * Lida com a seleção (checkbox) de um material
 * @param {Event} event - O evento de 'change'
 */
function handleMaterialChange(event) {
    if (event.target.type !== 'checkbox') return;

    const checkbox = event.target;
    const materialItem = checkbox.closest('.material-item');
    const measurementsDiv = materialItem.querySelector('.measurements');
    const materialId = checkbox.id;

    if (checkbox.checked) {
        measurementsDiv.style.display = 'grid';
        materialItem.classList.add('selected');
        // Adiciona material ao estado se não existir
        if (!state.materiaisSelecionados.find(m => m.id === materialId)) {
            state.materiaisSelecionados.push({
                id: materialId,
                nome: checkbox.nextElementSibling.textContent.trim(),
                area: 0
            });
        }
    } else {
        measurementsDiv.style.display = 'none';
        materialItem.classList.remove('selected');
        // Remove material do estado
        state.materiaisSelecionados = state.materiaisSelecionados.filter(m => m.id !== materialId);
        // Limpa campos de medida e área
        measurementsDiv.querySelectorAll('input').forEach(input => input.value = '');
        measurementsDiv.querySelector('.area-display').textContent = '0 m²';
    }
    calculateTotal();
}

/**
 * Lida com a alteração nos campos de medida (largura, comprimento, etc.)
 * @param {Event} event - O evento de 'input'
 */
function handleMeasurementChange(event) {
    if (event.target.type !== 'number') return;
    calculateArea(event.target);
    calculateTotal();
}

/**
 * Calcula a área de um item específico
 * @param {HTMLElement} inputElement - O campo de input que foi alterado
 */
function calculateArea(inputElement) {
    const measurementsDiv = inputElement.closest('.measurements');
    const materialId = measurementsDiv.closest('.material-item').querySelector('input[type="checkbox"]').id;
    
    const largura = parseFloat(measurementsDiv.querySelector('.largura')?.value) || 0;
    const comprimento = parseFloat(measurementsDiv.querySelector('.comprimento')?.value) || 0;
    
    const area = (largura * comprimento) / 10000; // cm² para m²
    
    measurementsDiv.querySelector('.area-display').textContent = `${area.toFixed(3)} m²`;

    const material = state.materiaisSelecionados.find(m => m.id === materialId);
    if (material) {
        material.area = area;
    }
}

/**
 * Carrega os preços dos materiais (simulado, idealmente viria da API)
 */
async function loadMaterialPrices() {
    // Em um cenário real, isso faria uma chamada à API:
    // const prices = await fetch(`${CONFIG.apiUrl}/materials/prices`).then(res => res.json());
    // state.precosPorM2 = prices;
    
    // Usando dados simulados por enquanto:
    state.precosPorM2 = {
        'bancada': 350, 'fechamento-lateral': 280, 'frontao': 320, 'saia': 250,
        'rodabase': 180, 'tabeira': 200, 'baguete': 150, 'soleira': 220,
        'pingadeira': 190, 'virada': 300, 'borda-piscina': 400, 'divisoria': 350,
        'escada-pisada': 380, 'escada-espelho': 320, 'lavatorio-esculpido': 800,
        'lavatorio-cuba': 450, 'mesa': 500, 'painel': 380, 'painel-parede': 350,
        'patamar': 400, 'peitoril': 250, 'rodape': 120
    };
    console.log('Preços dos materiais carregados.');
}

/**
 * Calcula o custo total do orçamento e atualiza a tela
 */
function calculateTotal() {
    const custoMaterial = state.materiaisSelecionados.reduce((total, material) => {
        const precoM2 = state.precosPorM2[material.id] || 0;
        return total + (material.area * precoM2);
    }, 0);

    state.areaTotal = state.materiaisSelecionados.reduce((total, material) => total + material.area, 0);

    const local = document.getElementById('local-mao-de-obra').value;
    const configMaoDeObra = CONFIG.maoDeObra[local];
    let custoMaoDeObra = 0;
    if (state.areaTotal > 0) {
        custoMaoDeObra = state.areaTotal <= 1 ? configMaoDeObra.valorMinimo : state.areaTotal * configMaoDeObra.valorMetroLinear;
    }
    
    state.custoTotal = custoMaterial + custoMaoDeObra;
    
    updateTotalDisplay(state.custoTotal);
}

/**
 * Atualiza o elemento de preço total na tela
 * @param {number} total - O valor total a ser exibido
 */
function updateTotalDisplay(total) {
    const totalPriceElement = document.getElementById('total-price');
    totalPriceElement.textContent = formatCurrency(total);
}

/**
 * Formata um número para o padrão de moeda brasileiro (BRL)
 * @param {number} value - O número a ser formatado
 * @returns {string} - O valor formatado como moeda
 */
function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value || 0);
}

// --- MÁSCARAS DE INPUT ---
const applyMask = (maskFn) => (event) => {
    event.target.value = maskFn(event.target.value);
};

const maskCpfCnpj = (value) => {
    value = value.replace(/\D/g, '');
    if (value.length <= 11) {
        return value
            .replace(/(\d{3})(\d)/, '$1.$2')
            .replace(/(\d{3})(\d)/, '$1.$2')
            .replace(/(\d{3})(\d{1,2})$/, '$1-$2');
    }
    return value.slice(0, 14)
        .replace(/^(\d{2})(\d)/, '$1.$2')
        .replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3')
        .replace(/\.(\d{3})(\d)/, '.$1/$2')
        .replace(/(\d{4})(\d)/, '$1-$2');
};

const maskCep = (value) => value.replace(/\D/g, '').replace(/^(\d{5})(\d)/, '$1-$2').slice(0, 9);
const maskCelular = (value) => value.replace(/\D/g, '').replace(/^(\d{2})(\d)/, '($1) $2').replace(/(\d{5})(\d)/, '$1-$2').slice(0, 15);


// --- VALIDAÇÃO E GERAÇÃO DO ORÇAMENTO ---

/**
 * Valida o formulário de cliente
 * @returns {boolean} - True se o formulário for válido, false caso contrário
 */
function validateClientForm() {
    const form = document.getElementById('client-form');
    if (!form.checkValidity()) {
        // O navegador mostrará as mensagens de erro padrão para campos 'required'
        form.reportValidity();
        return false;
    }
    return true;
}

/**
 * Lida com o clique no botão "Calcular Orçamento", que agora salva o orçamento
 */
async function handleQuoteGeneration() {
    if (!validateClientForm()) {
        showNotification('Por favor, preencha todos os dados do cliente.', 'warning');
        return;
    }
    if (state.materiaisSelecionados.length === 0 || state.areaTotal === 0) {
        showNotification('Selecione ao menos um material e preencha as medidas.', 'warning');
        return;
    }

    const quoteData = {
        client_data: {
            name: document.getElementById('nome').value,
            phone: document.getElementById('celular').value,
            email: document.getElementById('email').value,
            document: document.getElementById('cpf-cnpj').value,
            address: document.getElementById('endereco').value,
            zip_code: document.getElementById('cep').value
        },
        items: state.materiaisSelecionados.map(m => ({ name: m.nome, area: m.area })),
        labor_location: document.getElementById('local-mao-de-obra').value,
        total_price: state.custoTotal
    };

    try {
        showLoading(true);
        const response = await fetch(`${CONFIG.apiUrl}/budgets`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(quoteData)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || 'Erro ao salvar orçamento.');
        }

        const result = await response.json();
        showNotification('Orçamento salvo com sucesso!', 'success');
        console.log('Orçamento salvo:', result);

    } catch (error) {
        showNotification(error.message, 'error');
        console.error('Falha ao salvar orçamento:', error);
    } finally {
        showLoading(false);
    }
}

// --- FUNÇÕES UTILITÁRIAS ---

function showLoading(isLoading) {
    document.body.classList.toggle('loading', isLoading);
    document.getElementById('calculate-btn').disabled = isLoading;
}

function showNotification(message, type = 'info') {
    // Remove qualquer notificação existente
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }

    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);

    setTimeout(() => {
        notification.classList.add('fade-out');
        notification.addEventListener('transitionend', () => notification.remove());
    }, 3000);
}

// Adiciona os estilos da notificação dinamicamente para não poluir o CSS
const notificationStyle = `
    .notification {
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        color: white;
        font-weight: 500;
        z-index: 1000;
        transition: opacity 0.5s, transform 0.5s;
        transform: translateX(0);
        opacity: 1;
    }
    .notification.notification-info { background: #3498db; }
    .notification.notification-success { background: #27ae60; }
    .notification.notification-warning { background: #f39c12; }
    .notification.notification-error { background: #e74c3c; }
    .notification.fade-out {
        opacity: 0;
        transform: translateX(20px);
    }
    body.loading { opacity: 0.8; pointer-events: none; }
`;
const styleSheet = document.createElement("style");
styleSheet.innerText = notificationStyle;
document.head.appendChild(styleSheet);
