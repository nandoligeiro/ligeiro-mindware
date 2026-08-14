# Observability Cheatsheet

## Observability vs Monitoring

| Situação | Melhor ferramenta mental |
|---|---|
| Falha conhecida, threshold conhecido | Monitoring |
| Investigar estado novo ou bizarro | Observability |
| Ver saúde geral de infraestrutura | Monitoring |
| Entender experiência real por usuário/tenant/request | Observability |
| Alertar sobre sintoma interno simples | Monitoring |
| Alertar sobre confiabilidade percebida pelo usuário | SLO + Observability |

## Telemetria Útil

| Tipo | Use para | Cuidado |
|---|---|---|
| Wide event | Preservar contexto completo de uma operação | Não omitir campos de investigação |
| Trace | Entender causalidade distribuída | Span pobre sem atributos não ajuda |
| Metric | Tendência agregada e alerta simples | Agregação perde contexto |
| Log | Narrativa/evento textual | Texto sem estrutura é difícil de consultar |

## Campos Que Quase Sempre Ajudam

- `trace_id`, `span_id`, `parent_id`
- `service.name`, `operation`, `endpoint`, `method`
- `status`, `error`, `error_type`, `duration_ms`
- `user_id`, `tenant_id`, `account_id`, `plan`
- `region`, `az`, `host`, `container`, `runtime`
- `version`, `build_id`, `deploy_id`, `feature_flag`
- `queue`, `topic`, `partition`, `retry_count`
- `db.system`, `db.statement_shape`, `cache_hit`

## Core Analysis Loop

1. Observe uma anomalia ou alerta.
2. Compare uma população ruim contra uma boa.
3. Encontre dimensões que diferenciam as populações.
4. Drill down para eventos/traces exemplares.
5. Forme hipótese.
6. Valide com novo corte dos dados.
7. Corrija código, capacidade, configuração ou instrumentação.

## SLOs

| Conceito | Pergunta |
|---|---|
| SLI | Como medimos experiência relevante? |
| SLO | Qual nível aceitável prometemos internamente? |
| Error budget | Quanto erro podemos gastar antes de mudar prioridade? |
| Burn rate | Quão rápido estamos consumindo o orçamento? |

## Sampling

- Use sampling para controlar volume, não para esconder problemas.
- Prefira decisões que preservem erros, latências raras e tráfego importante.
- Sampling por traces precisa propagar decisão e taxa para reconstruir estimativas.
- Tail/dynamic sampling pode capturar eventos raros melhor que fixed-rate ingênuo.

## Build vs Buy

Compre quando:

- o diferencial é operar o produto, não construir plataforma de observabilidade;
- precisa acelerar adoção;
- custo de pessoas/plataforma é maior que vendor;
- workflow pronto atende bem.

Construa quando:

- requisitos são muito específicos;
- escala/custo justificam time dedicado;
- há competência real para storage/query/UX;
- a plataforma será produto interno sustentado.
