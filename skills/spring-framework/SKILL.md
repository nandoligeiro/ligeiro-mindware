---
name: spring-framework
description: "Cocérebro baseado na documentação oficial do Spring Framework 7.0.x: IoC container, dependency injection, bean lifecycle, resources, validation, conversion, SpEL, AOP, transactions, JDBC/R2DBC/ORM, Spring MVC, WebFlux, REST clients, testing, integration, scheduling, cache, observability e Kotlin. Use quando o usuário quiser projetar, implementar, testar, debugar ou revisar aplicações Java/Kotlin com Spring Framework."
metadata:
  short-description: Guia operacional do Spring Framework oficial
---

# Spring Framework — Ligeiro Mindware

Use este skill como parceiro para tomar decisões sobre Spring Framework, com base na documentação oficial do Spring Framework.

## Fontes Oficiais

- Página do projeto: `https://spring.io/projects/spring-framework/`
- Core: `https://docs.spring.io/spring-framework/reference/core.html`
- Data Access: `https://docs.spring.io/spring-framework/reference/data-access.html`
- Web MVC: `https://docs.spring.io/spring-framework/reference/web.html`
- WebFlux: `https://docs.spring.io/spring-framework/reference/web-reactive.html`
- Testing: `https://docs.spring.io/spring-framework/reference/testing.html`
- Integration: `https://docs.spring.io/spring-framework/reference/integration.html`
- Languages: `https://docs.spring.io/spring-framework/reference/languages.html`

## Postura

- Responda em português, mantendo nomes oficiais: `ApplicationContext`, `BeanFactory`, `@Bean`, `@Configuration`, `@Autowired`, `@Transactional`, `DispatcherServlet`, `WebClient`, `WebTestClient`, `MockMvc`.
- Diferencie Spring Framework de Spring Boot: Boot auto-configura; Framework fornece os blocos fundamentais.
- Prefira design explícito, testável e idiomático.
- Quando houver várias opções, explique trade-offs: anotação vs programação, MVC vs WebFlux, declarative vs programmatic transactions.
- Para detalhes versionados, recomende verificar a documentação oficial do projeto.

## Mapa Mental

Spring Framework é infraestrutura de aplicação: ele cuida do “plumbing” para que o código de negócio fique desacoplado de detalhes de construção, transação, web, recursos, integração e testes.

```text
Core container → cria e conecta objetos
AOP/proxies → aplica comportamento transversal
Transactions → define fronteiras de consistência
Web MVC/WebFlux → expõe e consome HTTP
Testing → carrega contexto e testa web/data/integration
Integration → tarefas, scheduling, cache, observability e messaging-adjacent
```

## Carregue Sob Demanda

- Core container, DI, beans e AOP: `chapters/core-container-aop.md`
- Data access e transações: `chapters/data-transactions.md`
- Web MVC e WebFlux: `chapters/web-mvc-webflux.md`
- Testing: `chapters/testing.md`
- Integration, cache, scheduling e observability: `chapters/integration-observability.md`
- Decisões rápidas: `cheatsheet.md`
- Padrões e anti-padrões: `patterns.md`
- Termos: `glossary.md`
- Fontes: `sources.md`

## Diagnóstico Inicial

Antes de sugerir uma solução Spring, pergunte:

1. É Spring Framework puro ou Spring Boot?
2. Qual versão de Spring/JDK/Jakarta?
3. O problema é wiring, lifecycle, transação, HTTP, reatividade, teste ou integração?
4. Há proxy envolvido (`@Transactional`, AOP, `@Async`, cache)?
5. O código é Servlet MVC, WebFlux/Reactor ou mistura?
6. A falha acontece em runtime, teste, startup ou AOT/native?
7. Qual fronteira de negócio deve ser transacional?
8. O teste precisa de contexto Spring ou pode ser unitário puro?

## Regras Práticas

- Constructor injection é o default saudável para dependências obrigatórias.
- Use `ApplicationContext` como container; evite service locator no código de domínio.
- `@Transactional` funciona via proxy; self-invocation é armadilha clássica.
- MVC é modelo Servlet/blocking; WebFlux é reativo/non-blocking e pede stack compatível.
- Não use WebFlux só “porque é moderno”; use quando o modelo reativo resolve um problema real.
- Teste unitário não precisa subir Spring.
- Teste de integração deve justificar o custo do contexto.
- AOP é ótimo para cross-cutting concerns; ruim para esconder regra de negócio.
