# API Design

Best practices for designing REST APIs.

---

## Use Nouns for Resources

Bad:

```
/getUsers
/createUser
```

Good:

```
/users
/users/{id}
```

---

## HTTP Methods

Use HTTP verbs correctly.

| Method | Purpose         |
| ------ | --------------- |
| GET    | retrieve data   |
| POST   | create resource |
| PUT    | update resource |
| PATCH  | partial update  |
| DELETE | remove resource |

Example:

```
GET /users
POST /users
GET /users/10
DELETE /users/10
```

---

## Use Proper Status Codes

Common responses:

| Code | Meaning            |
| ---- | ------------------ |
| 200  | success            |
| 201  | resource created   |
| 400  | bad request        |
| 401  | unauthorized       |
| 404  | resource not found |
| 500  | server error       |

Example response:

```json
{
  "id": 10,
  "name": "John"
}
```

---

## Use Consistent Naming

Prefer plural resources:

```
/users
/orders
/products
```

Avoid mixing styles.

Bad:

```
/userList
/order_data
```

---

## Pagination

Avoid returning large datasets.

Example:

```
GET /users?page=1&limit=20
```

Response:

```json
{
  "page": 1,
  "limit": 20,
  "total": 200,
  "data": []
}
```

---

## Filtering

Example:

```
GET /orders?status=paid
```

---

## Versioning

APIs should be versioned.

Example:

```
/api/v1/users
/api/v2/users
```

---

## Error Responses

Return structured errors.

Example:

```json
{
  "error": "User not found"
}
```

---

## Security

Important points:

* authentication
* authorization
* rate limiting
* input validation
