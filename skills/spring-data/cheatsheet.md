# Spring Data Cheatsheet

| Necessidade | Use |
|---|---|
| CRUD comum | Repository interface |
| Query simples | Derived query method |
| Query complexa | `@Query`, Specification, Querydsl ou custom repository |
| Campos parciais | Projection |
| Created/modified metadata | Auditing |
| Lógica customizada | Custom repository implementation |
| Eventos de aggregate | Domain events from aggregate roots |
| Blocking relational ORM | Spring Data JPA |
| SQL direto/agregado simples | Spring Data JDBC |
| Relacional reativo | Spring Data R2DBC |
| Documento MongoDB | Spring Data MongoDB |

## Sinais de Alerta

- Nome de método repository gigante.
- Lazy loading explodindo fora da transação.
- Entidade JPA usada como DTO de API.
- Reativo por cima de driver blocking.
- Ignorar índices e plano de query.
