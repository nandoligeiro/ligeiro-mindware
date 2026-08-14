# Testing e Hardening

## Proteções

Spring Security cobre CSRF, headers, session fixation, HTTP firewall e integrações com MVC/WebFlux.

## Testing

Teste:

- usuário autenticado/anônimo;
- roles/authorities;
- CSRF;
- OAuth2/JWT claims;
- método protegido;
- acesso negado.

Use `spring-security-test` com MockMvc/WebTestClient.
