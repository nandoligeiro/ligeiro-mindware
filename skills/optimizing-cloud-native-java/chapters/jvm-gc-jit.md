# JVM, Garbage Collection e JIT

## Capítulos Cobertos

- Cap. 3 — Overview of the JVM
- Cap. 4 — Understanding Garbage Collection
- Cap. 5 — Advanced Garbage Collection
- Cap. 6 — Code Execution on the JVM

## JVM Mental Model

HotSpot executa bytecode em uma máquina virtual gerenciada. Ela controla classloading, interpretação, compilação dinâmica, gerenciamento de memória, threads e várias otimizações invisíveis ao código-fonte.

## Classloading e Bytecode

Para performance, entender bytecode ajuda a explicar:

- custo de abstrações;
- dispatch virtual;
- inlining;
- lambdas e invokedynamic;
- reflection/method handles;
- compatibilidade entre código e runtime.

## Garbage Collection

GC troca controle manual de memória por gerenciamento automático. O custo aparece como CPU, pausas, throughput reduzido e uso de memória.

Conceitos-chave:

- mark-and-sweep;
- stop-the-world;
- moving/compacting/evacuating;
- gerações;
- young/old regions;
- live set;
- allocation rate;
- premature promotion.

## Coletores

- **G1**: bom default geral; trabalha com regiões e metas de pausa.
- **ZGC**: baixa pausa, adequado para heaps grandes e latência sensível.
- **Shenandoah**: baixa pausa com coleta concorrente.
- **Parallel**: throughput em workloads específicos.
- **Serial**: ambientes pequenos/simples.

Escolha coletor por meta e workload, não por moda.

## JIT e Code Execution

HotSpot observa código quente e compila para código nativo. Isso cria diferença entre:

- startup;
- warmup;
- steady-state;
- deoptimization;
- tiered compilation;
- code cache.

## Perguntas Para Tuning

1. O problema é pausa, throughput, memória ou custo?
2. Qual é allocation rate?
3. Qual é live set?
4. O heap está grande/pequeno para o limite do container?
5. Há humongous allocations?
6. Há promoção prematura?
7. A aplicação está em warmup ou steady-state?
