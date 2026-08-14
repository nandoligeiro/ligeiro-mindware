# Relacional: JPA, JDBC e R2DBC

## Spring Data JPA

Use quando precisa de JPA, persistence context, relações ORM, specifications, locking e integração com transações.

Cuidados:

- N+1 queries;
- lazy loading;
- fronteira transacional;
- entidade vazando para API;
- batch/fetch strategy.

## Spring Data JDBC

Use quando quer mapeamento relacional mais direto, agregado mais explícito e menos magia ORM.

## Spring Data R2DBC

Use com stack reativa real e driver R2DBC. Não misture com JDBC blocking no mesmo caminho quente.
