# Internals, Confiabilidade e Exactly-Once

## Capítulos Cobertos

- Cap. 6 — Kafka Internals
- Cap. 7 — Reliable Data Delivery
- Cap. 8 — Exactly-Once Semantics

## Internals Essenciais

Kafka coordena:

- cluster membership;
- controller;
- leader/follower replicas;
- request handling;
- storage em logs segmentados;
- índices;
- retenção e compactação.

Entender isso evita tuning aleatório.

## Replication

Cada partition tem leader e followers. Producers e consumers normalmente interagem com leader. Followers replicam dados e entram no conjunto de in-sync replicas quando acompanham o leader.

Termos:

- leader replica;
- follower replica;
- ISR;
- preferred leader;
- under-replicated partition;
- offline partition.

## Confiabilidade

Confiabilidade é propriedade do sistema inteiro:

- configuração de brokers;
- replication factor;
- min in-sync replicas;
- producer acks/retries;
- consumer commit;
- aplicação idempotente;
- storage/rede;
- testes de falha.

## Configuração de Durabilidade

Para evitar falsa segurança:

- use replication factor adequado;
- configure `min.insync.replicas`;
- use producer `acks=all`;
- habilite idempotência quando fizer sentido;
- teste falhas de broker e rede.

## Exactly-Once Semantics

Kafka EOS combina:

- idempotent producers;
- transactions;
- atomicidade entre writes e offset commits em cenários Kafka-to-Kafka.

Use quando:

- aplicação consome de Kafka, processa e produz em Kafka;
- duplicata altera resultado;
- complexidade operacional é aceitável.

Não prometa exactly-once para efeitos externos sem idempotência/transaction do sistema destino.
