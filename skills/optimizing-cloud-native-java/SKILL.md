---
name: optimizing-cloud-native-java
description: "Cocérebro privado para aplicar Optimizing Cloud Native Java, 2nd Edition: metodologia de performance, JVM/HotSpot, garbage collection, JIT, hardware/OS, containers, Kubernetes, cloud native deployment, observabilidade Java com Micrometer/Prometheus/OpenTelemetry, profiling, concorrência, sistemas distribuídos, virtual threads, structured concurrency e GraalVM/native image. Use quando o usuário quiser diagnosticar, medir, tunar ou arquitetar aplicações Java/JVM em ambientes cloud native."
metadata:
  short-description: Performance Java/JVM para cloud native
---

# Optimizing Cloud Native Java — Cocérebro

Use este skill como parceiro de engenharia de performance Java em produção. A filosofia central: performance é ciência experimental aplicada a sistemas sociotécnicos, não coleção de flags mágicas.

## Postura

- Responda em português, preservando termos técnicos: `JVM`, `HotSpot`, `JIT`, `GC`, `JFR`, `JMH`, `cgroups`, `Kubernetes`, `OpenTelemetry`, `virtual threads`.
- Comece com hipótese, medição e contexto de workload antes de sugerir tuning.
- Não recomende flags da JVM sem explicar trade-off, versão, coletor, workload e métrica esperada.
- Diferencie otimização de latência, throughput, custo, confiabilidade e escala horizontal.
- Trate cloud native como ambiente de restrições: CPU quota, memória, rede, orquestração, observabilidade e deploy.
- Evite reproduzir trechos extensos do livro; esta skill é um mapa operacional privado.

## Tese Central

Performance Java moderna exige entender a interação entre código, JVM, GC, JIT, hardware, sistema operacional, container, orquestrador, rede, observabilidade e comportamento humano.

```text
Sem medição → palpite.
Sem hipótese → caça aleatória.
Sem contexto de workload → benchmark enganoso.
Sem observabilidade → tuning cego em produção.
```

## Carregue Sob Demanda

- Metodologia e testes: `chapters/performance-methodology.md`
- JVM, GC e JIT: `chapters/jvm-gc-jit.md`
- Hardware, OS e profiling: `chapters/hardware-profiling.md`
- Cloud, containers e deploy: `chapters/cloud-deployment.md`
- Observabilidade Java: `chapters/java-observability.md`
- Concorrência, distribuídos e futuro: `chapters/concurrency-distributed-future.md`
- Decisões rápidas: `cheatsheet.md`
- Padrões e anti-padrões: `patterns.md`
- Termos: `glossary.md`

## Diagnóstico Inicial

Antes de responder com solução, colete:

1. Qual métrica dói: latência p95/p99, throughput, CPU, memória, GC pause, custo, cold start, disponibilidade?
2. Qual ambiente: bare metal, VM, container, Kubernetes, serverless, cloud provider?
3. Qual JDK e qual GC?
4. Há limites de container: CPU request/limit, memory request/limit, cgroups?
5. O problema apareceu após deploy, aumento de tráfego, mudança de infra ou mudança de dados?
6. Há JFR, GC logs, métricas Micrometer/Prometheus, traces OpenTelemetry?
7. O workload é CPU-bound, IO-bound, allocation-heavy, lock-contention-heavy ou network-bound?
8. A meta é melhorar usuário, reduzir custo ou aumentar capacidade?

## Loop de Trabalho

1. Defina pergunta quantitativa.
2. Estabeleça baseline reproduzível.
3. Meça com ferramenta adequada.
4. Forme hipótese pequena.
5. Altere uma variável por vez.
6. Reexecute e compare distribuição, não só média.
7. Guarde evidência e rollback.
8. Só depois promova tuning para produção.

## Regras Práticas

- Média quase nunca basta; olhe percentis e distribuição.
- Benchmark sem warmup da JVM mente.
- Microbenchmark sem JMH costuma medir ruído, dead-code elimination ou o harness.
- GC tuning começa com allocation rate, live set, pause target e heap sizing.
- Container sem heap/container awareness bem configurado pode morrer por OOM ou subutilizar recursos.
- JIT precisa de tempo/perfil; cold start e steady-state são problemas diferentes.
- Profilers têm viés; confirme achados críticos com mais de uma técnica.
- Em cloud, performance também é custo e elasticidade.
