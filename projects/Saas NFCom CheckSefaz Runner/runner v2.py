import requests
from colorama import Fore, Style, init

init(autoreset=True)

API_KEY = "44d3e21f4a3341c7bdd6272847a52ee9"
BASE_URL = "https://saas.inventti.app/nfcom/api/v1/documentosfiscais/"

headers = {
    "x-api-key": API_KEY
}

with open("ids.txt", "r") as file:
    ids = [line.strip() for line in file if line.strip()]

total = len(ids)

responses_file = open("responses.txt", "w", encoding="utf-8")

for i, doc_id in enumerate(ids, start=1):

    url = f"{BASE_URL}{doc_id}"

    try:
        response = requests.get(url, headers=headers)

        linha_progresso = f"[{i}/{total}] ID {doc_id} -> Status {response.status_code}"

        if response.status_code == 200:
            print(Fore.GREEN + linha_progresso)
        else:
            print(Fore.RED + linha_progresso)

        responses_file.write(f"ID: {doc_id}\n")
        responses_file.write(f"Status: {response.status_code}\n")
        responses_file.write(response.text + "\n")
        responses_file.write("\n-----------------------------\n\n")

    except Exception as e:
        erro = f"[{i}/{total}] ID {doc_id} -> ERROR {str(e)}"
        print(Fore.RED + erro)

        responses_file.write(f"ID: {doc_id}\n")
        responses_file.write(f"ERROR: {str(e)}\n")
        responses_file.write("\n-----------------------------\n\n")

responses_file.close()

print(Style.BRIGHT + "\nProcessamento finalizado. Respostas salvas em responses.txt")