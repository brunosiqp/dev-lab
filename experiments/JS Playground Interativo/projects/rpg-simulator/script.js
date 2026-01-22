const player1Select = document.getElementById('player1');
const player2Select = document.getElementById('player2');
const startBattleBtn = document.getElementById('startBattle');
const battleLog = document.getElementById('battleLog');

let characters = [];

// Carrega os personagens do JSON
fetch('characters.json')
    .then(res => res.json())
    .then(data => {
        characters = data;
        populateSelectors();
    });

function populateSelectors() {
    characters.forEach(char => {
        const option1 = document.createElement('option');
        option1.value = char.name;
        option1.textContent = char.name;
        player1Select.appendChild(option1);

        const option2 = document.createElement('option');
        option2.value = char.name;
        option2.textContent = char.name;
        player2Select.appendChild(option2);
    });
}

// Função de ataque
function attack(attacker, defender) {
    const damage = Math.max(attacker.atk - defender.def, 0);
    defender.hp -= damage;
    return `${attacker.name} hits ${defender.name} for ${damage} damage. (${defender.hp} HP left)`;
}

// Função de batalha
function battle(player1, player2) {
    let log = '';
    let p1 = { ...player1 };
    let p2 = { ...player2 };

    let turn = 1;
    while (p1.hp > 0 && p2.hp > 0) {
        log += `Turn ${turn}:\n`;
        log += attack(p1, p2) + '\n';
        if (p2.hp <= 0) {
            log += `${p2.name} is defeated! ${p1.name} wins!\n`;
            break;
        }
        log += attack(p2, p1) + '\n';
        if (p1.hp <= 0) {
            log += `${p1.name} is defeated! ${p2.name} wins!\n`;
            break;
        }
        log += '\n';
        turn++;
    }
    battleLog.textContent = log;
}

// Evento do botão
startBattleBtn.addEventListener('click', () => {
    const p1Name = player1Select.value;
    const p2Name = player2Select.value;

    if (p1Name === p2Name) {
        alert("Choose different characters, guri!");
        return;
    }

    const p1 = characters.find(c => c.name === p1Name);
    const p2 = characters.find(c => c.name === p2Name);

    battle(p1, p2);
});
