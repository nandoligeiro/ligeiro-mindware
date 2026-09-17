# Incident & Resilience cheatsheet

## Durante o incidente

1. Qual impacto de usuário e desde quando?
2. Qual escopo/população/região?
3. O que mudou recentemente?
4. Qual mitigação é mais rápida e reversível?
5. Como reduzir blast radius agora?
6. Qual dependência está degradando?
7. Existe fila/backlog crescendo?
8. Como validaremos recovery pelo usuário/SLO?
9. Que evidência precisa ser preservada?
10. Quem é owner da coordenação e das próximas decisões?

## Resiliência por sintoma

| Sintoma | Mecanismos a considerar |
| --- | --- |
| dependência lenta | timeout budget, breaker, bulkhead, fallback |
| overload | queue bounds, load shedding, admission control |
| função secundária falha | graceful degradation |
| região indisponível | failover testado + capacity/state validation |
| dados perdidos/corrompidos | backup/restore, RPO/RTO, reconciliation |
| cascading failure | isolation, budgets, breaker, retry control |
| detecção tardia | SLO/symptom alerts e observabilidade |

## Postmortem mínimo

- impacto;
- timeline;
- trigger;
- propagation path;
- contributing factors;
- controles que funcionaram/falharam;
- detecção e resposta;
- ações priorizadas;
- owner + prazo + evidência de conclusão.

## Regra de ação

Uma ação boa muda algo verificável no sistema ou no modo de operá-lo. “Treinar”, “lembrar” ou “ter atenção” só valem quando viram mecanismo executável e mensurável.
