# Padrões e Anti-Padrões

## Padrões

### Baseline Quantitativo

Defina métrica, carga, ambiente e distribuição antes de otimizar.

**Use quando:** qualquer conversa começa com “está lento”.

### Uma Variável Por Vez

Mude só uma coisa entre medições.

**Use quando:** tuning de GC, heap, pool, thread, container ou algoritmo.

### JFR Primeiro

Comece com Java Flight Recorder para obter visão ampla: CPU, allocation, GC, locks, IO, threads e eventos JVM.

**Use quando:** não há hipótese clara ou o problema está em produção.

### GC Log + Allocation Rate

Leia GC logs junto de métricas de allocation e live set.

**Use quando:** há pausas, OOM, throughput baixo ou custo de memória alto.

### Container-Aware Sizing

Dimensione heap e threads de acordo com limites reais do container.

**Use quando:** Java roda em Kubernetes ou ambiente com cgroups.

### JMH Para Microbenchmarks

Use JMH para warmup, forks, blackholes e medição estatística.

**Use quando:** quer comparar código pequeno, estrutura de dados, alocação ou algoritmo.

### Observability-Backed Performance

Use Micrometer, Prometheus, OpenTelemetry e logs estruturados para correlacionar performance com versão, tenant, endpoint, região e dependência.

**Use quando:** a dor acontece em produção ou em múltiplos serviços.

## Anti-Padrões

### Flag Cargo Cult

Copiar flags JVM de blog sem workload, versão e meta.

**Correção:** medir baseline, entender trade-off, testar em ambiente representativo.

### Benchmark de Laptop

Tirar conclusão sobre produção cloud a partir de máquina local sem isolamento.

**Correção:** reproduzir limites de CPU/memória/rede e carga.

### Média Como Verdade

Usar média para esconder cauda.

**Correção:** olhar p50, p95, p99, max, histograma e outliers.

### Microbenchmark Caseiro

Medir código Java sem JMH, warmup ou proteção contra otimização.

**Correção:** usar JMH e validar se o benchmark mede o que promete.

### GC Tuning Prematuro

Mexer em collector/heap antes de entender allocation e live set.

**Correção:** coletar GC logs, JFR, allocation profile e heap dump quando necessário.

### Autoscaling Como Cura Universal

Escalar instâncias para esconder gargalo de código, banco, lock ou dependência.

**Correção:** encontrar recurso limitante e testar degradação.

### Observabilidade Sem Ação

Expor métricas sem perguntas, SLOs ou runbooks.

**Correção:** conectar sinais a hipóteses, alertas e decisões operacionais.
