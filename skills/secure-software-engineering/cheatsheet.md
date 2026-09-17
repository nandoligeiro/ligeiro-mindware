# Secure Software Engineering — Cheatsheet

## Perguntas que destravam a análise

- Qual asset está em risco?
- Quem controla cada entrada?
- Onde mudamos de trust boundary?
- Qual identidade executa a ação?
- Qual privilégio é realmente necessário?
- Como esse controle será verificado?
- O que acontece se a dependência/build/pipeline for comprometido?

## Threat -> Control -> Evidence

| Threat | Controle típico | Evidência |
| --- | --- | --- |
| spoofing | autenticação forte, mTLS/OIDC | teste de identidade inválida/expirada |
| broken access control | autorização por recurso + least privilege | testes negativos de acesso |
| secret leakage | secret store + rotação + redaction | secret scanning + rotação comprovada |
| dependency compromise | pinning, policy, provenance | verificação de origem + SBOM |
| artifact tampering | assinatura + provenance + verification | policy no deploy/consumer |
| CI credential abuse | tokens efêmeros + escopo mínimo | policy/permissions auditáveis |
| injection | validação contextual/parametrização | testes de abuso + ASVS |

## Regras rápidas

- **Authenticate once, authorize every sensitive operation.**
- Cliente nunca é fronteira de segurança confiável.
- Um segredo vazado deve ser rotacionado; esconder não corrige.
- SBOM = inventário, não integridade.
- Provenance sem verificação no consumo é evidência não aplicada.
- Assinatura sem política de identidade esperada pode validar o atacante errado.
- Scanner sem teste de controle não fecha risco.
- Dependência transitiva também faz parte da supply chain.

## Supply chain mínima

```text
source
  -> reviewed change
  -> isolated build
  -> provenance
  -> signed artifact
  -> immutable registry
  -> verification policy
  -> deployment
```

## Definition of Done para controle crítico

Um controle só está completo quando há:

1. ameaça definida;
2. controle implementado;
3. teste/policy verificável;
4. telemetria para falha ou abuso relevante;
5. owner e processo de correção/rotação quando aplicável.
