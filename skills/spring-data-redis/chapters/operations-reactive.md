# Cluster, Reactive, Observability e Operação

## Drivers

Lettuce é a escolha comum para reactive/non-blocking e uso moderno. Jedis existe como alternativa.

## Sentinel e Cluster

- Sentinel: HA/failover.
- Cluster: sharding horizontal.

Esses modos afetam conexão, comandos multi-key, roteamento e operação.

## Reactive Redis

Use reactive Redis quando o caminho inteiro é reativo. Não resolve gargalo se o resto é blocking.

## Observability

Monitore:

- latência de comandos;
- timeouts;
- cache hit/miss;
- tamanho de chaves;
- memory/eviction;
- stream pending entries;
- erros de conexão;
- cluster/sentinel failover.
