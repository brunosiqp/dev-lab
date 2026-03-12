entrada = "ids.txt"      # teu arquivo de origem
saida = "in.txt"         # arquivo gerado

with open(entrada, "r") as f:
    nums = [linha.strip() for linha in f if linha.strip()]

resultado = "(" + ", ".join(nums) + ")"

with open(saida, "w") as f:
    f.write(resultado)

print("Arquivo gerado:", saida)
