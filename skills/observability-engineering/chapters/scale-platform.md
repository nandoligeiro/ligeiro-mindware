# Escala e Plataforma

## Capítulos Cobertos

- Cap. 15 — Build Versus Buy and Return on Investment
- Cap. 16 — Efficient Data Storage
- Cap. 17 — Cheap and Accurate Enough: Sampling
- Cap. 18 — Telemetry Management with Pipelines

## Build Versus Buy

A decisão não é binária. Avalie:

- custo de ingestão;
- custo de retenção;
- custo de query;
- custo de pessoas;
- custo de operação;
- custo de oportunidade;
- qualidade do workflow de debugging.

Construir uma plataforma exige competência em storage, query engine, UX, pipelines, confiabilidade e suporte interno.

## Storage Para Observabilidade

Observability pede consultas rápidas sobre eventos ricos, com muitos campos e filtros arbitrários.

Características desejáveis:

- armazenamento eficiente por coluna;
- partição por tempo;
- leitura seletiva de colunas;
- consultas interativas;
- suporte a alta cardinalidade;
- retenção alinhada ao valor dos dados.

Time-series databases tradicionais podem ser boas para métricas, mas não necessariamente para análise exploratória de eventos ricos.

## Sampling

Sampling torna custos manejáveis, mas precisa preservar sinal.

Estratégias:

- fixed-rate/constant probability;
- sampling por volume recente;
- sampling por chave;
- dynamic sampling;
- tail sampling;
- regras que preservam erros/outliers.

Perguntas:

- estamos descartando eventos raros importantes?
- a taxa de amostragem é registrada?
- conseguimos reconstruir estimativas?
- a decisão de sampling acontece antes ou depois de saber se o trace é interessante?

## Telemetry Pipelines

Pipelines ajudam com:

- routing;
- buffering;
- workload isolation;
- filtering;
- enrichment;
- transformation;
- sampling;
- security/compliance;
- múltiplos destinos.

Use pipelines para separar produtores e consumidores de telemetria sem transformar instrumentação em spaghetti.
