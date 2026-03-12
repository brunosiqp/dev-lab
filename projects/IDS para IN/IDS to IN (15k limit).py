entrada = "ids.txt"
tamanho_bloco = 15000

# Lê os IDs do arquivo
with open(entrada, "r") as f:
    ids = [linha.strip() for linha in f if linha.strip()]

# Divide em blocos
for i in range(0, len(ids), tamanho_bloco):
    bloco = ids[i:i + tamanho_bloco]
    numero_arquivo = (i // tamanho_bloco) + 1
    nome_saida = f"in{numero_arquivo}.txt"

    # Formata o bloco com ()
    conteudo = "(" + ", ".join(bloco) + ")"

    # Escreve o arquivo
    with open(nome_saida, "w") as f:
        f.write(conteudo)

    print(f"Gerado: {nome_saida}")

print("Finalizado, guri. Aulas demais.")
