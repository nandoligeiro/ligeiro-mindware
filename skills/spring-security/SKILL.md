---
name: spring-security
description: "Cocérebro baseado na documentação oficial Spring Security 7.1.x: authentication, authorization, SecurityFilterChain, servlet security, reactive security, password storage, CSRF, headers, session management, method security, OAuth2/OIDC login, OAuth2 client, resource server JWT/opaque token, SAML2, testing com MockMvc/WebTestClient e integração Spring."
metadata:
  short-description: Spring Security operacional
---

# Spring Security — Ligeiro Mindware

Use esta skill para projetar, implementar, revisar e testar segurança em aplicações Spring.

## Fontes Oficiais

- `https://spring.io/projects/spring-security/`
- `https://docs.spring.io/spring-security/reference/`

## Como Pensar

Spring Security protege aplicações por filtros/interceptores e componentes de autenticação/autorização. A pergunta central é: “quem é o principal, como ele foi autenticado, e o que ele pode acessar?”

## Carregue Sob Demanda

- Arquitetura, autenticação e autorização: `chapters/auth-authorization.md`
- Servlet, reactive, OAuth2 e SAML: `chapters/web-oauth2-saml.md`
- Exploit protection, testing e integrações: `chapters/testing-hardening.md`
- Decisões rápidas: `cheatsheet.md`
- Padrões e anti-padrões: `patterns.md`
- Termos: `glossary.md`

## Diagnóstico Inicial

1. É aplicação Servlet/MVC ou Reactive/WebFlux?
2. É sessão, stateless JWT, OAuth2 login, resource server, SAML ou basic/form?
3. Quem emite identidade: app, IdP, authorization server?
4. Autorização é por URL, método, domínio ou combinação?
5. CSRF deve estar ligado? Há browser/session/cookie?
6. Há CORS/proxy/gateway?
7. Como testar login, CSRF, JWT e roles?

## Regras Práticas

- Configure `SecurityFilterChain` explicitamente.
- Não desabilite CSRF sem entender browser/cookies/session.
- Hash de senha precisa `PasswordEncoder` adequado, nunca texto puro.
- Authorization rules devem ir do específico para o geral.
- Method security protege casos de uso; URL security protege entrada HTTP.
- Resource server valida token; não “confia” em claim sem regra.
