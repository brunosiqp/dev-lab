# Debugging de APIs HTTP

Guia rápido para identificar problemas comuns ao consumir ou desenvolver APIs REST.

---

## 1. Conferir o Status Code

Os códigos HTTP já indicam a direção do problema.

| Code | Significado                   |
| ---- | ----------------------------- |
| 200  | Requisição OK                 |
| 400  | Erro na requisição do cliente |
| 401  | Falta autenticação            |
| 403  | Sem permissão                 |
| 404  | Endpoint não encontrado       |
| 500  | Erro interno do servidor      |

Exemplo de resposta:

```json
{
  "status": 404,
  "message": "Route not found"
}
```

---

## 2. Testar a API via cURL

Antes de culpar o código da aplicação, teste direto no terminal.

```bash
curl -X GET https://api.exemplo.com/users \
  -H "Authorization: Bearer TOKEN_AQUI" \
  -H "Content-Type: application/json"
```

POST com body:

```bash
curl -X POST https://api.exemplo.com/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Joao",
    "email": "[email protected]"
  }'
```

---

## 3. Log da Requisição

Sempre registre:

* URL
* método HTTP
* headers
* body enviado
* response

Exemplo em Node.js:

```javascript
async function request(url, options) {
  console.log("REQUEST:", url, options)

  const response = await fetch(url, options)
  const data = await response.json()

  console.log("RESPONSE:", response.status, data)

  return data
}
```

---

## 4. Verificar Headers

Problemas comuns:

```
Content-Type errado
Authorization ausente
Token expirado
CORS bloqueado
```

Exemplo correto:

```
Content-Type: application/json
Authorization: Bearer TOKEN
```

---

## 5. Validar JSON

Erro clássico: JSON mal formado.

Errado:

```json
{
  "name": "Joao",
  "age": 30,
}
```

Certo:

```json
{
  "name": "Joao",
  "age": 30
}
```

Ferramentas úteis:

* jsonlint.com
* jq

---

## 6. Usar ferramentas de teste

Ferramentas comuns:

* Postman
* Insomnia
* Bruno
* Thunder Client (VSCode)

---

## 7. Checklist rápido

Antes de perder horas debugando:

* endpoint correto
* método HTTP correto
* headers corretos
* body válido
* autenticação válida
* servidor rodando
* logs do backend

---

## Conclusão

Grande parte dos erros de API são causados por:

1. headers errados
2. token inválido
3. JSON mal formado
4. endpoint incorreto

Sempre comece testando a requisição isoladamente antes de depurar o código.
