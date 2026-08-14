---
name: spring-data-redis
description: "Cocérebro baseado na documentação oficial Spring Data Redis 4.1.x: RedisTemplate, StringRedisTemplate, serializers, Redis Cache, Redis Repositories, TTL, keyspaces, secondary indexes, Lettuce/Jedis, Sentinel, Cluster, Pub/Sub, Redis Streams, scripting, transactions, pipelining, reactive Redis, observability e padrões como cache, rate limiting e locks."
metadata:
  short-description: Spring Data Redis operacional
---

# Spring Data Redis — Ligeiro Mindware

Use esta skill para projetar, implementar e debugar uso de Redis em aplicações Spring.

## Fontes Oficiais

- `https://spring.io/projects/spring-data-redis/`
- `https://docs.spring.io/spring-data/redis/reference/`

## Como Pensar

Spring Data Redis fornece abstrações de baixo e alto nível sobre Redis: conexão/driver, templates, serializers, cache abstraction, repositories, pub/sub, streams, transactions, pipelining e APIs reativas.

Redis não é “só cache”. Decida o papel exato antes de escolher abstração.

## Carregue Sob Demanda

- Templates, serializers e cache: `chapters/templates-cache.md`
- Repositories, TTL e mapping: `chapters/repositories-ttl.md`
- Pub/Sub, Streams, scripting e pipelining: `chapters/messaging-streams-pipelines.md`
- Cluster, reactive, observability e operação: `chapters/operations-reactive.md`
- Decisões rápidas: `cheatsheet.md`
- Padrões e anti-padrões: `patterns.md`
- Termos: `glossary.md`

## Diagnóstico Inicial

1. Redis será cache, store, counter, lock, rate limiter, pub/sub ou stream?
2. Dados podem expirar? Qual TTL?
3. Qual serializer é contrato: String, JSON, JDK, custom?
4. Precisa reativo? Está usando Lettuce?
5. Precisa Redis Cluster ou Sentinel?
6. A operação precisa atomicidade, transaction, Lua script ou pipeline?
7. Pub/Sub precisa durabilidade? Se sim, considere Redis Streams.
8. Cache precisa invalidação, key naming, TTL e métricas?

## Regras Práticas

- Escolha serializer explicitamente; não deixe virar acidente histórico.
- Use `StringRedisTemplate` para strings simples.
- Use `RedisTemplate` quando precisa tipos/serialização customizados.
- Use cache abstraction quando a intenção é cache, não banco de dados.
- Use repositories Redis quando o modelo hash/keyspace encaixa.
- TTL é parte do modelo de dados.
- Pub/Sub não guarda mensagens para consumidor offline.
- Streams são melhores quando precisa histórico, grupos e ack.
- Pipelining melhora round-trips, mas muda ergonomia de erro/resultado.
- Locks distribuídos exigem muito cuidado; prefira soluções testadas e timeouts.
