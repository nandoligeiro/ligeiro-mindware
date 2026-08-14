# Padrões e Anti-Padrões Kafka

## Padrões

### Event Log como Contrato

Modele tópicos como contratos duráveis entre produtores e consumidores.

**Use quando:** múltiplos consumidores precisam evoluir independentemente.

### Keyed Ordering

Use chave para garantir ordering por entidade dentro de uma partition.

**Use quando:** eventos de uma conta, pedido, usuário ou agregado precisam ordem relativa.

### At-Least-Once com Idempotência no Sink

Aceite duplicatas e torne processamento idempotente.

**Use quando:** perda é pior que duplicata.

### Idempotent Producer

Habilite producer idempotente para evitar duplicatas causadas por retries.

**Use quando:** producer precisa confiabilidade sem duplicar por falha transitória.

### Transactional Consume-Process-Produce

Use transações para processar de Kafka para Kafka com exactly-once processing.

**Use quando:** aplicação consome, transforma/agrega e produz de volta no Kafka.

### Kafka Connect

Use conectores para mover dados entre Kafka e sistemas externos.

**Use quando:** integração é comum, repetível e precisa operação padronizada.

### MirrorMaker / Cluster Linking Mental Model

Use mirroring para DR, migração, agregação regional ou compliance, entendendo latência e topologia.

**Use quando:** há necessidade real de múltiplos clusters interdependentes.

## Anti-Padrões

### Um Tópico Para Tudo

Misturar contratos e domínios em tópico genérico.

**Correção:** separar por evento/contrato, com schema claro.

### Partições Sem Planejamento

Criar partições demais ou de menos sem pensar em paralelismo, ordering e crescimento.

**Correção:** dimensionar por throughput, consumidores, keys e futuro.

### Commit Cego de Offset

Auto-commit sem entender quando a mensagem foi realmente processada.

**Correção:** controlar commit conforme garantia desejada.

### Falsa Durabilidade

Usar replication factor > 1, mas producer com `acks=1` e `min.insync.replicas` inadequado.

**Correção:** alinhar producer, tópico e broker.

### Consumer Lag Sem Contexto

Alertar por qualquer lag sem entender padrão de batch, horário e drenagem.

**Correção:** alertar em tendência, idade e impacto.

### Rebalance Storm

Consumers entram e saem do group repetidamente, interrompendo processamento.

**Correção:** investigar heartbeat, poll interval, static membership, cooperative rebalance e tempo de processamento.

### Segurança Pós-Produção

Adicionar TLS/SASL/ACL depois que integrações já se espalharam.

**Correção:** tratar segurança como arquitetura desde o início.
