# Spring Kafka Cheatsheet

| Necessidade | Use |
|---|---|
| Enviar mensagem | `KafkaTemplate` |
| Consumir como método POJO | `@KafkaListener` |
| Controlar consumo | Listener container/container factory |
| Commit manual | Ack modes e `Acknowledgment` |
| Retry blocking | Error handler/backoff |
| Retry non-blocking | Retryable Topics |
| Dead letter | DLT/DLPR |
| Transação Kafka | `KafkaTransactionManager` |
| Teste integrado | `spring-kafka-test` / embedded Kafka |
| Streams | suporte Kafka Streams via Spring |

## Checklist de Listener

- `groupId` definido?
- concurrency compatível com partitions?
- erro tratado?
- DLT monitorada?
- payload validado?
- headers importantes preservados?
- commits alinhados à garantia?

## Checklist de Producer

- tópico e key corretos?
- serializer/converter compatível?
- callback/resultado tratado?
- retries/idempotência configurados?
- headers de correlação/trace incluídos?
