import pandas as pd
import requests
import json
import time
from datetime import datetime

API_URL = "https://edp.inventti.app/nf3e/api/v1/documentos-fiscais/eventos-fiscais/emitir"
API_KEY = "44d3e21f4a3341c7bdd6272847a52ee9"

CNPJ_FIXO = "02302100000106"

HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

ARQUIVOS = [
    "Doc estornado. aprovado no monitor.xlsx"
]

COL_CHAVE = "Chave"
LOG_FILE = "runner_log.txt"

def log(msg):
    print(msg)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

log(f"\n=== INÍCIO EXECUÇÃO {datetime.now()} ===")

total = sucesso = falha = 0

for arquivo in ARQUIVOS:
    log(f"\n--- Processando arquivo: {arquivo} ---")

    df = pd.read_excel(arquivo)

    if COL_CHAVE not in df.columns:
        log(f"[ERRO] Coluna '{COL_CHAVE}' não encontrada no arquivo")
        continue

    for idx, row in df.iterrows():
        total += 1
        chave = str(row[COL_CHAVE]).strip()

        if not chave or chave.lower() == "nan":
            log(f"[IGNORADO] Linha {idx + 1} sem chave")
            continue

        payload = {
            "infEvento": {
                "cnpj": CNPJ_FIXO,
                "chNf3e": chave,
                "tpEvento": 110111,
                "xJust": "Cancelamento homologado"
            }
        }

        try:
            response = requests.post(
                API_URL,
                headers=HEADERS,
                data=json.dumps(payload),
                timeout=30
            )

            if response.status_code == 200:
                sucesso += 1
                log(f"[200 OK] Linha {idx + 1} | Chave {chave}")
            else:
                falha += 1
                log(
                    f"[FALHA] Linha {idx + 1} | "
                    f"Status {response.status_code} | "
                    f"Chave {chave} | "
                    f"Resposta: {response.text}"
                )

        except Exception as e:
            falha += 1
            log(f"[ERRO EXCEÇÃO] Linha {idx + 1} | Chave {chave} | {e}")

        time.sleep(0.3)

log("\n=== RESUMO FINAL ===")
log(f"Total processados: {total}")
log(f"Sucesso (200): {sucesso}")
log(f"Falha: {falha}")
log(f"Fim execução: {datetime.now()}")
log("\n=== FIM ===")
