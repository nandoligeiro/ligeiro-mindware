# Observabilidade Java

## Capítulos Cobertos

- Cap. 10 — Introduction to Observability
- Cap. 11 — Implementing Observability in Java

## Ideia-Mãe

Observabilidade para Java deve conectar sinais da aplicação, da JVM e do ambiente cloud. Não basta saber que “CPU subiu”; é preciso ligar isso a endpoint, versão, tenant, GC, trace e experiência.

## Três Pilares na Prática

- **Metrics**: tendências, alertas e visão agregada.
- **Logs**: eventos textuais/estruturados e contexto.
- **Traces**: causalidade entre serviços e operações.

Use os três como um workflow integrado.

## Micrometer

Micrometer fornece fachada para métricas Java:

- timers;
- counters;
- gauges;
- registries;
- integração com Prometheus e vendors.

Boa para métricas de aplicação e JVM.

## Prometheus

Prometheus é forte em scrape, séries temporais e alertas, mas não substitui tracing ou eventos ricos.

Use para:

- métricas JVM;
- métricas HTTP;
- RED/USE;
- SLOs básicos;
- alertas agregados.

## OpenTelemetry

OTel ajuda a padronizar:

- traces;
- métricas;
- logs;
- context propagation;
- exporters;
- collectors.

Use para reduzir lock-in e correlacionar serviços.

## Java Runtime Signals

Monitore:

- GC pauses;
- heap/non-heap;
- allocation;
- threads;
- classloading;
- JIT/code cache;
- CPU;
- file descriptors;
- connection pools.

## Instrumentação Boa

Inclua atributos:

- `service.name`, `service.version`;
- endpoint/operação;
- status/erro;
- duração;
- tenant/user quando apropriado;
- pod/container/node;
- feature flag/deploy id;
- trace/span id.
