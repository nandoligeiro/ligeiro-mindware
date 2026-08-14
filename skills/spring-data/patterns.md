# Padrões e Anti-Padrões Spring Data

## Padrões

- **Repository per Aggregate**: repositório representa acesso a agregado/raiz.
- **Derived Query for Simple Intent**: use nomes derivados para queries óbvias.
- **Custom Repository for Complex Behavior**: mova lógica complexa para implementação customizada.
- **Projection for Read Model**: evite carregar entidade inteira quando precisa de visão parcial.
- **Auditing by Default**: padronize created/modified by/date.

## Anti-Padrões

- **Repository as God DAO**: dezenas de métodos sem coesão.
- **Method Name Novel**: query derivada ilegível.
- **JPA Everywhere**: usar JPA onde JDBC/documento seria mais simples.
- **Leaking Entities to API**: expor entidade persistente como contrato HTTP.
- **Reactive Costume**: `Mono`/`Flux` com acesso blocking por baixo.
