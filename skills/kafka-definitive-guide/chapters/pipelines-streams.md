# Pipelines, Mirroring e Streams

## Capítulos Cobertos

- Cap. 9 — Building Data Pipelines
- Cap. 10 — Cross-Cluster Data Mirroring
- Cap. 14 — Stream Processing

## Kafka em Pipelines

Kafka funciona como buffer durável e desacoplador entre sistemas com ritmos diferentes.

Avalie:

- timeliness;
- confiabilidade;
- throughput variável;
- formatos de dados;
- transformações;
- segurança;
- tratamento de falhas;
- acoplamento e agilidade.

## Kafka Connect

Kafka Connect padroniza integrações source/sink.

Use para:

- bancos;
- data lakes;
- search;
- object storage;
- CDC;
- filas/sistemas externos.

Vantagens:

- configuração declarativa;
- offset management;
- escalabilidade;
- tolerância a falhas;
- ecossistema de conectores.

## Mirroring Entre Clusters

Casos de uso:

- DR/HA;
- migração cloud/datacenter;
- agregação regional;
- edge para central;
- compliance;
- isolamento por workload/SLA.

Arquiteturas:

- hub-and-spoke;
- active-active;
- active-standby;
- aggregation.

Cuidado com latência, largura de banda, custos, conflitos de escrita e semântica de failover.

## Stream Processing

Stream processing processa eventos continuamente.

Conceitos:

- event time;
- processing time;
- windows;
- joins;
- aggregation;
- state stores;
- topology;
- KStream/KTable;
- repartitioning.

Use Kafka Streams quando quer embutir processamento em aplicação Java sem operar framework externo.
