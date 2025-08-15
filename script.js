// Configurações da calculadora
const CONFIG = {
    // Preços de mão de obra por localização
    maoDeObra: {
        mogi: {
            valorMinimo: 200, // até 1m²
            valorMetroLinear: 200 // acima de 1m²
        },
        'capital-sp': {
            valorMinimo: 280, // até 1m²
            valorMetroLinear: 200 // acima de 1m²
        }
    },
    
    // URL da API (será configurada dinamicamente)
    apiUrl: 'http://localhost:5000/api'
};

// Estado da aplicação
let state = {
    materiais: [],
    precosPorM2: {},
    totalMaterial: 0,
    totalMaoDeObra: 0,
    totalGeral: 0,
    areaTotal: 0
};

// Inicialização da aplicação
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    setupEventListeners();
    loadMaterialPrices();
    setupFormValidation();
}

function setupEventListeners() {
    // Event listeners para checkboxes de material
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', handleMaterialSelection);
    });

    // Event listeners para campos de medidas
    const measurementInputs = document.querySelectorAll('.measurements input');
    measurementInputs.forEach(input => {
        input.addEventListener('input', calculateArea);
    });

    // Event listener para o botão de calcular
    const calculateBtn = document.getElementById('calculate-btn');
    calculateBtn.addEventListener('click', calculateTotal);

    // Event listener para mudança de localização
    const localSelect = document.getElementById('local-mao-de-obra');
    localSelect.addEventListener('change', calculateTotal);

    // Máscara para CPF/CNPJ
    const cpfCnpjInput = document.getElementById('cpf-cnpj');
    cpfCnpjInput.addEventListener('input', applyCpfCnpjMask);

    // Máscara para CEP
    const cepInput = document.getElementById('cep');
    cepInput.addEventListener('input', applyCepMask);

    // Máscara para celular
    const celularInput = document.getElementById('celular');
    celularInput.addEventListener('input', applyCelularMask);
}

function handleMaterialSelection(event) {
    const checkbox = event.target;
    const materialItem = checkbox.closest('.material-item');
    const measurements = materialItem.querySelector('.measurements');
    
    if (checkbox.checked) {
        measurements.style.display = 'grid';
        measurements.classList.add('show');
        materialItem.classList.add('selected');
        
        // Adicionar ao estado
        const materialId = checkbox.id;
        if (!state.materiais.find(m => m.id === materialId)) {
            state.materiais.push({
                id: materialId,
                nome: checkbox.nextElementSibling.textContent,
                area: 0,
                preco: 0
            });
        }
    } else {
        measurements.style.display = 'none';
        measurements.classList.remove('show');
        materialItem.classList.remove('selected');
        
        // Remover do estado
        const materialId = checkbox.id;
        state.materiais = state.materiais.filter(m => m.id !== materialId);
        
        // Limpar campos de medida
        const inputs = measurements.querySelectorAll('input');
        inputs.forEach(input => input.value = '');
        
        // Limpar display de área
        const areaDisplay = measurements.querySelector('.area-display');
        areaDisplay.textContent = '0 m²';
    }
    
    calculateTotal();
}

function calculateArea(event) {
    const input = event.target;
    const measurements = input.closest('.measurements');
    const materialItem = measurements.closest('.material-item');
    const checkbox = materialItem.querySelector('input[type="checkbox"]');
    
    if (!checkbox.checked) return;
    
    const largura = parseFloat(measurements.querySelector('.largura').value) || 0;
    const comprimento = parseFloat(measurements.querySelector('.comprimento').value) || 0;
    const altura = parseFloat(measurements.querySelector('.altura').value) || 0;
    
    // Calcular área em m² (convertendo de cm para m)
    let area = 0;
    if (largura > 0 && comprimento > 0) {
        area = (largura * comprimento) / 10000; // cm² para m²
    }
    
    // Para alguns itens, pode ser necessário considerar a altura
    const materialId = checkbox.id;
    if (['fechamento-lateral', 'divisoria', 'painel-parede'].includes(materialId)) {
        if (largura > 0 && altura > 0) {
            area = (largura * altura) / 10000;
        }
    }
    
    // Atualizar display
    const areaDisplay = measurements.querySelector('.area-display');
    areaDisplay.textContent = `${area.toFixed(2)} m²`;
    
    // Atualizar estado
    const material = state.materiais.find(m => m.id === materialId);
    if (material) {
        material.area = area;
    }
    
    calculateTotal();
}

async function loadMaterialPrices() {
    try {
        // Simular preços por m² (em produção, viria da API Monday.com)
        state.precosPorM2 = {
            'bancada': 350,
            'fechamento-lateral': 280,
            'frontao': 320,
            'saia': 250,
            'rodabase': 180,
            'tabeira': 200,
            'baguete': 150,
            'soleira': 220,
            'pingadeira': 190,
            'virada': 300,
            'borda-piscina': 400,
            'divisoria': 350,
            'escada-pisada': 380,
            'escada-espelho': 320,
            'lavatorio-esculpido': 800,
            'lavatorio-cuba': 450,
            'mesa': 500,
            'painel': 380,
            'painel-parede': 350,
            'patamar': 400,
            'peitoril': 250,
            'rodape': 120
        };
        
        console.log('Preços carregados:', state.precosPorM2);
    } catch (error) {
        console.error('Erro ao carregar preços:', error);
        showNotification('Erro ao carregar preços. Usando valores padrão.', 'warning');
    }
}

function calculateTotal() {
    // Calcular total de material
    state.totalMaterial = 0;
    state.areaTotal = 0;
    
    state.materiais.forEach(material => {
        const precoM2 = state.precosPorM2[material.id] || 0;
        material.preco = material.area * precoM2;
        state.totalMaterial += material.preco;
        state.areaTotal += material.area;
    });
    
    // Calcular mão de obra
    const local = document.getElementById('local-mao-de-obra').value;
    const configMaoDeObra = CONFIG.maoDeObra[local];
    
    if (state.areaTotal <= 1) {
        state.totalMaoDeObra = configMaoDeObra.valorMinimo;
    } else {
        state.totalMaoDeObra = state.areaTotal * configMaoDeObra.valorMetroLinear;
    }
    
    // Total geral
    state.totalGeral = state.totalMaterial + state.totalMaoDeObra;
    
    // Atualizar display
    updateTotalDisplay();
}

function updateTotalDisplay() {
    const totalPriceElement = document.getElementById('total-price');
    totalPriceElement.textContent = formatCurrency(state.totalGeral);
    
    // Adicionar animação
    totalPriceElement.style.transform = 'scale(1.1)';
    setTimeout(() => {
        totalPriceElement.style.transform = 'scale(1)';
    }, 200);
}

function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}

// Máscaras de input
function applyCpfCnpjMask(event) {
    let value = event.target.value.replace(/\D/g, '');
    
    if (value.length <= 11) {
        // CPF: 000.000.000-00
        value = value.replace(/(\d{3})(\d)/, '$1.$2');
        value = value.replace(/(\d{3})(\d)/, '$1.$2');
        value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
    } else {
        // CNPJ: 00.000.000/0000-00
        value = value.replace(/^(\d{2})(\d)/, '$1.$2');
        value = value.replace(/^(\d{2})\.(\d{3})(\d)/, '$1.$2.$3');
        value = value.replace(/\.(\d{3})(\d)/, '.$1/$2');
        value = value.replace(/(\d{4})(\d)/, '$1-$2');
    }
    
    event.target.value = value;
}

function applyCepMask(event) {
    let value = event.target.value.replace(/\D/g, '');
    value = value.replace(/^(\d{5})(\d)/, '$1-$2');
    event.target.value = value;
}

function applyCelularMask(event) {
    let value = event.target.value.replace(/\D/g, '');
    value = value.replace(/^(\d{2})(\d)/, '($1) $2');
    value = value.replace(/(\d{5})(\d)/, '$1-$2');
    event.target.value = value;
}

// Validação de formulário
function setupFormValidation() {
    const requiredFields = document.querySelectorAll('input[required]');
    
    requiredFields.forEach(field => {
        field.addEventListener('blur', validateField);
        field.addEventListener('input', clearFieldError);
    });
}

function validateField(event) {
    const field = event.target;
    const value = field.value.trim();
    
    if (!value) {
        showFieldError(field, 'Este campo é obrigatório');
        return false;
    }
    
    // Validações específicas
    switch (field.type) {
        case 'email':
            if (!isValidEmail(value)) {
                showFieldError(field, 'Email inválido');
                return false;
            }
            break;
        case 'tel':
            if (value.length < 14) {
                showFieldError(field, 'Celular inválido');
                return false;
            }
            break;
    }
    
    clearFieldError(field);
    return true;
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function showFieldError(field, message) {
    clearFieldError(field);
    
    field.style.borderColor = '#e74c3c';
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'field-error';
    errorDiv.style.color = '#e74c3c';
    errorDiv.style.fontSize = '0.8rem';
    errorDiv.style.marginTop = '0.25rem';
    errorDiv.textContent = message;
    
    field.parentNode.appendChild(errorDiv);
}

function clearFieldError(field) {
    const errorDiv = field.parentNode.querySelector('.field-error');
    if (errorDiv) {
        errorDiv.remove();
    }
    field.style.borderColor = '';
}

// Notificações
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        color: white;
        font-weight: 500;
        z-index: 1000;
        animation: slideIn 0.3s ease-out;
    `;
    
    switch (type) {
        case 'success':
            notification.style.background = '#27ae60';
            break;
        case 'warning':
            notification.style.background = '#f39c12';
            break;
        case 'error':
            notification.style.background = '#e74c3c';
            break;
        default:
            notification.style.background = '#3498db';
    }
    
    notification.textContent = message;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease-out';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Função para gerar orçamento (futura integração)
function generateQuote() {
    const clientData = getClientData();
    const materialData = state.materiais.filter(m => m.area > 0);
    const local = document.getElementById('local-mao-de-obra').value;
    
    const quote = {
        cliente: clientData,
        materiais: materialData,
        localInstalacao: local,
        valores: {
            material: state.totalMaterial,
            maoDeObra: state.totalMaoDeObra,
            total: state.totalGeral
        },
        areaTotal: state.areaTotal,
        dataOrcamento: new Date().toISOString()
    };
    
    console.log('Orçamento gerado:', quote);
    return quote;
}

function getClientData() {
    return {
        nome: document.getElementById('nome').value,
        celular: document.getElementById('celular').value,
        email: document.getElementById('email').value,
        cpfCnpj: document.getElementById('cpf-cnpj').value,
        endereco: document.getElementById('endereco').value,
        cep: document.getElementById('cep').value
    };
}

// Adicionar estilos para animações
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    #total-price {
        transition: transform 0.2s ease;
    }
`;
document.head.appendChild(style);

// Função para integração futura com Monday.com
async function fetchMondayPrices() {
    try {
        const response = await fetch(`${CONFIG.apiUrl}/materials/prices`);
        if (!response.ok) {
            throw new Error('Erro ao buscar preços');
        }
        
        const prices = await response.json();
        state.precosPorM2 = prices;
        
        showNotification('Preços atualizados com sucesso!', 'success');
        calculateTotal();
    } catch (error) {
        console.error('Erro ao buscar preços do Monday.com:', error);
        showNotification('Erro ao atualizar preços. Usando valores em cache.', 'warning');
    }
}

// Função para salvar orçamento (futura integração)
async function saveQuote() {
    try {
        const quote = generateQuote();
        
        const response = await fetch(`${CONFIG.apiUrl}/quotes`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(quote)
        });
        
        if (!response.ok) {
            throw new Error('Erro ao salvar orçamento');
        }
        
        const result = await response.json();
        showNotification('Orçamento salvo com sucesso!', 'success');
        return result;
    } catch (error) {
        console.error('Erro ao salvar orçamento:', error);
        showNotification('Erro ao salvar orçamento', 'error');
        throw error;
    }
}

// Exportar funções para uso global
window.calculadoraDCoratto = {
    generateQuote,
    saveQuote,
    fetchMondayPrices,
    state
};

