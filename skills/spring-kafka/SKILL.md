---
name: spring-kafka
description: "Cocérebro baseado na documentação oficial Spring for Apache Kafka 4.1.x: KafkaTemplate, @KafkaListener, listener containers, offset commits, transactions, exactly-once semantics, retries, retryable topics, DLT, serialization, message conversion, Kafka Streams support, testing com spring-kafka-test, monitoring e integração com Spring Boot."
metadata:
  short-description: Spring for Apache Kafka operacional
---

# Spring for Apache Kafka — Ligeiro Mindware

Use esta skill para projetar, implementar e debugar aplicações Spring que produzem, consomem e processam mensagens Kafka.

## Fontes Oficiais

- `https://spring.io/projects/spring-kafka/`
- `https://docs.spring.io/spring-kafka/reference/`

## Como Pensar

Spring Kafka aplica conceitos Spring ao Kafka: `KafkaTemplate` para envio, `@KafkaListener` para consumo orientado a POJO, listener containers para lifecycle/concurrency, `KafkaTransactionManager` para transações e recursos como `@RetryableTopic`/DLT para resiliência.

## Carregue Sob Demanda

- Producers, consumers e containers: `chapters/clients-listeners.md`
- Reliability, transactions e retries: `chapters/reliability-retries.md`
- Serialization, testing e observability: `chapters/testing-observability.md`
- Decisões rápidas: `cheatsheet.md`
- Padrões e anti-padrões: `patterns.md`
- Termos: `glossary.md`

## Diagnóstico Inicial

1. O app só produz, só consome ou consume-process-produce?
2. Qual garantia: at-least-once, idempotência, transação/EOS?
3. Offset commit é automático, manual ou transacional?
4. Erro deve bloquear, retryar, ir para DLT ou ser descartado?
5. Há ordering por chave/partition?
6. Serialização usa JSON, Avro, String, bytes ou converter customizado?
7. Está usando Spring Boot auto-config ou configuração manual?
8. O teste precisa de embedded Kafka?
9. Retry deve ser blocking no container ou non-blocking com `@RetryableTopic`?

## Regras Práticas

- Use `KafkaTemplate` para produzir; encapsule decisão de tópico/chave/headers.
- Use `@KafkaListener` para handlers claros, mas entenda o container por baixo.
- Use `@RetryableTopic` para retries não bloqueantes com tópicos intermediários e DLT.
- Commits manuais dão controle, mas exigem disciplina.
- Retries sem DLT podem travar consumo.
- DLT sem observabilidade vira cemitério silencioso.
- Transações Kafka ajudam em consume-process-produce, não magicamente em sistemas externos.
- Teste listener, serialização e erro com `spring-kafka-test`.
