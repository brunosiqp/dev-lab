import requests
import time
import urllib3
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from tqdm import tqdm

# desliga warning de SSL inseguro
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY = "77f84e5f5594415b8cb6c6fc4507e165"
BASE_URL = "https://shein.inventti.app/cte2/api/v2/documentos-fiscais/reprocessar/{}"
ARQUIVO_CHAVES = "chaves.txt"
MAX_THREADS = 10
DELAY_ENTRE_REQUISICOES = 0.0
LOG_FILE = "resultado.log"

lock = Lock()

# 🎨 cores ANSI
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
RESET = "\033[0m"


def carregar_chaves(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        return [linha.strip() for linha in f if linha.strip()]


def logar(msg):
    with lock:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(msg + "\n")


def processar_chave(chave):
    url = BASE_URL.format(chave)
    headers = {"X-API-Key": API_KEY}

    try:
        response = requests.post(
            url,
            headers=headers,
            timeout=30,
            verify=False
        )
        return chave, response.status_code, None
    except Exception as e:
        return chave, None, str(e)
    finally:
        if DELAY_ENTRE_REQUISICOES > 0:
            time.sleep(DELAY_ENTRE_REQUISICOES)


def cor_por_status(status, erro):
    if erro:
        return VERMELHO
    if status is None:
        return VERMELHO
    if 200 <= status < 300:
        return VERDE
    if status >= 500:
        return VERMELHO
    return AMARELO  # ex: 4xx


def main():
    chaves = carregar_chaves(ARQUIVO_CHAVES)
    total = len(chaves)

    print(f"{AMARELO}Total de chaves: {total}{RESET}")
    print(f"{AMARELO}Threads: {MAX_THREADS}{RESET}")

    # limpa log antigo
    open(LOG_FILE, "w").close()

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(processar_chave, c) for c in chaves]

        for future in tqdm(as_completed(futures), total=total, desc="Processando"):
            chave, status, erro = future.result()

            if erro:
                msg = f"ERRO | {chave} | {erro}"
            else:
                msg = f"OK | {chave} | Status {status}"

            cor = cor_por_status(status, erro)
            print(f"{cor}{msg}{RESET}")
            logar(msg)

    print(f"\n{VERDE}Processamento finalizado.{RESET}")


if __name__ == "__main__":
    main()