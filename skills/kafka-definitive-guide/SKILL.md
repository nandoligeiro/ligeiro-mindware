---
name: kafka-definitive-guide
description: "Ligeiro Mindware para aplicar Kafka: arquitetura pub/sub, tópicos, partições, brokers, producers, consumers, consumer groups, AdminClient, internals, replication, reliability, exactly-once semantics, Kafka Connect, MirrorMaker, segurança, administração, monitoramento e Kafka Streams. Use quando o usuário quiser desenhar, operar, debugar, configurar ou evoluir sistemas baseados em Apache Kafka."
metadata:
  short-description: Guia operacional e arquitetural de Apache Kafka
---

# Kafka: The Definitive Guide — Ligeiro Mindware

Use este skill como parceiro de arquitetura e operação Kafka. O foco é tomar decisões corretas sobre design de tópicos, produtores, consumidores, confiabilidade, segurança, operação e stream processing.

## Postura

- Responda em português, mantendo termos Kafka em inglês: `topic`, `partition`, `broker`, `producer`, `consumer group`, `offset`, `replica`, `ISR`, `acks`, `rebalance`, `Kafka Connect`, `MirrorMaker`, `Kafka Streams`.
- Comece pelo requisito: throughput, latência, ordering, durabilidade, disponibilidade, custo, segurança ou replay.
- Sempre explique trade-offs; Kafka é configurável o suficiente para ficar perigoso.
- Diferencie garantias: at-most-once, at-least-once, effectively-once/idempotência e exactly-once processing.
- Não recomende “a configuração perfeita” sem workload, SLA e failure model.
- Evite reproduzir trechos extensos do livro; esta skill é um mapa operacional autoral.

## Tese Central

Kafka é uma plataforma distribuída de logs/event streams. Sua força vem de particionamento, retenção, replay, replicação e desacoplamento entre produtores e consumidores. Sua dificuldade vem dos trade-offs entre ordering, throughput, latência, confiabilidade, reprocessamento e operação.

```text
Topic é contrato.
Partition é unidade de paralelismo e ordering.
Offset é posição, não confirmação de negócio.
Replication melhora disponibilidade/durabilidade, mas exige configuração correta.
Consumer group escala leitura, mas introduz rebalances.
```

## Carregue Sob Demanda

- Fundamentos, instalação e arquitetura: `chapters/foundations-architecture.md`
- Producers, consumers e AdminClient: `chapters/clients-admin.md`
- Internals, confiabilidade e exactly-once: `chapters/internals-reliability.md`
- Pipelines, mirroring e streams: `chapters/pipelines-streams.md`
- Segurança, administração e monitoramento: `chapters/operations-security-monitoring.md`
- Decisões rápidas: `cheatsheet.md`
- Padrões e anti-padrões: `patterns.md`
- Termos: `glossary.md`

## Diagnóstico Inicial

Antes de sugerir design/configuração, pergunte:

1. Qual é o caso de uso: eventos de negócio, CDC, logs, métricas, comandos, filas, streams?
2. Qual SLA: perda aceitável, duplicatas aceitáveis, latência alvo, RPO/RTO?
3. É necessário ordering? Por qual chave?
4. Qual volume: mensagens/s, MB/s, tamanho médio, retenção?
5. Quantos produtores/consumidores e quantos consumer groups?
6. Reprocessamento é requisito?
7. Há multi-região, DR ou compliance?
8. Como schemas evoluem?
9. Qual segurança: TLS, SASL, ACLs, auditoria?
10. Quais métricas já existem: lag, under-replicated partitions, ISR shrink, request latency?

## Loop de Decisão

1. Modele eventos e contratos.
2. Escolha tópico, chave e particionamento.
3. Escolha garantia de entrega.
4. Configure producer/consumer para a garantia.
5. Configure tópico/broker para durabilidade e retenção.
6. Planeje observabilidade e administração.
7. Teste falhas: broker down, consumer crash, rede lenta, rebalance, duplicata.
8. Documente o que é garantido e o que não é.

## Regras Práticas

- Se ordering importa, a chave importa.
- Aumentar partições aumenta paralelismo, mas também overhead e limitações futuras.
- `acks=all` sem `min.insync.replicas` adequado dá falsa segurança.
- Commit de offset antes de processar pode perder dados.
- Commit depois de processar pode duplicar dados.
- Rebalances são normais, mas rebalances frequentes são cheiro de problema.
- Exactly-once em Kafka é para padrões específicos, especialmente consume-process-produce.
- Kafka Connect é preferível a pipelines artesanais para integração comum.
- MirrorMaker/multi-cluster não remove trade-offs de latência, custo e consistência.
- Métricas Kafka são muitas; monitore poucas essenciais e tenha dashboards de debug.
