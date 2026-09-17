# API Contract Engineering — Cheatsheet

## 10 perguntas
1. Quem publica e quem consome?
2. Qual comportamento público existe hoje?
3. O que é shape e o que é semântica?
4. A mudança é additive, restrictive, semantic ou removal?
5. Quem quebra se apenas o provider mudar?
6. Quem quebra se apenas o consumer mudar?
7. Dá para evoluir compatível sem nova versão?
8. Qual teste prova compatibilidade?
9. Como vamos medir migração/depreciação?
10. Quem é owner do contrato?

## Atalhos
| Situação | Direção inicial |
| --- | --- |
| novo campo | opcional + semântica/default explícitos |
| remoção/rename | migração paralela + telemetry + sunset |
| mudança de significado | novo contrato/versão quando não houver evolução compatível |
| consumer externo | contract gate + compatibilidade explícita |
| evento assíncrono | schema + semântica + identity + ordering/dedupe assumptions |
| enum crescendo | validar tolerância a unknown values |
| depreciação | medir uso real antes de remover |

## Red flags
- "o schema compila, então não quebra"
- `/v2` como resposta automática
- mudança silenciosa de unidade/timezone/default
- remoção sem telemetry
- CDC tratado como substituto de toda integração
- contrato sem owner