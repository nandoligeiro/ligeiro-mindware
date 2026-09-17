---
name: networking-for-software-engineers
description: "Ligeiro Mindware para diagnosticar e projetar comunicação de rede em sistemas modernos: DNS, TCP, TLS, HTTP, proxies, load balancers, NAT, service discovery, timeouts, connection pools, keep-alive, mTLS, CIDR, routing, ingress/egress, service mesh e failure modes de conectividade. Use quando um problema de software depende explicitamente da camada de rede, do transporte ou da conectividade entre serviços, clusters, clouds ou datacenters."
metadata:
  short-description: Networking pragmático para engenheiros de software
---

# Networking for Software Engineers

Use esta skill quando o problema não puder ser explicado apenas pela aplicação e exigir raciocínio sobre **resolução, rota, transporte, sessão, TLS, proxy ou política de rede**.

## Não ativar

Não use como resposta principal para:

- sintaxe de cliente HTTP sem sintomas de rede;
- modelagem de domínio;
- desenho de retry/idempotência sem falha de conectividade;
- tuning JVM sem relação com sockets/connections;
- configuração específica de um produto de rede sem contexto arquitetural.

## Modelo operacional

Diagnostique a conexão como uma cadeia:

`name resolution -> route -> connect -> TLS -> protocol -> application -> response path`

Cada estágio pode falhar de forma diferente. Não trate “timeout” ou “connection refused” como categorias genéricas.

## Fluxo

1. Identifique source, destination e protocolo.
2. Determine a fronteira: processo, host, subnet/VPC/VNet, cluster, região, cloud ou datacenter.
3. Verifique resolução de nome e TTL/cache.
4. Verifique reachability e rota de ida/volta.
5. Classifique a falha de transporte: connect timeout, reset, refused, half-open, idle timeout.
6. Verifique TLS/mTLS: trust chain, hostname, SNI, expiry, protocol/cipher compatível.
7. Verifique intermediários: proxy, LB, ingress, gateway, service mesh, NAT.
8. Verifique pooling/keep-alive/concurrency e limites de portas/connections.
9. Explicite timeout por estágio: connect, TLS handshake, request, read, idle.
10. Defina observabilidade e evidência de sucesso.

## Heurísticas

### DNS
- falha de DNS e falha TCP são problemas diferentes;
- cache local pode manter endpoint antigo além do esperado;
- TTL baixo não garante atualização imediata em todos os clientes;
- split-horizon DNS exige clareza sobre origem da consulta.

### TCP
- `connection refused` normalmente significa que o destino foi alcançado, mas não há listener aceitando naquela combinação IP/porta;
- connect timeout aponta mais para reachability, firewall, route, blackhole ou saturação do caminho;
- reset pode vir do peer ou de um intermediário;
- retransmissão não deve ser confundida automaticamente com erro de aplicação.

### TLS/mTLS
- diferencie trust failure, hostname mismatch, expiry e authn mTLS;
- certificado válido não implica autorização da aplicação;
- mTLS autentica peers, mas não substitui policy de negócio.

### HTTP e proxies
- 5xx pode vir do upstream, gateway ou proxy; identifique a origem;
- timeout de LB e timeout da aplicação precisam ser coerentes;
- retries em proxy e cliente podem se multiplicar.

### Pools e keep-alive
- pool é budget, não cache infinito;
- fila de espera de conexão deve ser limitada;
- keep-alive agressivo pode colidir com idle timeout de intermediários;
- connection churn pode consumir ephemeral ports e aumentar handshake/TLS overhead.

### NAT e portas efêmeras
Considere exaustão quando houver muitas conexões outbound curtas atrás de poucos IPs/NATs. Reduza churn, reuse connections e dimensione a capacidade de egress.

### Service mesh
Use mesh para policy/telemetry/routing quando houver benefício claro. Não introduza mesh apenas para “resolver networking”; ele adiciona outro hop e novos failure modes.

## Evidência esperada

A resposta deve explicitar:

- source/destination;
- estágio da cadeia onde a falha ocorre;
- hipótese mais provável e alternativas;
- evidência necessária para confirmar/refutar;
- timeout/pool/route/policy relevantes;
- residual risk e observabilidade.

## Leituras internas

Consulte `patterns.md` e `cheatsheet.md`.
