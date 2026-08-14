# Core Container e AOP

## Fontes

- `https://docs.spring.io/spring-framework/reference/core.html`

## Core Container

O container IoC cria e conecta objetos. O `ApplicationContext` é o ponto central para configuração, lifecycle, eventos, recursos, i18n, ambiente e beans.

Use Spring para:

- compor objetos;
- externalizar configuração;
- gerenciar lifecycle;
- conectar infraestrutura a aplicação;
- aplicar cross-cutting concerns.

## Dependency Injection

Prefira constructor injection para dependências obrigatórias. Use qualifiers quando houver ambiguidade e `ObjectProvider` para resolução tardia/opcional.

## Bean Lifecycle

Preste atenção em:

- criação;
- dependency injection;
- post-processors;
- callbacks de inicialização/destruição;
- scopes;
- lazy initialization.

## Java Configuration

`@Configuration` + `@Bean` permite declarar wiring explicitamente em Java. Use para integração com bibliotecas externas, infraestrutura e beans que não são seus componentes escaneados.

## AOP

Spring AOP é baseado em proxies e atende bem cross-cutting concerns:

- transações;
- logging/auditing;
- security checks;
- metrics;
- cache;
- retries.

Limitações típicas:

- self-invocation;
- métodos não interceptáveis;
- diferença entre proxy JDK e CGLIB;
- join points limitados comparados ao AspectJ completo.
