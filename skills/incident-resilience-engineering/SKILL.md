---
name: incident-resilience-engineering
description: "Ligeiro Mindware para responder incidentes e projetar resiliência operacional: detecção, severidade, triage, containment, mitigação, recuperação, comunicação, SLO/error budget, graceful degradation, circuit breakers, bulkheads, load shedding, dependency failure, failover, disaster recovery, postmortem e ações verificáveis. Use quando o problema envolve degradação em produção, indisponibilidade, propagação de falha, recuperação ou prevenção baseada em incidentes reais."
metadata:
  short-description: Resiliência operacional e resposta a incidentes
---

# Incident & Resilience Engineering

Use esta skill para transformar falhas de produção em **controle operacional + aprendizado verificável**.

## Não ativar

Não use como resposta principal para:

- debugging local sem impacto operacional;
- apenas configurar logs/metrics;
- modelar retries/idempotência sem incidente ou objetivo de resiliência;
- processo administrativo de incidentes sem engenharia;
- postmortem como relatório narrativo sem ações técnicas.

## Modelo

Separe cinco dimensões:

1. **detect** — como sabemos que há impacto real;
2. **stabilize** — como limitamos blast radius;
3. **recover** — como restauramos serviço/correção;
4. **explain** — qual cadeia causal e contributing factors;
5. **learn** — qual mudança verificável reduz recorrência ou impacto.

## Fluxo de incidente

1. Declare impacto observado e população afetada.
2. Classifique severidade pelo impacto, não pela ansiedade do time.
3. Estabeleça incident commander/owner quando o caso exigir coordenação.
4. Crie timeline factual com timestamps e decisões.
5. Pare mudanças não essenciais se aumentarem incerteza.
6. Priorize mitigação reversível e redução de blast radius.
7. Diferencie containment de root cause.
8. Valide recuperação por sinais de usuário/SLO, não apenas por “pods verdes”.
9. Preserve evidências para análise posterior.
10. Gere ações com owner, deadline, evidência de conclusão e risco coberto.

## Heurísticas de resiliência

### SLO antes de alerta
- alerte por sintomas de usuário e risco ao SLO quando possível;
- error budget ajuda a equilibrar velocidade e confiabilidade;
- disponibilidade sem janela/população não é uma métrica útil.

### Degradação controlada
Prefira preservar funções críticas quando dependências secundárias falharem. Defina explicitamente o que pode ser omitido, atrasado, servido stale ou rejeitado.

### Circuit breaker
Use quando falhas repetidas de uma dependência estão desperdiçando capacidade ou amplificando latência. Breaker não substitui timeout, retry budget, idempotência ou recuperação da dependência.

### Bulkhead
Isole pools/threads/connections/quotas quando uma classe de carga ou dependência não deve consumir toda a capacidade compartilhada.

### Load shedding
Sob saturação, rejeitar cedo pode ser mais resiliente que aceitar trabalho que expirará depois. Preserve prioridade e limite filas.

### Failover
Failover precisa ser testado. Considere consistência de estado, DNS/routing, warm-up, credentials, capacity e retorno para a região/origem normal.

### Disaster recovery
Declare RTO e RPO para o serviço/dado concreto. Backup sem restore testado não prova recovery.

### Dependency resilience
Modele cada dependência por:
- criticality;
- timeout/budget;
- failure mode;
- fallback/degradation;
- recovery/reconciliation;
- observability.

## Postmortem

Evite “erro humano” como causa terminal. Analise:

- condição inicial;
- trigger;
- propagation path;
- controles que funcionaram;
- controles ausentes/falhos;
- detecção e resposta;
- fatores organizacionais/técnicos que tornaram o erro possível.

Ações devem alterar sistema, processo executável ou capacidade de detecção. “Ter mais atenção” não é ação de engenharia.

## Saída esperada

A resposta deve explicitar:

- impacto e escopo;
- hipótese/timeline conhecida;
- containment/mitigation;
- recovery criteria;
- mecanismos de resiliência relevantes;
- residual risk;
- observabilidade;
- ações e evidência de conclusão.

## Leituras internas

Consulte `patterns.md` e `cheatsheet.md`.
