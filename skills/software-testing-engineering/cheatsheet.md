# Cheatsheet

## Perguntas antes de testar
- Qual defeito relevante queremos detectar?
- Em qual fronteira esse defeito aparece?
- Qual é o teste mais barato que observa o comportamento real?
- O teste precisa de dependência real?
- Qual é o oráculo/assertion de sucesso?
- Quanto tempo o feedback pode levar?

## Regra de bolso
```text
regra pura -> unit/property
integração real -> integration
compatibilidade -> contract
jornada crítica -> E2E
falha/resiliência -> fault injection/chaos
qualidade da suíte -> mutation
```

## Sinais de alerta
- mock do banco para testar SQL;
- mock do broker para provar semântica do broker;
- `sleep()` para esperar assíncrono;
- retries escondendo flaky tests;
- E2E para regra que caberia em unit;
- cobertura como único critério de qualidade;
- teste que não explica qual risco protege.

## Saída recomendada
| Campo | Pergunta |
|---|---|
| Risco | O que pode dar errado? |
| Nível | Onde observar? |
| Ambiente | O que precisa ser real? |
| Oráculo | Como sabemos que passou? |
| Feedback | Quanto custa executar/diagnosticar? |
| Gap | O que ainda não foi provado? |
