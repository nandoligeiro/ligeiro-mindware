# Glossário Spring Data Redis

- **RedisTemplate**: API de alto nível para operações Redis com serialização configurável.
- **StringRedisTemplate**: template otimizado para chaves/valores string.
- **RedisConnectionFactory**: fábrica de conexões Redis.
- **Lettuce**: driver Redis assíncrono/reactive baseado em Netty.
- **Jedis**: driver Redis tradicional.
- **Serializer**: componente que converte objetos Java para bytes/strings Redis.
- **Keyspace**: namespace lógico de chaves para repositories.
- **TTL**: tempo de vida de uma chave.
- **Redis Repository**: repository Spring Data mapeado para estruturas Redis.
- **Pub/Sub**: mensagens efêmeras por canal.
- **Redis Streams**: log de mensagens com IDs, consumer groups e ack.
- **Pipelining**: envio de múltiplos comandos reduzindo round-trips.
- **Transaction**: execução agrupada com MULTI/EXEC.
- **Lua Script**: script executado no Redis para lógica atômica.
- **Sentinel**: monitoramento/failover Redis.
- **Cluster**: particionamento/sharding Redis.
