# Servlet, Reactive, OAuth2 e SAML

## Servlet vs Reactive

Servlet usa filter chain; Reactive usa WebFlux security em `ServerWebExchange`.

Não misture modelos sem necessidade.

## OAuth2/OIDC

- Login: usuário autentica via IdP.
- Client: aplicação obtém token para chamar outra API.
- Resource Server: API valida bearer token JWT ou opaque.

## SAML2

Use para SSO enterprise onde SAML é requisito organizacional. Atenção a metadata, certificados, clocks e logout.
