---
name: spring-data
description: "Cocérebro baseado na documentação oficial Spring Data 2026.0.x: repositories, query methods, object mapping, projections, auditing, custom repositories, entity callbacks, Spring Data Commons, JPA, JDBC/R2DBC, MongoDB, Redis/Data REST visão geral, release trains e escolha de módulo por datastore."
metadata:
  short-description: Spring Data operacional
---

# Spring Data — Ligeiro Mindware

Use esta skill para escolher e aplicar Spring Data em persistência relacional, reativa e NoSQL.

## Fontes Oficiais

- `https://spring.io/projects/spring-data/`
- `https://docs.spring.io/spring-data/commons/reference/`
- `https://docs.spring.io/spring-data/jpa/reference/`
- `https://docs.spring.io/spring-data/mongodb/reference/`
- `https://docs.spring.io/spring-data/redis/reference/`

## Como Pensar

Spring Data fornece um modelo familiar de repositórios, query derivation, mapeamento, auditoria e extensões por datastore, preservando características do banco subjacente.

## Carregue Sob Demanda

- Commons, repositories e queries: `chapters/commons-repositories.md`
- JPA, JDBC/R2DBC e transações: `chapters/relational.md`
- MongoDB/NoSQL, auditing e projections: `chapters/nosql-mapping.md`
- Redis, cache e estruturas chave-valor: `chapters/redis-overview.md`
- Decisões rápidas: `cheatsheet.md`
- Padrões e anti-padrões: `patterns.md`
- Termos: `glossary.md`

## Diagnóstico Inicial

1. Qual datastore: JPA, JDBC, R2DBC, Mongo, Redis, Cassandra etc.?
2. Acesso é blocking ou reactive?
3. Repositório derivado basta ou precisa query customizada?
4. O modelo é agregado rico ou CRUD simples?
5. Transação existe e é local/distribuída?
6. Precisa auditing, projections, pagination, scrolling ou events?
7. Query method está claro ou virando linguagem secreta?
8. Redis será cache, key-value store, pub/sub, streams, rate limit ou lock?

## Regras Práticas

- Repositories reduzem boilerplate; não substituem modelagem.
- Query derivation é ótima até ficar ilegível.
- Custom repository é melhor que método monstruoso.
- JPA não é JDBC; Mongo não é JPA; preserve semântica do datastore.
- Redis não é só cache; escolha explicitamente entre template, cache abstraction, repositories, pub/sub ou streams.
- Reactive repository só faz sentido com stack e driver reativos.
- Auditing exige modelo de ownership/tempo claro.
