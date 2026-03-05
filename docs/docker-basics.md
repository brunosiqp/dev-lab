# Docker Basics

Quick guide to working with Docker for development environments.

---

## What is Docker

Docker allows applications to run inside isolated environments called containers.

Benefits:

* consistent environments
* easy dependency management
* reproducible builds
* simpler deployments

---

## Basic Concepts

### Image

A template used to create containers.

Example:

```bash
docker pull node:20
```

---

### Container

A running instance of an image.

```bash
docker run node:20
```

---

### Dockerfile

File that defines how an image is built.

Example:

```dockerfile
FROM node:20

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

CMD ["node", "index.js"]
```

---

## Building an Image

```bash
docker build -t my-app .
```

---

## Running a Container

```bash
docker run -p 3000:3000 my-app
```

This maps:

```
container port 3000 -> host port 3000
```

---

## Running in Background

```bash
docker run -d my-app
```

---

## Listing Containers

```bash
docker ps
```

All containers:

```bash
docker ps -a
```

---

## Stopping a Container

```bash
docker stop CONTAINER_ID
```

---

## Removing Containers

```bash
docker rm CONTAINER_ID
```

---

## Removing Images

```bash
docker rmi IMAGE_ID
```

---

## Docker Compose

Used for running multiple services.

Example:

```yaml
version: "3"

services:
  api:
    build: .
    ports:
      - "3000:3000"

  database:
    image: postgres
    ports:
      - "5432:5432"
```

Start services:

```bash
docker compose up
```

---

## Best Practices

* keep images small
* use `.dockerignore`
* avoid running containers as root
* use multi-stage builds
