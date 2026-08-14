# Reliability, Transactions e Retries

## Offset e Garantias

Commit de offset é a fronteira de progresso do consumer group. Alinhe commit ao efeito real do processamento.

## Retries

Use retries para falhas transitórias. Para falhas permanentes, mande para DLT ou trate explicitamente.

## Retryable Topics

Retries não bloqueantes usam tópicos intermediários para não prender a partition principal.

## Transactions

Use `KafkaTransactionManager` para agrupar operações Kafka. O caso clássico é consume-process-produce com exactly-once semantics dentro do Kafka.
