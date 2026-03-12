import pandas as pd
import re

ARQUIVO = "dados.xlsx"

df = pd.read_excel(ARQUIVO)

def limpar_cnpj(cnpj):
    return re.sub(r"\D", "", str(cnpj))

valores = []

for _, row in df.iterrows():
    cnpj = limpar_cnpj(row["CNPJ EMISSOR"])
    nnf = int(row["NUM_NF"])
    serie = int(row["SÉRIE"])

    valores.append(f"({serie},{nnf},'{cnpj}')")

values_sql = ",\n".join(valores)

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

with open("select.sql", "w", encoding="utf-8") as f:
    f.write(query)

print("SQL gerado em select.sql")