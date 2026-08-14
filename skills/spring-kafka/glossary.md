# Glossário Spring Kafka

- **`KafkaTemplate`**: abstração Spring para produzir mensagens Kafka.
- **`@KafkaListener`**: anotação para métodos consumidores.
- **Listener Container**: componente que gerencia consumers, threads, poll e lifecycle.
- **AckMode**: política de commit de offset.
- **Retryable Topics**: padrão de retries não bloqueantes por tópicos intermediários.
- **DLT**: dead-letter topic.
- **`KafkaTransactionManager`**: transações Kafka integradas ao Spring.
- **Message Converter**: conversão entre records Kafka e payloads Spring.
- **Embedded Kafka**: broker de teste fornecido por `spring-kafka-test`.
