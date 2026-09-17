# Transações, Outbox/Inbox e Recuperação

## Dual write é um cheiro forte

Quando uma operação precisa:

1. alterar estado local; e
2. publicar/enviar algo remotamente,

há uma janela de inconsistência se essas duas ações não compartilham transação.

Exemplo ruim:

```text
update database
publish event
```

Se o processo cair entre as etapas, estado e evento divergem.

## Transactional outbox

Na mesma transação local:

```text
business state update
+ outbox record
COMMIT
```

Um relay separado publica a outbox e marca/progride sua entrega. O consumidor ainda deve tolerar duplicatas porque publicação pode ser repetida após crash.

Outbox resolve atomicidade da **intenção local**, não exactly-once end-to-end.

## Inbox / processed-message

No consumidor, use uma chave durável da mensagem/operação para impedir efeito repetido.

Quando possível:

```text
insert inbox(message_id)
apply business effect
COMMIT
```

Unique constraint pode transformar duplicate delivery em no-op controlado.

## Saga

Saga coordena uma sequência de transações locais.

Escolha entre:

- choreography: eventos acionam próximos passos;
- orchestration: coordenador explícito mantém estado e comanda etapas.

Avalie:

- quantidade de etapas;
- necessidade de visibilidade do workflow;
- acoplamento temporal;
- dificuldade de compensação;
- ownership organizacional.

## Compensação

Compensação não apaga a história. É uma nova ação de negócio que tenta neutralizar ou corrigir um efeito anterior.

Exemplos:

- estornar em vez de “desfazer” uma cobrança já registrada;
- liberar reserva em vez de fingir que nunca existiu;
- emitir evento corretivo em vez de apagar evento consumido.

Compensações também podem falhar e precisam de retry, idempotência e observabilidade.

## Reconciliação

Use reconciliação periódica quando:

- não existe atomicidade entre sistemas;
- callbacks/eventos podem ser perdidos;
- integrações externas possuem estado consultável;
- custo de inconsistência temporária é aceitável.

O reconciler compara fontes, detecta divergência e aplica ação segura/idempotente.

## DLQ não é estratégia de recuperação completa

DLQ é estacionamento. Para ser útil precisa de:

- reason code;
- payload/contexto suficiente;
- política de replay;
- idempotência no replay;
- owner operacional;
- métrica e prazo de tratamento.

## Distributed transactions

2PC/XA pode ser apropriado em fronteiras controladas, mas aumenta acoplamento, coordenação e blast radius.

Antes de adotar, compare com:

- transação local + outbox;
- saga;
- idempotência + retry;
- reconciliação.

Não rejeite nem adote 2PC por dogma: documente latência, disponibilidade, participantes e requisitos de atomicidade.
