# Git Workflow

Guia simples de fluxo de trabalho usando Git para projetos individuais ou em equipe.

---

## Estrutura de Branches

Modelo comum:

```
main
develop
feature/*
hotfix/*
```

### main

Branch de produção. Apenas código estável.

### develop

Branch de integração das features antes de ir para produção.

### feature/*

Branch usada para desenvolvimento de funcionalidades.

Exemplo:

```
feature/login
feature/user-api
feature/payment-integration
```

### hotfix/*

Correções urgentes em produção.

```
hotfix/login-error
```

---

## Criar uma Feature

Atualize a branch develop:

```bash
git checkout develop
git pull origin develop
```

Criar nova branch:

```bash
git checkout -b feature/nome-da-feature
```

---

## Commits

Boas práticas:

```
feat: adiciona endpoint de usuários
fix: corrige validação de email
refactor: melhora estrutura do service
docs: adiciona documentação
```

Exemplo:

```bash
git commit -m "feat: adiciona endpoint de criação de usuário"
```

---

## Subir branch

```bash
git push origin feature/nome-da-feature
```

---

## Pull Request

1. Abrir PR para `develop`
2. Revisar código
3. Aprovar
4. Merge

---

## Atualizar sua branch

Evita conflitos grandes.

```bash
git checkout develop
git pull origin develop
git checkout feature/minha-feature
git merge develop
```

---

## Resolver conflitos

Arquivos em conflito aparecem assim:

```
<<<<<<< HEAD
codigo atual
=======
codigo da outra branch
>>>>>>> develop
```

Escolha a versão correta e depois:

```bash
git add .
git commit
```

---

## Deploy

Fluxo típico:

```
feature -> develop -> main
```

Deploy sempre a partir da `main`.

---

## Boas práticas

* commits pequenos
* nomes claros de branch
* PRs pequenos
* revisão de código obrigatória
* nunca trabalhar direto na main
