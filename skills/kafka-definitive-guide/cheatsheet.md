# Kafka Cheatsheet

## Design de Tópicos

| Decisão | Pergunta |
|---|---|
| Nome do tópico | Qual domínio/evento/contrato ele representa? |
| Chave | Qual entidade precisa de ordering? |
| Partições | Qual paralelismo necessário agora e depois? |
| Replication factor | Qual durabilidade/disponibilidade exigida? |
| Retention | Quanto tempo precisa replay/reprocessamento? |
| Compaction | Preciso manter último valor por chave? |
| Schema | Como produtores e consumidores evoluem sem quebrar? |

## Producer

| Meta | Configurações/decisões |
|---|---|
| Durabilidade | `acks=all`, `retries`, idempotência, `min.insync.replicas` |
| Throughput | batching, compression, linger, buffer memory |
| Latência | reduzir batching/linger, monitorar request latency |
| Ordering | chave estável, cuidado com retries/in-flight |
| Duplicatas | idempotent producer |

## Consumer

| Meta | Configurações/decisões |
|---|---|
| Escala | partições >= consumidores ativos do group |
| Controle | commit manual quando processamento importa |
| Evitar perda | processe antes de commitar offset |
| Reduzir duplicata | idempotência no sink/processamento |
| Rebalance suave | cooperative rebalance, static membership |
| Lag | medir por group/topic/partition |

## Garantias

| Garantia | Como acontece | Risco |
|---|---|---|
| At-most-once | commit antes de processar | perda |
| At-least-once | processa antes de commit | duplicata |
| Idempotent produce | producer evita duplicata por retry | escopo limitado |
| Transactions/EOS | consume-process-produce transacional | complexidade e limites |

## Operação Essencial

- Under-replicated partitions devem ser zero.
- Offline partitions são emergência.
- ISR shrink/expand frequente indica instabilidade.
- Consumer lag precisa contexto: está crescendo, estável ou drenando?
- Disk usage e retention precisam alertas.
- Request latency por tipo ajuda a localizar gargalo.
- Controller changes frequentes são sinal ruim.

## Segurança

- TLS/SSL para criptografia e identidade de servidor.
- SASL para autenticação.
- ACLs para autorização.
- Proteja ZooKeeper/KRaft/control plane.
- Restrinja ferramentas administrativas.
- Audite alterações de tópico, ACL e configuração.
