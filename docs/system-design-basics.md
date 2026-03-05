# System Design Basics

Introduction to designing scalable software systems.

---

## What is System Design

System design focuses on how components interact to build scalable and reliable applications.

Key topics:

* scalability
* availability
* performance
* reliability

---

## Vertical Scaling

Increasing resources of a single server.

Example:

```
4GB RAM -> 32GB RAM
```

Limitations:

* hardware limits
* expensive
* single point of failure

---

## Horizontal Scaling

Adding more servers.

Example:

```
Server 1
Server 2
Server 3
```

Traffic is distributed between servers.

---

## Load Balancer

Distributes traffic across multiple servers.

Example flow:

```
Client
   |
Load Balancer
  /     \
Server1 Server2
```

Benefits:

* high availability
* better performance
* fault tolerance

---

## Caching

Stores frequently accessed data in memory.

Example technologies:

* Redis
* Memcached

Example flow:

```
Client -> Cache -> Database
```

If data is in cache, database is not queried.

---

## Database Scaling

Two common strategies:

### Read Replicas

One primary database with multiple replicas.

```
Primary DB
  /   |   \
Replica Replica Replica
```

---

### Sharding

Data split across multiple databases.

Example:

```
Users 1-1M -> DB1
Users 1M-2M -> DB2
```

---

## Message Queues

Used for asynchronous processing.

Examples:

* RabbitMQ
* Kafka
* SQS

Example:

```
API -> Queue -> Worker
```

---

## Microservices

Application split into independent services.

Example:

```
Auth Service
Order Service
Payment Service
```

Benefits:

* independent scaling
* team autonomy

Tradeoffs:

* complexity
* network latency
* distributed systems challenges
