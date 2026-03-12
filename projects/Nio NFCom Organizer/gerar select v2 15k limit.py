import pandas as pd
import re
import math

ARQUIVO = "dados.xlsx"
LIMITE = 15000

df = pd.read_excel(ARQUIVO)

def limpar_cnpj(cnpj):
    return re.sub(r"\D", "", str(cnpj))

valores = []

for _, row in df.iterrows():
    cnpj = limpar_cnpj(row["CNPJ EMISSOR"])
    nnf = int(row["NUM_NF"])
    serie = int(row["SÉRIE"])

    valores.append(f"({serie},{nnf},'{cnpj}')")

total_blocos = math.ceil(len(valores) / LIMITE)

for i in range(total_blocos):
    inicio = i * LIMITE
    fim = inicio + LIMITE
    bloco = valores[inicio:fim]

    values_sql = ",\n".join(bloco)

    query = f"""
SELECT df.*
FROM documento_fiscal df
JOIN (
VALUES
{values_sql}
) v(serie, nnf, empresa_cnpj)
ON df.serie = v.serie
AND df.nnf = v.nnf
AND df.empresa_cnpj = v.empresa_cnpj;
"""

    nome_arquivo = f"select_{i+1}.sql"

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(query)

    print(f"Gerado {nome_arquivo} com {len(bloco)} registros")