---
name: software-delivery-engineering
description: "Ligeiro Mindware para desenhar pipelines e estratégias de entrega: CI/CD, build once promote many, artefatos imutáveis, versionamento, ambientes, trunk-based e branch flows, feature flags, progressive delivery, rollback/rollforward e change safety. Use quando o problema envolver como software validado vira release e chega com segurança a ambientes e produção."
metadata:
  short-description: CI/CD, release e promoção segura
---

# Software Delivery Engineering

Otimize para **fluxo seguro e repetível**, não para quantidade de stages ou tags.

## Ativação
Use esta skill quando houver:
- desenho/revisão de CI/CD;
- promoção entre ambientes;
- estratégia de versionamento/tag/release;
- artefato mutável vs imutável;
- trunk-based, release branches ou long-lived branches;
- feature flags, canary, blue/green ou progressive delivery;
- rollback/rollforward e change failure rate.

Não ative para:
- comando git isolado;
- sintaxe pontual de workflow sem decisão de delivery;
- troubleshooting puramente de runtime.

## Modelo mental

Separe:
1. **source state** — commit que representa a mudança;
2. **build** — produção do artefato;
3. **verification** — testes/gates sobre aquele artefato;
4. **release identity** — versão/digest/tag que referencia conteúdo imutável;
5. **promotion** — mover o mesmo conteúdo entre ambientes;
6. **deployment** — disponibilizar no runtime;
7. **release exposure** — liberar comportamento a usuários, possivelmente via flag.

## Princípio central

**Build once, promote the same immutable artifact.**

Ambiente deve variar configuração e policy, não recompilar o software.

## Fluxo de análise
1. Mapeie source -> build -> verify -> publish -> promote -> deploy -> expose.
2. Identifique onde o conteúdo pode mudar sem nova identidade.
3. Torne artefatos promovidos imutáveis e endereçáveis por digest/versão.
4. Defina gates por risco, não por tradição de ambientes.
5. Escolha branch strategy que minimize integração tardia.
6. Separe deploy de release quando feature flags reduzirem blast radius.
7. Escolha progressive delivery quando sinais permitem decisão segura.
8. Defina rollback e rollforward antes da falha.
9. Registre evidence: commit, artifact digest, tests, approvals/policies e deployment.
10. Meça lead time, deployment frequency, change failure e recovery.

## Heurísticas

### Mutable snapshots
Snapshots podem servir a feedback rápido de integração, mas não devem ser a identidade promovida de homologação/produção quando o conteúdo pode mudar sob o mesmo nome.

### Tags
Tag deve apontar para uma identidade histórica útil. Não use tag como substituto de cada tentativa operacional quando o artefato testado pode ser promovido por digest/version sem regeneração.

### Branching
Prefira integração frequente. Branches longas aumentam divergência e integração tardia; release branches só quando há necessidade operacional clara.

### Rollback vs rollforward
Rollback é útil quando reversão de schema/state é segura. Rollforward costuma ser melhor quando dados/migrações tornam reversão perigosa.

### Progressive delivery
Canary/blue-green só ajudam quando há métricas, thresholds, abort criteria e automação de decisão/rollback.

## Saída esperada
Declare:
- cadeia de delivery atual;
- identidade do artefato e imutabilidade;
- estratégia de promoção;
- branch/release model e tradeoffs;
- gates e evidências;
- estratégia de exposição/progressive delivery;
- rollback/rollforward;
- métricas e failure modes residuais.

Consulte `patterns.md` e `cheatsheet.md`.