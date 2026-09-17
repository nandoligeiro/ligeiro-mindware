# Distributed Systems Engineering — Cheatsheet

## Perguntas primeiro

1. Qual é a operação de negócio?
2. Quais fronteiras remotas ela cruza?
3. O que pode duplicar, atrasar, reordenar ou sumir?
4. Qual efeito precisa ser único?
5. Qual chave identifica a operação?
6. Quem possui o trabalho e por quanto tempo?
7. Onde o progresso fica durável?
8. Quais falhas merecem retry?
9. Como o sistema converge depois de falhar?
10. Como vamos observar attempts, owner e resultado?

## Decisões rápidas

| Problema | Primeira opção a avaliar |
|---|---|
| timeout em operação com side effect | idempotency key + consulta/reconciliação |
| duplicate delivery | inbox/dedupe + efeito idempotente |
| banco + evento | transactional outbox |
| múltiplos workers disputando trabalho | claim; lease se ownership expira; fencing se stale owner pode escrever |
| workflow multi-serviço | saga/orchestration ou choreography conforme visibilidade e acoplamento |
| estado divergente entre sistemas | reconciliation loop |
| downstream saturado | backpressure/load shedding |
| conflito de escrita raro | optimistic concurrency/version |
| necessidade de ordering | preferir ordering por key/entity antes de global |

## Retry seguro

```text
classify error
  -> retryable?
      -> bounded attempts
      -> time budget
      -> exponential backoff
      -> jitter
      -> same operation identity
  -> not retryable: fail fast / compensate / escalate
```

## Idempotência

```text
operation_id
  -> claim
  -> execute
  -> persist result
  -> return/ack
```

Guarde o resultado quando o caller pode repetir e precisa receber resposta equivalente.

## Lease + fencing

```text
claim(resource) -> token N
renew while alive
new owner -> token N+1
resource rejects writes with token < current
```

## Outbox

```text
TX:
  update business state
  insert outbox event
COMMIT
relay -> publish -> mark/progress
```

## Inbox

```text
TX:
  insert message_id (unique)
  apply effect
COMMIT
```

## Red flags

- retry sem idempotência;
- novo UUID por tentativa;
- ack confundido com sucesso de negócio;
- dual write;
- distributed lock sem fencing;
- DLQ sem replay seguro;
- fila ilimitada;
- “exactly-once” sem declarar a fronteira da garantia;
- CAP usado como slogan.
