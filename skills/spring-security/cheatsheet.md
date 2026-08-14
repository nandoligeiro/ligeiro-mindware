# Spring Security Cheatsheet

| Necessidade | Use |
|---|---|
| Configurar segurança web | `SecurityFilterChain` |
| Autenticação usuário/senha | `UserDetailsService`, `AuthenticationProvider`, `PasswordEncoder` |
| Proteger endpoint | `authorizeHttpRequests` |
| Proteger método | method security |
| API com JWT | OAuth2 Resource Server |
| Login via Google/IdP | OAuth2/OIDC Login |
| Cliente chamando APIs OAuth2 | OAuth2 Client |
| SAML enterprise | SAML2 Login |
| Testar MVC seguro | spring-security-test + MockMvc |
| Testar WebFlux seguro | WebTestClient support |

## CSRF

- Browser + cookies/session: normalmente mantenha.
- API stateless com bearer token: geralmente pode desabilitar com cuidado.
- Teste endpoints mutáveis com token CSRF quando aplicável.

## Authorization

- Deny by default.
- Regras específicas antes de genéricas.
- Separe autenticação de autorização.
- Audite roles/authorities/claims.
