# Patterns e anti-patterns — Networking

## Patterns

### Connection-stage diagnosis
Diagnostique por estágio: DNS -> route -> connect -> TLS -> protocol -> application. Evita atribuir todo timeout à aplicação.

### Timeout budget
Defina budgets separados para connect, handshake, request/read e idle. O timeout externo deve ser maior que a soma razoável dos estágios internos, sem criar caudas intermináveis.

### Connection reuse
Prefira pooling/keep-alive quando o protocolo e intermediários suportarem. Reduz handshake, TLS e consumo de portas efêmeras.

### Evidence-first troubleshooting
Colete evidência do estágio: resolução, rota, socket, TLS, status/proxy headers e métricas antes de alterar configuração.

### Symmetric-path awareness
Considere rota de retorno, NAT, firewall stateful e assimetria. Reachability de ida não garante resposta correta.

### Layered observability
Tenha sinais de DNS failures, connect latency/errors, TLS handshake, pool saturation, HTTP upstream status e proxy/LB metrics.

## Anti-patterns

- aumentar timeout sem identificar o estágio;
- retry em múltiplas camadas sem budget coordenado;
- usar ping como prova definitiva de conectividade de aplicação;
- atribuir 502/503 automaticamente ao serviço final;
- recriar conexão por request sem necessidade;
- pool sem limite e fila sem limite;
- introduzir service mesh como correção genérica;
- confundir mTLS com autorização de negócio;
- ignorar DNS caching/TTL em mudanças de endpoint;
- investigar apenas a rota de ida.
