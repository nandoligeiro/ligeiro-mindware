# Concorrência, Distribuídos e Futuro

## Capítulos Cobertos

- Cap. 13 — Concurrent Performance Techniques
- Cap. 14 — Distributed Systems Techniques and Patterns
- Cap. 15 — Modern Performance and The Future

## Concorrência

Concorrência melhora performance apenas quando há paralelismo útil e gargalo compatível.

Use Amdahl’s Law para lembrar: a parte serial limita o ganho total.

Áreas críticas:

- locks;
- atomics;
- volatile;
- memory model;
- false sharing;
- thread pools;
- contention;
- coordination cost.

## Java Memory Model

O JMM define visibilidade e ordenação entre threads. Não “role seu próprio atomic”; use bibliotecas padrão.

## Sistemas Distribuídos

Cloud native amplia efeitos das falácias distribuídas:

- rede não é confiável;
- latência não é zero;
- largura de banda não é infinita;
- topologia muda;
- há múltiplos administradores e falhas parciais.

Técnicas importantes:

- retries com backoff;
- timeouts;
- circuit breakers;
- idempotência;
- particionamento;
- replicação;
- consenso;
- write-ahead logs;
- clocks/IDs.

## Virtual Threads

Virtual threads reduzem custo de concorrência IO-bound, mas não tornam CPU infinita.

Boas para:

- muitas operações bloqueantes;
- simplificar código assíncrono;
- serviços que aguardam rede/IO.

Cuidado com:

- pinning;
- pools antigos;
- CPU-bound work;
- bibliotecas bloqueantes incompatíveis;
- observabilidade de grandes quantidades de threads.

## Structured Concurrency e Scoped Values

Structured concurrency trata subtarefas relacionadas como unidade de trabalho, melhorando cancelamento, erro e legibilidade.

Scoped values oferecem alternativa para contexto imutável associado a execução, com afinidade a virtual threads.

## GraalVM Native Image

Native image pode melhorar startup e footprint, mas muda trade-offs:

- build mais complexo;
- reflexão/configuração;
- menor warmup;
- possível diferença de peak throughput;
- compatibilidade de bibliotecas.

Use quando cold start e memória importam muito.
