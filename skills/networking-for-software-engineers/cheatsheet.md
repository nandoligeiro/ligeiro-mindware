# Networking cheatsheet

## Primeiras perguntas

1. Quem inicia a conexão?
2. Qual hostname/IP e porta?
3. Onde estão source e destination?
4. O DNS resolve para o endpoint esperado?
5. Há rota de ida e volta?
6. O connect falha, recusa ou demora?
7. O TLS completa? Qual erro exato?
8. Há proxy/LB/ingress/mesh/NAT no caminho?
9. Quais timeouts existem em cada camada?
10. O pool está saturado ou há churn de conexões?

## Sintoma -> suspeitas

| Sintoma | Investigue primeiro |
| --- | --- |
| DNS failure | resolver, zone, TTL/cache, split DNS |
| connection refused | listener/porta/endereço errado |
| connect timeout | route, firewall, blackhole, capacity |
| TLS hostname error | SAN/SNI/hostname usado |
| cert expired/untrusted | chain, truststore, rotação |
| 502 | proxy/gateway + upstream reachability |
| 503 | capacidade, health, routing, admission |
| 504 | timeout do intermediário/upstream |
| pool timeout | pool size, hold time, leak, downstream latency |
| resets intermitentes | peer, LB/proxy idle timeout, connection reuse |

## Regra prática de retry

Antes de retry, determine se a operação é segura/idempotente e coordene tentativas entre cliente, proxy e serviço. Networking explica a falha; `distributed-systems-engineering` deve orientar semântica de retry e efeitos duplicados.
