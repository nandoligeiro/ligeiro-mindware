# Clients, Templates e Listeners

## Producers

`KafkaTemplate` é o caminho idiomático para envio. Configure producer factory, serializers e propriedades Kafka/Spring Boot.

Boas decisões:

- chave define ordering;
- tópico é contrato;
- headers carregam correlação;
- resultado de envio deve ser observado/tratado.

## Consumers

`@KafkaListener` transforma consumo em método Spring. O listener container gerencia poll, commits, threads e lifecycle.

Cuidados:

- concurrency não supera partitions úteis;
- listener deve ser thread-safe;
- tempo de processamento afeta poll/rebalance;
- validação e conversão devem falhar de forma previsível.
