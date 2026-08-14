# Fundamentos e Arquitetura

## Capítulos Cobertos

- Cap. 1 — Meet Kafka
- Cap. 2 — Installing Kafka

## Kafka em Uma Frase

Kafka é uma plataforma distribuída para publicar, armazenar, replicar, consumir e reprocessar streams de eventos.

## Conceitos Base

- **Message/record**: unidade de dados.
- **Topic**: categoria/log de records.
- **Partition**: sequência ordenada e append-only dentro de um topic.
- **Offset**: posição do record na partition.
- **Producer**: escreve records.
- **Consumer**: lê records.
- **Consumer group**: escala leitura dividindo partitions.
- **Broker**: nó do cluster.
- **Cluster**: conjunto de brokers.

## Por Que Kafka?

Use Kafka quando precisa:

- desacoplar produtores e consumidores;
- reter eventos para replay;
- escalar ingestão e leitura;
- alimentar múltiplos consumidores;
- construir pipelines confiáveis;
- processar streams continuamente;
- integrar sistemas com ritmos diferentes.

## Instalação e Ambiente

Para produção, pense além de “subiu o broker”:

- Linux e JVM suportada;
- disco rápido e suficiente;
- rede previsível;
- ZooKeeper ou KRaft conforme versão;
- configuração de broker;
- múltiplos brokers;
- rack/zone awareness;
- segurança desde o início;
- monitoramento e backups operacionais.

## Arquitetura de Partições

Partições determinam:

- paralelismo de escrita/leitura;
- ordering por chave;
- distribuição de dados;
- capacidade de escalar consumer groups;
- custo operacional.

Escolha com cuidado: aumentar partições é possível, mas muda distribuição de keys e pode afetar ordering futuro.
