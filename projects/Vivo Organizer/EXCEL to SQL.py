linhas = open("lista.txt").read().splitlines()

values = []

for linha in linhas:
    partes = linha.split(",")
    serie = partes[-3]
    nnf = partes[-2]
    cnpj = partes[-1]
    values.append(f"({serie},{nnf},'{cnpj}')")

sql = f"""
SELECT df.*
FROM documento_fiscal df
JOIN (
VALUES
{",\n".join(values)}
) v(serie, nnf, empresa_cnpj)
ON df.serie = v.serie
AND df.nnf = v.nnf
AND df.empresa_cnpj = v.empresa_cnpj;
"""

open("consulta.sql","w").write(sql)