# SLOs, Alertas e Confiabilidade

## Capítulos Cobertos

- Cap. 12 — Using Service-Level Objectives for Reliability
- Cap. 13 — Acting on and Debugging SLO-Based Alerts

## Ideia-Mãe

Alertas devem representar impacto real ou provável na experiência do usuário. SLOs conectam confiabilidade técnica, prioridade de produto e decisão de negócio.

## Problema do Threshold Alerting

Thresholds tradicionais tendem a gerar:

- alertas demais;
- sintomas internos sem ação clara;
- ruído por componentes que não afetam usuário;
- resposta reativa a falhas conhecidas;
- pouca relação com objetivos de negócio.

## SLI, SLO e Error Budget

- **SLI**: medida, como taxa de sucesso ou latência aceitável.
- **SLO**: alvo, como “99,9% das requests boas em 30 dias”.
- **Error budget**: margem de falha permitida antes de violar o objetivo.

Um SLO útil mede experiência do usuário, não apenas saúde interna.

## Burn Alerts

Burn rate alerta quando o orçamento está sendo consumido rápido demais.

Tipos úteis:

- curto prazo para incidentes rápidos;
- longo prazo para degradação lenta;
- preditivo para agir antes de zerar budget;
- context-aware para trazer dimensões de investigação.

## Debugando Alertas SLO

Quando um SLO dispara:

1. Identifique a população ruim que consome budget.
2. Compare contra requests boas.
3. Ache dimensões dominantes: endpoint, tenant, região, deploy, dependência.
4. Abra traces/eventos exemplares.
5. Corrija o que afeta experiência, não apenas o sintoma mais barulhento.

## Cultura

Error budgets ajudam a negociar velocidade vs confiabilidade. Quando budget está saudável, assuma mais risco; quando está queimando, priorize estabilidade e aprendizado.
