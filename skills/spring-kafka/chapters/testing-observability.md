# Testing e Observability

## Testing

Use `spring-kafka-test` quando o comportamento depende de broker, listener container, serialização ou commits.

Teste:

- envio com `KafkaTemplate`;
- listener consumindo;
- erro e DLT;
- serialização/deserialização;
- transação/retry.

## Observability

Monitore:

- consumer lag;
- listener errors;
- DLT rate;
- retry attempts;
- send failures;
- processing latency;
- rebalance events.
