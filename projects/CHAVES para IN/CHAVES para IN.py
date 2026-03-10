entrada = "chaves.txt"
tamanho_bloco = 15000

# Lê os valores do arquivo
with open(entrada, "r") as f:
    valores = [linha.strip() for linha in f if linha.strip()]

# Divide em blocos
for i in range(0, len(valores), tamanho_bloco):
    bloco = valores[i:i + tamanho_bloco]
    numero_arquivo = (i // tamanho_bloco) + 1
    nome_saida = f"in{numero_arquivo}.txt"

    # Formata cada valor entre aspas simples
    bloco_formatado = [f"'{v}'" for v in bloco]

    # Monta o conteúdo
    conteudo = "(" + ", ".join(bloco_formatado) + ")"

    # Grava no arquivo
    with open(nome_saida, "w") as f:
        f.write(conteudo)

    print(f"Gerado: {nome_saida}")

print("Finalizado, guri. Chave virou SQL na marra.")
