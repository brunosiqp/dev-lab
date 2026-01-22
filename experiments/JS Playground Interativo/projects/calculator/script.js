// Pega todos os botões e o display
const display = document.getElementById('display');
const buttons = document.querySelectorAll('.btn');
const clearBtn = document.getElementById('clear');
const equalsBtn = document.getElementById('equals');

let currentInput = "";

// Função para atualizar o display
function updateDisplay() {
    display.value = currentInput || "0";
}

// Adiciona eventos a todos os botões
buttons.forEach(button => {
    button.addEventListener('click', () => {
        const value = button.getAttribute('data-value');

        // Evita adicionar dois operadores seguidos
        if (["+", "-", "*", "/"].includes(value) && ["+", "-", "*", "/"].includes(currentInput.slice(-1))) {
            return;
        }

        currentInput += value;
        updateDisplay();
    });
});

// Limpa o display
clearBtn.addEventListener('click', () => {
    currentInput = "";
    updateDisplay();
});

// Calcula o resultado
equalsBtn.addEventListener('click', () => {
    try {
        currentInput = eval(currentInput).toString();
        updateDisplay();
    } catch {
        display.value = "Erro";
        currentInput = "";
    }
});
