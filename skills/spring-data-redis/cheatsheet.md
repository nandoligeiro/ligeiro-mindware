# Spring Data Redis Cheatsheet

| Necessidade | Use |
|---|---|
| Operações string simples | `StringRedisTemplate` |
| Operações gerais Redis | `RedisTemplate<K,V>` |
| Cache Spring | Redis Cache / cache abstraction |
| Objetos por hash/keyspace | Redis Repositories |
| Pub/sub fire-and-forget | Redis Pub/Sub |
| Stream com histórico/grupos | Redis Streams |
| Operações atômicas complexas | Lua scripting |
| Reduzir round-trips | Pipelining |
| Reativo/non-blocking | Reactive Redis + Lettuce |
| HA/failover | Sentinel |
| Sharding horizontal | Redis Cluster |

## Checklist de Cache

- TTL definido?
- key naming padronizado?
- serializer compatível entre versões?
- invalidação planejada?
- métricas de hit/miss?
- fallback quando Redis falha?

## Checklist de Repository

- keyspace definido?
- TTL por entidade?
- índices secundários necessários?
- queries compatíveis com Redis?
- tamanho/eviction aceitáveis?

## Checklist de Streams

- consumer group definido?
- ack/retry planejado?
- pending entries monitoradas?
- trimming/retention definido?
- idempotência no consumidor?
