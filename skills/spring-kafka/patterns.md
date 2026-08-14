# Padrões e Anti-Padrões Spring Kafka

## Padrões

- **Template Gateway**: encapsule `KafkaTemplate` atrás de um serviço de domínio/aplicação.
- **Listener Thin Handler**: listener valida, traduz e delega; regra fica em serviço.
- **DLT Observável**: toda DLT tem métrica, alerta e processo de replay/triagem.
- **Retry por Classe de Erro**: retry para transitórios; DLT/fail-fast para permanentes.
- **`@RetryableTopic` para Backoff Longo**: use retries não bloqueantes quando esperar no container prenderia a partition por tempo demais.
- **Transactional Pipeline**: use transações quando consome de Kafka e produz para Kafka.

## Anti-Padrões

- **Listener Faz Tudo**: handler cheio de regra, IO e tratamento especial.
- **Retry Infinito**: mensagem venenosa bloqueia partition.
- **`@RetryableTopic` em Erro Permanente**: fica só movendo mensagem ruim entre tópicos.
- **DLT Sem Dono**: erros acumulam sem SLA.
- **Commit Antes do Efeito**: risco de perda.
- **Transação Como Talismã**: usar `KafkaTransactionManager` esperando cobrir banco/sistemas externos sem desenho transacional.
