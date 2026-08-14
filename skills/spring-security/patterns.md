# Padrões e Anti-Padrões Spring Security

## Padrões

- **Explicit SecurityFilterChain**: declare regras de forma legível.
- **Deny By Default**: libere apenas o necessário.
- **Method Security for Use Cases**: proteja operações de negócio sensíveis.
- **Resource Server Boundary**: valide JWT/opaque token na borda da API.
- **Security Tests as Contract**: teste acesso permitido, negado, CSRF e claims.

## Anti-Padrões

- **Disable CSRF Everywhere**: desabilitar por frustração.
- **permitAll Acidental**: regra genérica antes da específica.
- **Role String Soup**: roles espalhadas como strings sem modelo.
- **Token Blind Trust**: aceitar claims sem issuer/audience/assinatura/escopo.
- **Security Só no Controller**: serviços internos ficam desprotegidos.
