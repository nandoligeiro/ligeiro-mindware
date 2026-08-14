# Hardware, OS e Profiling

## Capítulos Cobertos

- Cap. 7 — Hardware and Operating Systems
- Cap. 12 — Profiling

## Mechanical Sympathy

Java abstrai hardware, mas performance não desaparece. CPU, caches, memória, NUMA, scheduler, IO e syscalls ainda moldam o comportamento da JVM.

## Hardware/OS Importam Porque

- cache miss custa caro;
- concorrência pode causar contenção;
- contexto de thread tem custo;
- CPU quota em container muda scheduling;
- IO e rede introduzem latência variável;
- memória e GC interagem com pressão do sistema.

## Profiling

Profiling deve responder “onde o tempo/memória está indo?”.

Tipos:

- execution profiling;
- allocation profiling;
- lock/contention profiling;
- wall-clock profiling;
- event-based profiling com JFR.

## Ferramentas

- **JFR/JMC**: visão ampla da JVM com baixo overhead.
- **VisualVM**: inspeção e profiling visual.
- **JMH**: microbenchmarks confiáveis.
- **GC logs**: análise de pausas e ciclos.
- **Heap dump**: vazamentos e retenção.
- **Sistema operacional**: CPU, memória, IO, rede, scheduler.

## Cuidado Com Viés

Profilers podem distorcer:

- safepoint bias;
- overhead de instrumentação;
- amostragem insuficiente;
- workload não representativo;
- interpretação por expectativa.

Valide achados importantes com outra ferramenta ou outro tipo de medição.
