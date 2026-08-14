# Data Access e Transações

## Fontes

- `https://docs.spring.io/spring-framework/reference/data-access.html`

## Transações

Spring unifica transações via `PlatformTransactionManager`. O modelo declarativo com `@Transactional` é o caminho comum para serviços de aplicação.

Perguntas-chave:

- Qual unidade de trabalho?
- Qual isolamento?
- Qual propagação?
- Quais exceções causam rollback?
- O método é chamado via proxy Spring?

## Declarative vs Programmatic

Use declarativo quando a fronteira é clara e convencional. Use `TransactionTemplate` quando fluxo, rollback ou escopo precisam controle explícito.

## JDBC

Spring JDBC reduz boilerplate:

- conexão;
- statements;
- exception translation;
- batch;
- data source;
- resource cleanup.

## ORM/JPA

Spring integra ORM com transações, exception translation e lifecycle. Evite deixar transação aberta sem necessidade e cuidado com lazy loading fora da fronteira transacional.

## R2DBC

R2DBC é para acesso relacional reativo. Use quando a aplicação é reativa de ponta a ponta; não misture por estética com código bloqueante.

## Eventos Transacionais

Use eventos bound to transaction quando uma reação deve acontecer após commit ou em outra fase da transação.
