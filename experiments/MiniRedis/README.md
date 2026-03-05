# MiniRedis

A simplified distributed cache system inspired by Redis, built in **C++**.

Este projeto implementa um **servidor de cache em memória com comunicação TCP**, permitindo armazenar e recuperar dados usando comandos simples.

Ce projet implémente **un serveur de cache en mémoire avec communication TCP**, permettant de stocker et récupérer des données via des commandes simples.

---

# Overview

## English
MiniRedis is a lightweight key-value database server designed to demonstrate how in-memory caching systems like Redis work internally.

## Português
MiniRedis é um servidor de banco de dados key-value leve criado para demonstrar como sistemas de cache em memória como o Redis funcionam internamente.

## Français
MiniRedis est un serveur de base de données clé-valeur léger conçu pour démontrer le fonctionnement interne des systèmes de cache en mémoire comme Redis.

---

# Features

## English
- TCP server
- In-memory key-value store
- Basic command parser
- Redis-like commands
- Simple client interaction

## Português
- Servidor TCP
- Armazenamento key-value em memória
- Parser simples de comandos
- Comandos semelhantes ao Redis
- Interação simples com cliente

## Français
- Serveur TCP
- Stockage clé-valeur en mémoire
- Analyseur de commandes simple
- Commandes similaires à Redis
- Interaction simple avec client

---

# Supported Commands

| Command | Description |
|--------|------------|
| PING | Check server health |
| SET key value | Store a value |
| GET key | Retrieve a value |
| DEL key | Delete a key |

Example:

```
SET name John
GET name
DEL name
PING
```

---

# Project Structure

```
mini-redis/
│
├── CMakeLists.txt
├── README.md
│
├── src/
│   ├── main.cpp
│   │
│   ├── server/
│   │   ├── TcpServer.h
│   │   └── TcpServer.cpp
│   │
│   ├── store/
│   │   ├── KeyValueStore.h
│   │   └── KeyValueStore.cpp
│   │
│   ├── protocol/
│   │   ├── CommandParser.h
│   │   └── CommandParser.cpp
│   │
│   └── commands/
│       ├── CommandHandler.h
│       └── CommandHandler.cpp
│
└── client/
    └── test-client.py
```

---

# Architecture

## English

The system is composed of four main modules.

TCP Server  
Handles client connections and receives commands.

Command Parser  
Converts raw text input into structured command tokens.

Command Handler  
Executes commands and interacts with the data store.

KeyValue Store  
In-memory storage implemented using `unordered_map`.

---

## Português

O sistema é composto por quatro módulos principais.

Servidor TCP  
Responsável por receber conexões e comandos dos clientes.

Parser de Comandos  
Converte texto bruto recebido em tokens de comando estruturados.

Manipulador de Comandos  
Executa os comandos e interage com o armazenamento.

KeyValue Store  
Armazenamento em memória implementado com `unordered_map`.

---

## Français

Le système est composé de quatre modules principaux.

Serveur TCP  
Gère les connexions clients et reçoit les commandes.

Analyseur de commandes  
Transforme l'entrée texte en commandes structurées.

Gestionnaire de commandes  
Exécute les commandes et interagit avec le stockage.

KeyValue Store  
Stockage en mémoire implémenté avec `unordered_map`.

---

# How to Build

Requirements:

- C++17
- CMake
- Linux or macOS recommended

Build steps:

```
mkdir build
cd build
cmake ..
make
```

---

# Running the Server

```
./mini_redis
```

Server will start on:

```
localhost:6379
```

---

# Testing the Server

Run the test client:

```
python3 client/test-client.py
```

Example session:

```
mini-redis> SET name Alice
OK

mini-redis> GET name
Alice

mini-redis> DEL name
1

mini-redis> PING
PONG
```

---

# Future Improvements

## English
- Multithreading support
- Key expiration (TTL)
- Persistence to disk
- Redis RESP protocol
- LRU memory eviction
- Cluster support

## Português
- Suporte a multithreading
- Expiração de chaves (TTL)
- Persistência em disco
- Protocolo RESP do Redis
- Política de remoção LRU
- Suporte a cluster

## Français
- Multithreading
- Expiration des clés (TTL)
- Persistance sur disque
- Protocole RESP de Redis
- Politique d'éviction LRU
- Support de cluster

---

# Learning Goals

## English
This project demonstrates:

- TCP networking in C++
- Server architecture
- Command parsing
- Memory-based storage systems

## Português
Este projeto demonstra:

- Programação de rede em C++
- Arquitetura de servidores
- Parsing de comandos
- Sistemas de armazenamento em memória

## Français
Ce projet démontre :

- Programmation réseau en C++
- Architecture serveur
- Analyse de commandes
- Systèmes de stockage en mémoire

---

# License

MIT License