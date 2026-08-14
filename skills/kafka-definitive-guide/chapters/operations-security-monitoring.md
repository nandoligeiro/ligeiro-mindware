# Operação, Segurança e Monitoramento

## Capítulos Cobertos

- Cap. 11 — Securing Kafka
- Cap. 12 — Administering Kafka
- Cap. 13 — Monitoring Kafka

## Segurança

Kafka precisa garantir:

- autenticidade de cliente;
- autenticidade de servidor;
- privacidade;
- integridade;
- autorização;
- auditabilidade;
- disponibilidade.

Ferramentas:

- TLS/SSL;
- SASL;
- ACLs;
- segurança do ZooKeeper/KRaft/control plane;
- restrição de ferramentas administrativas.

## Administração

Operações comuns:

- criar/descrever/deletar topics;
- adicionar partitions;
- alterar configs;
- reassignment de partitions;
- leader election;
- consumer group inspection;
- ACL management.

Governança importa: topic naming, ownership, schema, retention e quotas evitam entropia.

## Monitoramento Essencial

Monitore sempre:

- broker up/down;
- offline partitions;
- under-replicated partitions;
- active controller count;
- request latency;
- network/disk usage;
- ISR shrink/expand;
- consumer lag;
- disk fill/retention;
- produce/fetch rates.

## Alertas

Alertas devem ser acionáveis:

- offline partitions: crítico;
- under-replicated partitions persistente: crítico/alto;
- consumer lag crescendo e violando SLA: alto;
- disco perto do limite: alto;
- controller changes frequentes: investigar;
- request latency alta: investigar por tipo.

## Debug Operacional

Quando Kafka parece lento:

1. Verifique broker e partitions offline/under-replicated.
2. Compare produce/fetch request latency.
3. Olhe disco e rede.
4. Olhe ISR e leader distribution.
5. Analise consumer lag por group/partition.
6. Verifique rebalances e tempo de processamento.
7. Relacione com deploys, reassignment, compactação ou tráfego.
