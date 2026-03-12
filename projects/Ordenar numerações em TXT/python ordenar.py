# Abrir o arquivo original e ler os IDs
with open("ordenar.txt", "r") as f:
    ids = [int(line.strip()) for line in f if line.strip()]

# Ordenar os IDs
ids.sort()

# Salvar em um novo arquivo
with open("ordenados.txt", "w") as f:
    for i in ids:
        f.write(str(i) + "\n")

print("IDs ordenados com sucesso!")
