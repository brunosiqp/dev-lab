import pyodbc

conn = pyodbc.connect(
    DRIVER={ODBC Driver 17 for SQL Server};
    SERVER=SEU_SERVIDOR;
    DATABASE=SEU_BANCO;
    UID=USUARIO;
    PWD=SENHA
)

cursor = conn.cursor()

try
    print(Buscando duplicados...)

    cursor.execute(
        SELECT ID
        FROM (
            SELECT 
                IC.ID,
                ROW_NUMBER() OVER (
                    PARTITION BY ICX.A_ID 
                    ORDER BY IC.ID
                ) AS rn
            FROM INTERF_CTE IC
            INNER JOIN INTERF_CTE_XML ICX 
                ON ICX.INTERF_CTE_FK = IC.ID
            WHERE IC.IND_STATUS = 2
        ) t
        WHERE rn  1
    )

    ids = [row.ID for row in cursor.fetchall()]

    if not ids
        print(Nenhum duplicado encontrado.)
        conn.close()
        exit()

    print(fDuplicados encontrados {len(ids)})

    ids_str = ,.join(map(str, ids))

    print(Iniciando limpeza...)

    cursor.execute(BEGIN TRAN)

    # exemplo de delete
    cursor.execute(f
        DELETE FROM rejeicao_cte
        WHERE interf_cte_fk IN ({ids_str})
    )

    cursor.execute(f
        DELETE FROM INTERF_CTE
        WHERE ID IN ({ids_str})
    )

    cursor.execute(COMMIT)

    print(Limpeza concluída com sucesso.)

except Exception as e
    print(Erro, e)
    cursor.execute(ROLLBACK)

finally
    conn.close()