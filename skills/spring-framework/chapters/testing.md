# Testing

## Fontes

- `https://docs.spring.io/spring-framework/reference/testing.html`

## Estratégia

Nem todo teste precisa de Spring. Comece pelo menor escopo que prova o comportamento.

Camadas:

- unitário puro;
- teste com mocks;
- Spring TestContext;
- `MockMvc`;
- `WebTestClient`;
- testes de banco com transações/SQL;
- end-to-end.

## TestContext Framework

Fornece:

- carregamento e cache de contexto;
- dependency injection em testes;
- profiles e propriedades de teste;
- transaction management;
- SQL scripts;
- eventos de teste.

## MockMvc

Use para testar Spring MVC sem servidor real:

- request mapping;
- validação;
- serialização;
- filtros;
- controller advice;
- responses.

## WebTestClient

Use para WebFlux e também cenários HTTP testáveis. Bom para APIs reativas e contratos de endpoint.

## Armadilhas

- Contexto demais deixa suite lenta.
- `@DirtiesContext` em excesso destrói cache.
- Teste de controller não deve virar teste de banco.
- Mockar Spring demais pode esconder wiring quebrado.
