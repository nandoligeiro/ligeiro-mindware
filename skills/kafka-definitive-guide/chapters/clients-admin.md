# Producers, Consumers e AdminClient

## Capítulos Cobertos

- Cap. 3 — Kafka Producers
- Cap. 4 — Kafka Consumers
- Cap. 5 — Managing Apache Kafka Programmatically

## Producer

O producer decide para qual topic/partition enviar, serializa registros, agrupa em batches, lida com retries e aguarda acknowledgments.

Decisões importantes:

- serializer e schema;
- key e partitioner;
- `acks`;
- retries;
- idempotência;
- compression;
- batch size e linger;
- tratamento de erro.

## Consumer

O consumer lê records, controla posição por offsets e participa de um consumer group.

Decisões importantes:

- subscribe vs assign;
- auto commit vs manual commit;
- processamento síncrono/assíncrono;
- max poll records/interval;
- heartbeat/session timeout;
- partition assignment;
- static membership;
- cooperative rebalance.

## Consumer Groups

Um consumer group divide partições entre consumers. Uma partition de um topic é consumida por no máximo um consumer do mesmo group por vez.

Implicações:

- mais consumers que partitions ficam ociosos;
- rebalances pausam/reorganizam trabalho;
- lag deve ser analisado por group/topic/partition;
- paralelismo depende de partitions.

## Offset Commit

Offset commit registra progresso, não sucesso de negócio.

- Commit antes do processamento: risco de perda.
- Commit depois do processamento: risco de duplicata.
- Commit transacional: útil em consume-process-produce Kafka.

## AdminClient

AdminClient administra Kafka via API:

- criar/listar/deletar topics;
- alterar configs;
- descrever cluster;
- gerenciar ACLs;
- verificar metadata.

Use com parcimônia: criação dinâmica de topics pode ser útil, mas também pode criar caos operacional se não houver governança.
