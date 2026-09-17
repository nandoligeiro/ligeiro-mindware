# Software Delivery Engineering — Cheatsheet

## 10 perguntas
1. Qual commit gerou este artefato?
2. O artefato é imutável?
3. O mesmo conteúdo é promovido entre ambientes?
4. O que varia por configuração/policy?
5. Quais gates protegem riscos reais?
6. Deploy e release precisam ser separados?
7. Qual estratégia de branch reduz integração tardia?
8. Canary/blue-green têm métricas e abort criteria?
9. Rollback é realmente seguro para schema/dados?
10. Conseguimos rastrear commit -> artifact -> deployment?

## Atalhos
| Situação | Direção inicial |
| --- | --- |
| rebuild por ambiente | build once + config externa |
| snapshot mutável em HOM/PROD | publicar artefato imutável |
| tags por tentativa de deploy | promover mesma identidade, tag só para mudança relevante |
| rollout arriscado | progressive delivery + sinais |
| feature pronta mas não liberável | feature flag |
| migration irreversível | rollforward-first + compatibilidade |

## Red flags
- versão cujo conteúdo muda
- HOM e PROD recompilados separadamente
- canary sem thresholds
- rollback que ignora dados
- branch longa como buffer permanente
- tag usada como log operacional