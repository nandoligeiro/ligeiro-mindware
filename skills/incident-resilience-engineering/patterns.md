# Patterns e anti-patterns — Incident & Resilience

## Patterns

### Mitigate before explain
Durante impacto ativo, priorize mitigação segura e reversível antes de buscar a narrativa causal completa.

### Blast-radius reduction
Use feature flags, traffic shaping, disablement de função não crítica, quotas ou isolamento para limitar propagação.

### Symptom-based detection
Alertas devem refletir impacto do usuário/SLO, complementados por sinais de causa para diagnóstico.

### Bounded failure
Timeouts, circuit breakers, bulkheads, queue limits e load shedding impedem que uma dependência degrada consuma toda a capacidade.

### Graceful degradation
Defina previamente quais funções são críticas e quais podem retornar resposta parcial, stale, async ou indisponível.

### Recovery verification
Considere incidente recuperado só após validar indicadores de usuário/SLO e backlog/reconciliação, não apenas saúde de infraestrutura.

### Postmortem-to-regression
Converta failure modes reais em teste, alerta, policy, runbook, capacity guardrail ou design change verificável.

## Anti-patterns

- investigar root cause enquanto o blast radius continua crescendo;
- declarar recovery porque deploy/pod ficou verde;
- alertar em toda exceção sem relação com impacto;
- circuit breaker sem timeout;
- retries ilimitados durante overload;
- failover nunca exercitado;
- backup nunca restaurado;
- postmortem com “erro humano” como fim da análise;
- ação “tomar mais cuidado”;
- dezenas de ações sem owner/prioridade/evidência;
- confundir containment com resolução definitiva;
- usar média de disponibilidade sem janela e população.
