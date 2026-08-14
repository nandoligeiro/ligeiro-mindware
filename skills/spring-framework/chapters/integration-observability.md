# Integration, Cache, Scheduling e Observability

## Fontes

- `https://docs.spring.io/spring-framework/reference/integration.html`
- `https://docs.spring.io/spring-framework/reference/core.html`

## Integration

A área de integration cobre suporte a:

- remoting;
- JMS/JCA/JMX;
- email;
- tasks;
- scheduling;
- cache;
- observability.

## Tasks e Scheduling

Use abstrações de task execution/scheduling para separar política de execução do código de negócio.

Cuidados:

- pool sizing;
- tratamento de erro;
- idempotência;
- concorrência;
- shutdown gracioso.

## Cache

Cache é cross-cutting concern. Use anotações/abstrações quando:

- chave é clara;
- invalidação é compreendida;
- consistência eventual é aceitável;
- métrica de hit/miss existe.

## Observability

Spring Framework fornece integração para observabilidade em pontos de infraestrutura. Conecte com Micrometer/OpenTelemetry no ecossistema Spring quando estiver usando Boot ou stack observável.

## Kotlin e Linguagens

Spring documenta suporte a Kotlin e outras linguagens. Em Kotlin, atenção a null-safety, classes/métodos finais e idiomatismos que afetam proxies e configuração.
