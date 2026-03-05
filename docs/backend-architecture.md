# Backend Architecture

Overview of common backend architecture patterns.

---

## Layered Architecture

A common backend structure separates responsibilities into layers.

Example:

```
Controller
Service
Repository
Database
```

---

## Controller Layer

Handles HTTP requests.

Example:

```javascript
app.get("/users", async (req, res) => {
  const users = await userService.getUsers()
  res.json(users)
})
```

Responsibilities:

* request validation
* calling services
* formatting responses

---

## Service Layer

Contains business logic.

Example:

```javascript
class UserService {
  async getUsers() {
    return userRepository.findAll()
  }
}
```

Responsibilities:

* application rules
* data processing
* orchestration

---

## Repository Layer

Responsible for database access.

Example:

```javascript
class UserRepository {
  async findAll() {
    return db.query("SELECT * FROM users")
  }
}
```

Responsibilities:

* database queries
* data persistence
* mapping records

---

## Benefits

Layered architecture improves:

* maintainability
* testability
* scalability

---

## Example Structure

```
src/
  controllers/
  services/
  repositories/
  models/
  routes/
```

---

## Dependency Flow

Dependencies should only flow downward.

```
Controller -> Service -> Repository
```

Avoid:

```
Repository -> Controller
```

---

## Testing Strategy

Each layer can be tested separately:

* controller tests
* service tests
* repository tests
