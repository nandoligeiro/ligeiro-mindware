# Pub/Sub, Streams, Scripting e Pipelining

## Pub/Sub

Pub/Sub é efêmero. Bom para notificações simples, ruim para fila durável.

## Redis Streams

Streams fornecem log com IDs, consumer groups, ack e pending entries.

Use para:

- processamento assíncrono leve;
- fan-out com histórico;
- retry/replay;
- integração simples.

## Scripting

Lua scripts ajudam quando múltiplos comandos precisam ser atômicos.

## Transactions e Pipelining

Transactions agrupam comandos com MULTI/EXEC. Pipelining reduz round-trips, mas exige cuidado com erro e interpretação de resultados.
