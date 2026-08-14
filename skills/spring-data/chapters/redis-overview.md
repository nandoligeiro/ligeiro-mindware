# Redis no Spring Data

## Fonte

- `https://docs.spring.io/spring-data/redis/reference/`

## Quando Usar

Spring Data Redis fornece acesso a Redis por templates, cache abstraction, repositories, pub/sub, streams, scripting, transactions, pipelining e APIs reativas via Lettuce.

Escolha Redis para:

- cache;
- dados efêmeros com TTL;
- counters;
- rate limiting;
- distributed locks com cuidado;
- pub/sub simples;
- streams;
- key-value de baixa latência.

## Abstrações

- `RedisTemplate`: operações gerais com serializers configuráveis.
- `StringRedisTemplate`: strings como caso comum.
- Redis Cache: integração com cache abstraction do Spring.
- Redis Repositories: mapeamento de objetos para hashes.
- Reactive Redis: acesso non-blocking com Lettuce.

## Cuidados

- Serializer é parte do contrato de dados.
- TTL precisa ser explícito para dados efêmeros.
- Cache precisa estratégia de invalidação.
- Pub/sub não é fila durável.
- Streams são mais adequados para consumo com histórico.
- Redis Cluster/Sentinel mudam conexão, roteamento e operação.
