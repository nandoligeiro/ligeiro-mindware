# Reliability, Transactions e Retries

## Offset e Garantias

Commit de offset é a fronteira de progresso do consumer group. Alinhe commit ao efeito real do processamento.

## Retries

Use retries para falhas transitórias. Para falhas permanentes, mande para DLT ou trate explicitamente.

## Retryable Topics

Retries não bloqueantes usam tópicos intermediários para não prender a partition principal.

`@RetryableTopic` é a forma declarativa de configurar esse padrão em listeners. Use quando a falha é provavelmente transitória e o delay desejado é longo o suficiente para tornar ruim bloquear o consumer thread/container.

Decisões importantes:

- `attempts`: quantas tentativas totais fazem sentido antes de DLT.
- `backoff`: delay fixo, exponencial ou política customizada.
- inclusões/exclusões de exceções: retry só para erro transitório.
- DLT strategy: quem consome, alerta, reprocessa ou descarta.
- topic naming: nomes previsíveis para retry topics e DLT.
- ordering: mensagens atrasadas podem quebrar expectativa operacional de ordem entre eventos relacionados.

Use blocking retry curto para falhas muito rápidas e `@RetryableTopic` para espera longa. Evite retryar validação, schema inválido, payload irrecuperável ou erro de regra permanente.

## Transactions

Use `KafkaTransactionManager` para agrupar operações Kafka. O caso clássico é consume-process-produce com exactly-once semantics dentro do Kafka.
