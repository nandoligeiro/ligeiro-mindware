# Authentication e Authorization

## Authentication

Autenticação estabelece identidade. Pode vir de form login, basic, LDAP, OAuth2/OIDC, SAML, JWT, X.509, pre-auth etc.

Componentes comuns:

- `Authentication`;
- `AuthenticationManager`;
- `AuthenticationProvider`;
- `UserDetailsService`;
- `PasswordEncoder`.

## Authorization

Autorização decide acesso por URL, método, objeto de domínio ou claims.

Use:

- regras HTTP para borda web;
- method security para casos de uso;
- ACL/domain security quando objeto importa.
