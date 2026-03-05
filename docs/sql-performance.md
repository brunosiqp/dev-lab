# SQL Performance

Guia rápido para melhorar performance de consultas SQL.

Compatível com MySQL, PostgreSQL, SQL Server e Oracle.

---

## Usar índices

Sem índice:

```sql
SELECT *
FROM users
WHERE email = '[email protected]'
```

Criar índice:

```sql
CREATE INDEX idx_users_email
ON users(email);
```

---

## Evitar SELECT *

Ruim:

```sql
SELECT *
FROM orders
```

Melhor:

```sql
SELECT id, total, created_at
FROM orders
```

Reduz uso de memória e tráfego.

---

## Usar LIMIT

Evita trazer milhares de registros.

```sql
SELECT *
FROM logs
ORDER BY created_at DESC
LIMIT 100
```

---

## Evitar funções em colunas indexadas

Ruim:

```sql
SELECT *
FROM users
WHERE LOWER(email) = '[email protected]'
```

Melhor:

```sql
SELECT *
FROM users
WHERE email = '[email protected]'
```

Funções impedem uso do índice.

---

## Analisar plano de execução

MySQL / PostgreSQL:

```sql
EXPLAIN
SELECT *
FROM orders
WHERE user_id = 10;
```

SQL Server:

```sql
SET SHOWPLAN_ALL ON
```

Isso mostra:

* uso de índice
* full table scan
* custo da query

---

## Evitar JOINs desnecessários

Ruim:

```sql
SELECT *
FROM orders o
JOIN users u ON u.id = o.user_id
```

Se não usa dados do usuário, não faça join.

---

## Índices compostos

Úteis quando filtrando múltiplas colunas.

```sql
CREATE INDEX idx_orders_user_date
ON orders(user_id, created_at);
```

Consulta:

```sql
SELECT *
FROM orders
WHERE user_id = 10
AND created_at > '2025-01-01'
```

---

## Paginação eficiente

Ruim:

```sql
SELECT *
FROM products
LIMIT 1000 OFFSET 10000
```

Melhor:

```sql
SELECT *
FROM products
WHERE id > 10000
LIMIT 100
```

---

## Monitoramento

Ferramentas úteis:

* slow query log
* pg_stat_statements
* SQL Server Profiler
* AWR (Oracle)

---

## Checklist de performance

Antes de otimizar:

* existe índice?
* query usa índice?
* SELECT *?
* JOIN desnecessário?
* paginação correta?
* volume de dados muito grande?
