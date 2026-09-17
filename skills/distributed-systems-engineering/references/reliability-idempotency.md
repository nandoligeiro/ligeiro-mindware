# Reliability, Retries e Idempotência

## Regra de ouro

Em rede, timeout não prova que o remoto não executou. Trate o resultado como desconhecido até obter evidência.

## Retry taxonomy

Classifique falhas antes de repetir:

- transitórias: timeout, 429, indisponibilidade temporária;
- persistentes: validação, regra de negócio, autorização;
- desconhecidas: conexão caiu após envio; resposta perdida;
- ambíguas: remoto pode ter aplicado efeito sem confirmação.

Retry deve possuir:

- limite de tentativas;
- orçamento de tempo;
- exponential backoff;
- jitter;
- classificação de erro;
- observabilidade por attempt.

## Idempotency key

A chave deve representar a operação de negócio, não a tentativa técnica.

Exemplos:

- `payment-request-id` melhor que UUID novo por retry;
- `notification-command-id` melhor que timestamp de tentativa;
- `order-id + operation-type` quando o domínio garante unicidade dessa operação.

## Durable claim

Fluxo recomendado:

```text
receive(operation_id)
  -> try claim operation_id
     -> already completed: return stored result
     -> in progress: decide wait/retry/conflict
     -> claimed: execute effect
  -> persist result/status
  -> acknowledge/respond
```

O claim precisa estar no mesmo boundary transacional do efeito quando a unicidade depende disso; caso contrário existe janela de duplicação.

## Dedupe window

TTL só é seguro quando existe um limite de negócio claro para repetição. Expirar cedo demais reabre a possibilidade de efeito duplicado.

Pergunte:

- por quanto tempo o upstream pode repetir?
- replay histórico é possível?
- a chave é globalmente única?
- precisamos guardar apenas marcador ou também resultado?

## Acknowledgement

Nunca confunda `ack` de transporte com sucesso do negócio.

Um broker pode considerar a mensagem consumida enquanto um efeito externo ainda falha, dependendo do ponto de commit. Modele explicitamente a ordem:

```text
receive -> effect -> durable state -> ack
```

ou, quando necessário, use outbox/inbox para separar atomicidade local de entrega assíncrona.
