# Database Engineering — Cheatsheet

## 10 perguntas
1. Quais invariantes o storage precisa proteger?
2. Quais são os hot reads/writes?
3. Qual volume/cardinalidade/crescimento?
4. Quais keys e constraints preservam correção?
5. Quais queries justificam índices?
6. Qual anomalia de concorrência é intolerável?
7. App e schema coexistem durante migration?
8. Quantas conexões totais todas as instâncias podem abrir?
9. Backup foi restaurado e medido?
10. Quais métricas mostram locks, lag, slow queries e saturation?

## Atalhos
| Situação | Direção inicial |
| --- | --- |
| unicidade de negócio | unique constraint + tratamento de conflito |
| conflito raro de update | optimistic concurrency/version |
| schema incompatível | expand-and-contract |
| query lenta | plano + cardinalidade + índice orientado a workload |
| muitas instâncias | budget global de conexões |
| requisito de recovery | backup + restore testado + RPO/RTO |

## Red flags
- banco espelhando ORM sem workload
- índice sem query que o justifique
- isolamento máximo por padrão
- migration destrutiva em deploy único
- pool por pod sem conta global
- backup nunca restaurado