---
name: distributed-systems-engineering
description: "Ligeiro Mindware para projetar, diagnosticar e revisar sistemas distribuídos: falhas parciais, timeouts, retries, backoff e jitter, idempotência, deduplicação, consistência eventual, ordering, concorrência, claim/lease/fencing, saga, compensação, transactional outbox/inbox, backpressure e load shedding. Use quando o problema atravessar processos, serviços, filas, bancos, jobs ou regiões e exigir raciocínio explícito sobre entrega, consistência, coordenação ou recuperação de falhas."
metadata:
  short-description: Engenharia pragmática de sistemas distribuídos
---

# Distributed Systems Engineering — Ligeiro Mindware

Use esta skill para raciocinar sobre sistemas em que componentes independentes se comunicam por rede e podem falhar, atrasar, duplicar, reordenar ou processar parcialmente uma operação.

O objetivo não é aplicar padrões por reflexo. É tornar explícitos **failure modes, guarantees, ownership e recovery semantics** antes de escolher tecnologia.

## Quando ativar

Ative quando houver pelo menos um destes sinais:

- uma operação cruza dois ou mais processos/serviços;
- existe REST/RPC, broker, fila, stream, job distribuído ou banco remoto;
- retry pode repetir efeito colateral;
- é necessário decidir entre at-most-once, at-least-once ou comportamento efetivamente once;
- consistência imediata não é garantida ou não é desejável;
- há concorrência entre workers, consumers ou schedulers;
- existem leases, locks distribuídos, leader election ou ownership temporário;
- uma transação de negócio cruza recursos independentes;
- há risco de overload, fila crescente ou cascading failure.

## Quando não ativar

Não use esta skill para:

- dúvidas puramente locais de sintaxe Java/Spring;
- CRUD local sem comunicação remota ou concorrência relevante;
- configuração específica de Kafka quando o problema é apenas API/configuração do cliente;
- tuning de JVM sem semântica distribuída;
- modelagem de domínio que não envolve integração, consistência ou coordenação entre componentes.

Nesses casos, prefira a skill específica do framework, Kafka, DDD ou performance.

## Modelo mental central

Em um sistema distribuído, você raramente sabe ao mesmo tempo **o que aconteceu remotamente** e **se a resposta chegou até você**.

```text
request
   │
   ├─ operação não chegou
   ├─ operação chegou e falhou
   ├─ operação chegou e concluiu
   └─ operação concluiu, mas a resposta se perdeu
                     │
                     └─ retry pode duplicar efeito
```

Portanto, sempre separe:

1. **delivery semantics** — quantas vezes a tentativa pode ser entregue;
2. **processing semantics** — quantas vezes o efeito pode acontecer;
3. **visibility semantics** — quando outros componentes enxergam o efeito;
4. **recovery semantics** — como o sistema converge depois da falha.

## Fluxo de análise

Ao receber um problema distribuído, siga esta ordem:

1. **Desenhe a operação ponta a ponta.** Liste cada fronteira de processo, rede, broker, banco e efeito colateral.
2. **Nomeie os failure modes.** Timeout, resposta perdida, duplicate delivery, reordering, crash-after-write, crash-before-ack, split ownership, overload.
3. **Defina a garantia necessária.** Não assuma exactly-once; descreva o efeito de negócio que precisa ser único.
4. **Defina identity.** Qual chave identifica a operação ou comando de negócio?
5. **Defina ownership.** Quem pode executar e por quanto tempo? Há concorrência?
6. **Defina persistência do progresso.** Onde ficam claim, resultado, offset, estado intermediário ou intenção de publicação?
7. **Defina retry.** Quais erros são transitórios, qual orçamento de tentativa e como aplicar backoff+jitter?
8. **Defina recuperação.** Retry, compensação, reconciliação, DLQ, replay ou intervenção humana?
9. **Defina observabilidade.** Correlation/operation id, attempt, state transition, owner/fence token, latency e reason codes.
10. **Só então escolha mecanismos.** Broker, lock, transaction, outbox, saga, cache, scheduler etc.

## Heurísticas principais

### Timeout não significa falha remota

Timeout significa apenas: **não recebi confirmação dentro do tempo esperado**.

Nunca transforme automaticamente timeout em “não executou”. Se houver efeito colateral, assuma estado desconhecido até prova em contrário.

### Retry exige idempotência ou reconciliação

Se repetir uma chamada pode repetir cobrança, envio, reserva, baixa ou publicação, não faça retry cego.

Prefira:

```text
operation_id + durable claim/result + retry-safe handler
```

Quando idempotência forte não for possível, tenha mecanismo explícito de reconciliação/compensação.

### At-least-once + idempotência costuma ser melhor que buscar exactly-once global

“Exactly once” normalmente depende de fronteiras específicas. Para sistemas heterogêneos, modele **efeito de negócio único** com idempotency key, dedupe e persistência adequada.

### Claim, lease e fencing resolvem problemas diferentes

- `claim`: registra quem assumiu o trabalho;
- `lease`: limita temporalmente esse ownership;
- `fencing token`: impede um owner antigo de continuar escrevendo após perder o lease.

Lease sem fencing pode permitir **stale owner**.

### Outbox resolve atomicidade entre estado local e publicação

Se você precisa atualizar banco e publicar evento como uma única intenção de negócio, prefira transactional outbox a dual-write ingênuo.

### Inbox/dedupe protege o consumidor

Se entrega duplicada é possível, persista uma chave de processamento antes ou junto do efeito que precisa ser único.

### Saga não é transação distribuída mágica

Use saga quando cada etapa possui commit local e existe ação compensatória ou estratégia de convergência. Compensação não é rollback perfeito; é uma nova ação de negócio.

### Backpressure é contrato, não detalhe de performance

Quando downstream não acompanha, escolha conscientemente entre:

- desacelerar produtor;
- enfileirar com limite;
- rejeitar;
- degradar funcionalidade;
- descartar trabalho de menor valor.

Fila ilimitada só troca erro imediato por colapso atrasado.

## CAP sem slogan

Use CAP apenas quando existe partição de rede relevante e você precisa discutir comportamento durante a partição.

Não use “CP vs AP” como etiqueta permanente de produto. Pergunte:

- qual operação?
- qual dado?
- durante qual falha?
- qual comportamento de leitura/escrita é aceitável?

## Carregue sob demanda

- Falhas, retries e idempotência: `references/reliability-idempotency.md`
- Consistência, ordering e coordenação: `references/consistency-coordination.md`
- Sagas, outbox/inbox e recuperação: `references/transactions-recovery.md`
- Decisões rápidas: `cheatsheet.md`
- Padrões e anti-padrões: `patterns.md`

## Saída esperada

Uma boa resposta desta skill deve explicitar:

1. fronteiras distribuídas;
2. failure modes relevantes;
3. garantia necessária;
4. identity/idempotency strategy;
5. ownership/concurrency strategy quando aplicável;
6. retry e recovery policy;
7. trade-offs e condição de falha residual;
8. sinais de observabilidade necessários.

Não responda apenas com nome de pattern. Explique **por que ele resolve aquele failure mode** e qual risco continua existindo.
