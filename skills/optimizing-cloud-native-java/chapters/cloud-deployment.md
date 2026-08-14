# Cloud, Containers e Deployment

## Capítulos Cobertos

- Cap. 8 — Components of the Cloud Stack
- Cap. 9 — Deploying Java in the Cloud

## Cloud Native Performance

Cloud native adiciona metas e restrições além da performance clássica:

- custo;
- confiabilidade;
- elasticidade;
- escala horizontal;
- isolamento;
- tempo de deploy;
- observabilidade operacional.

## Componentes do Stack

Entenda:

- containers;
- Kubernetes;
- service mesh;
- ingress;
- config/secrets;
- autoscaling;
- Prometheus/OpenTelemetry;
- imagens e registries;
- CI/CD.

## Java em Containers

Pontos críticos:

- limites de CPU e memória;
- ergonomia da JVM com cgroups;
- heap sizing;
- metas de GC;
- startup/warmup;
- readiness/liveness probes;
- shutdown gracioso;
- thread pools vs CPU quota.

## Deployment Patterns

Use padrões para reduzir risco:

- rolling deployment;
- blue/green;
- canary;
- feature flags;
- progressive delivery;
- rollback seguro.

## Checklist Kubernetes

- Requests e limits estão coerentes?
- JVM vê limite correto de memória?
- Heap deixa espaço para metaspace, stacks, direct buffers e native memory?
- Probes medem prontidão real?
- HPA escala com métrica relevante?
- Há traces/métricas por versão e pod?
- Deploy considera warmup?
