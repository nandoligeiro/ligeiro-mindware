# Templates, Serializers e Cache

## Templates

Use `StringRedisTemplate` para casos simples de string. Use `RedisTemplate` quando precisa controlar tipos e serializers.

Operações comuns:

- values;
- hashes;
- lists;
- sets;
- sorted sets;
- counters;
- expirations.

## Serializers

Serializer é contrato de compatibilidade. Decida entre String, JSON, JDK ou custom.

Cuidados:

- evolução de classes;
- interoperabilidade;
- legibilidade;
- tamanho;
- segurança;
- compatibilidade entre serviços.

## Cache

Redis Cache integra com a cache abstraction do Spring.

Defina:

- TTL por cache;
- key prefix;
- serializer;
- política de invalidação;
- tolerância a falhas;
- métricas.
