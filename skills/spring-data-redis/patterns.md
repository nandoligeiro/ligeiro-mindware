# Padrões e Anti-Padrões Spring Data Redis

## Padrões

- **Cache Aside com TTL**: busque fonte de verdade quando cache miss; escreva no Redis com TTL.
- **Explicit Serialization Contract**: configure serializers como parte da arquitetura.
- **StringRedisTemplate for Simple Keys**: reduza complexidade para strings/counters/flags.
- **RedisTemplate Gateway**: encapsule operações Redis em adapter/serviço, não espalhe comandos.
- **Streams for Durable Async Work**: prefira Streams a Pub/Sub quando precisa histórico e ack.
- **Lua for Atomic Multi-Key Logic**: use script quando precisa atomicidade além de comando simples.
- **Observability on Cache and Streams**: monitore hit/miss, latência, pending entries, erros e timeouts.

## Anti-Padrões

- **Redis as Accidental Primary DB**: dados críticos só no Redis sem durabilidade/backup/modelo.
- **No TTL Cache**: cache eterno vira dado obsoleto.
- **JDK Serialization by Accident**: payload opaco, frágil e ruim para interoperabilidade.
- **Pub/Sub as Queue Durable**: mensagens somem para consumidores offline.
- **Distributed Lock Naive**: lock sem timeout, fencing token ou lib robusta.
- **KEYS in Production**: comandos globais bloqueantes em dataset grande.
- **Reactive Costume**: API reativa sobre fluxo de aplicação blocking.
