# Spring MVC e WebFlux

## Fontes

- `https://docs.spring.io/spring-framework/reference/web.html`
- `https://docs.spring.io/spring-framework/reference/web-reactive.html`

## Spring MVC

Spring MVC é baseado no Servlet stack. `DispatcherServlet` recebe a request, encontra handler/controller, converte argumentos, chama o método e resolve response/view.

Use MVC quando:

- stack é blocking;
- usa Servlet container;
- banco/drivers são blocking;
- simplicidade operacional é prioridade.

## WebFlux

WebFlux é stack reativa. Trabalha com `Mono`, `Flux`, backpressure e runtimes non-blocking.

Use WebFlux quando:

- há alta concorrência IO-bound;
- dependências são reativas/non-blocking;
- precisa streaming;
- o time domina Reactor.

## Controllers

Pontos importantes:

- request mapping;
- method arguments;
- return values;
- validation;
- exception handling;
- content negotiation;
- CORS;
- message converters/codecs.

## Clients

- `RestClient`/clientes blocking para MVC.
- `WebClient` para stack reativa e chamadas non-blocking.

## Erros HTTP

Centralize tratamento com `@ControllerAdvice`, error responses e mapeamento claro de exceções de domínio/aplicação para status HTTP.
