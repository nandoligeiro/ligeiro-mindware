# Java Performance Cheatsheet

## Pergunta Antes da Ferramenta

| Dor | Comece por |
|---|---|
| Latência alta | percentis, traces, profiling, GC pauses |
| Throughput baixo | CPU, locks, IO, pool sizing, JIT warmup |
| Alto uso de CPU | profiler de execução, flame graph, algoritmo |
| Memória/OOM | heap dump, allocation profiling, GC logs, live set |
| Pausas | GC logs/JFR, collector, heap, allocation rate |
| Cold start | startup path, classloading, JIT, CDS, native image |
| Custo cloud | requests/limits, autoscaling, allocation, workload shape |

## Tipos de Teste

| Tipo | Pergunta |
|---|---|
| Latency test | Quanto tempo uma transação leva? |
| Throughput test | Quantas operações por unidade de tempo? |
| Stress test | Onde o sistema quebra? |
| Load test | Aguenta a carga esperada? |
| Endurance test | Degrada com o tempo? |
| Capacity planning | Que recurso limita crescimento? |
| Degradation test | Como se comporta parcialmente falho? |

## JVM/GC

- Verifique JDK, GC, heap, metas de pausa e container limits.
- Coletores comuns: G1, ZGC, Shenandoah, Parallel/Serial em casos específicos.
- Sintomas importantes: allocation rate alto, premature promotion, humongous objects, long pauses, high live set.
- GC não corrige vazamento lógico; heap dump e dominator tree ajudam.

## JIT

- HotSpot interpreta primeiro e compila código quente depois.
- Warmup muda resultados; benchmark curto é suspeito.
- Tiered compilation melhora equilíbrio entre startup e steady-state.
- Code cache cheio ou deoptimization pode afetar performance.

## Containers/Kubernetes

- Confirme `requests` e `limits`.
- CPU quota pode distorcer latência e pausas.
- Memória do container não é memória da máquina.
- Configure heap em relação ao limite real, não ao host.
- Liveness/readiness ruins causam restart loops e incidentes artificiais.

## Observabilidade Java

- Micrometer: métricas de app/JVM para múltiplos registries.
- Prometheus: scrape e query de métricas.
- OpenTelemetry: traces, métricas, logs e propagação de contexto.
- JFR: eventos de baixo overhead para runtime/JVM.
- JMX: exposição/controle histórico de métricas JVM.

## Profiling

- Use JFR/JMC para visão ampla JVM.
- Use profiler de CPU quando CPU-bound.
- Use allocation profiling para pressão no GC.
- Use JMH para microbenchmarks.
- Desconfie de profiler que só amostra em safepoints.
