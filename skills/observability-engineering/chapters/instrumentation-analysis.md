# Instrumentação e Análise

## Capítulos Cobertos

- Cap. 5 — Structured Events Are the Building Blocks of Observability
- Cap. 6 — Stitching Events into Traces
- Cap. 7 — Instrumentation with OpenTelemetry
- Cap. 8 — Analyzing Events to Achieve Observability
- Cap. 11 — Observability-Driven Development

## Structured Events

O bloco básico é o evento estruturado rico. Ele deve carregar contexto suficiente para responder perguntas futuras.

Campos recomendados:

- identidade: usuário, tenant, conta, request;
- execução: serviço, operação, endpoint, método;
- causalidade: trace, span, parent;
- resultado: status, erro, duração;
- ambiente: região, host, runtime, cluster;
- mudança: versão, deploy, build, feature flag.

## Wide Events

Wide events preservam muitas dimensões no mesmo registro. Isso evita a necessidade de prever quais combinações serão úteis.

Use-os para:

- debugging de latência;
- regressões pós-deploy;
- problemas por cliente/tenant;
- comportamento de feature flags;
- incidentes distribuídos.

## Traces

Traces conectam eventos relacionados. Um trace útil mostra:

- caminho da request;
- serviços envolvidos;
- duração de cada etapa;
- erros e retries;
- chamadas externas;
- atributos de negócio relevantes.

Trace sem atributos é mapa sem legenda.

## OpenTelemetry

OpenTelemetry fornece padrão para:

- APIs e SDKs de instrumentação;
- propagação de contexto;
- traces, metrics e logs;
- collectors;
- exporters para backends diversos.

Use OTel para evitar acoplamento a vendor e criar consistência entre linguagens e serviços.

## Core Analysis Loop

1. Defina a anomalia.
2. Separe eventos afetados e não afetados.
3. Compare dimensões.
4. Identifique atributos com distribuição diferente.
5. Abra exemplos concretos.
6. Valide ou descarte hipótese.
7. Corrija sistema ou instrumentação.

## Observability-Driven Development

Instrumentação deve entrar cedo no ciclo de desenvolvimento. Ao criar uma feature, pergunte:

- como saberei se funciona em produção?
- como saberei se está lenta?
- como saberei quem foi afetado?
- como saberei se uma flag/deploy causou regressão?
- que campos faltariam em um incidente?
