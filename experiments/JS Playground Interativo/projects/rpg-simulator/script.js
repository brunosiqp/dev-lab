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

// Função de ataque normal
function attack(attacker, defender) {
    const crit = Math.random() < 0.2; // 20% chance de crítico
    let damage = Math.max(attacker.atk - defender.def, 0);
    if (crit) damage = Math.floor(damage * 1.5);

    defender.hp -= damage;
    return crit
        ? `${attacker.name} hits CRITICALLY ${defender.name} for ${damage} damage! (${defender.hp} HP left)`
        : `${attacker.name} hits ${defender.name} for ${damage} damage. (${defender.hp} HP left)`;
}

// Função para usar habilidades
function useSkill(user, skill, target) {
    let log = '';
    if (skill.damage) {
        target.hp -= skill.damage;
        log = `${user.name} uses ${skill.name} on ${target.name} for ${skill.damage} damage. (${target.hp} HP left)`;
    } else if (skill.heal) {
        user.hp += skill.heal;
        log = `${user.name} uses ${skill.name} and heals ${skill.heal} HP. (${user.hp} HP total)`;
    } else if (skill.defBoost) {
        user.def += skill.defBoost;
        log = `${user.name} uses ${skill.name} and increases defense by ${skill.defBoost} (current DEF: ${user.def})`;
    }
    return log;
}

// Decide aleatoriamente se usa ataque ou skill
function chooseAction(player, opponent) {
    const useSkillChance = 0.6; // 60% chance de usar skill
    if (player.skills.length > 0 && Math.random() < useSkillChance) {
        const skill = player.skills[Math.floor(Math.random() * player.skills.length)];
        return useSkill(player, skill, opponent);
    } else {
        return attack(player, opponent);
    }
}

// Função principal de batalha
function battle(player1, player2) {
    let log = '';
    let p1 = { ...player1 };
    let p2 = { ...player2 };

    let turn = 1;
    while (p1.hp > 0 && p2.hp > 0) {
        log += `Turn ${turn}:\n`;
        log += chooseAction(p1, p2) + '\n';
        if (p2.hp <= 0) {
            log += `${p2.name} is defeated! ${p1.name} wins!\n`;
            break;
        }
        log += chooseAction(p2, p1) + '\n';
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
