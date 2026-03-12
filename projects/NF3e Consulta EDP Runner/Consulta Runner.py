import pandas as pd
import requests
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY = "44d3e21f4a3341c7bdd6272847a52ee9"
BASE_URL = "https://edp.inventti.app/nf3e/api/v1/documentos-fiscais"
OUTPUT_DIR = "responses"

os.makedirs(OUTPUT_DIR, exist_ok=True)

arquivos = [
    "Doc estornado. aprovado no monitor_v1.xlsx"
]

headers = {
    "x-api-key": API_KEY
}

session = requests.Session()
session.headers.update(headers)

for arquivo in arquivos:
    print(f"\nLendo arquivo: {arquivo}")

    df = pd.read_excel(arquivo)

    if "Chave" not in df.columns:
        print(f"❌ Coluna 'Chave' não encontrada em {arquivo}")
        continue

    chaves = df["Chave"].dropna().astype(str)

    for chave in chaves:
        chave = chave.strip()
        if not chave:
            continue

        url = f"{BASE_URL}/{chave}/consultar-sefaz"
        print(f"Consultando chave: {chave}")

        try:
            response = session.get(
                url,
                timeout=30,
                verify=False
            )

            with open(f"{OUTPUT_DIR}/{chave}.json", "w", encoding="utf-8") as f:
                f.write(response.text)

            if response.status_code != 200:
                print(
                    f"⚠️ Status {response.status_code} | "
                    f"Response: {response.text[:200]}"
                )

        except Exception as e:
            print(f"❌ Erro na chave {chave}: {e}")
