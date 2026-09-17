# Software Supply Chain Security

## Mental model

A supply chain de software conecta fonte, dependências, build, artifact store e deploy. O objetivo é conseguir responder e verificar:

```text
what source -> what change -> what builder -> what inputs -> what artifact -> what identity -> what consumer policy
```

## SBOM

SBOM ajuda a responder "o que existe dentro deste software?". É útil para inventário, vulnerabilidades e impacto de incidentes em dependências.

SBOM não prova:

- que o artefato veio do repositório esperado;
- que o build não foi adulterado;
- que a dependência listada é autêntntica;
- que o consumidor verificou integridade.

## Provenance

Provenance descreve como um artefato foi produzido, incluindo origem, processo e inputs. O valor aumenta quando é gerada automaticamente por um ambiente de build confiável e verificada downstream.

A especificação SLSA 1.2 organiza garantias incrementais de supply chain e define provenance como informação verificável para rastrear artefatos até sua origem/build.

## Signing

Assinar liga integridade do artefato a uma chave ou identidade. A assinatura precisa ser acompanhada de uma expectativa verificável de quem deveria assinar.

Exemplo de abordagem moderna: assinatura baseada em identidade com certificado curto e transparency log, evitando chaves permanentes quando apropriado.

## Consumer verification

O controle acontece no consumidor:

```text
artifact digest
+ signature
+ expected identity
+ provenance policy
= allow / deny
```

Sem enforcement, os metadados existem mas não protegem o deploy.

## CI/CD

Pipelines devem ser tratados como infraestrutura privilegiada:

- princípio de menor privilégio;
- credenciais efêmeras;
- isolamento entre PR/untrusted code e release;
- pinning/verificação de actions/plugins;
- proteção de branch e aprovação de mudanças sensíveis;
- ambiente de build reproduzível/hardened quando necessário;
- registry imutável ou promotion por digest.

## Dependencies

Avalie:

- origem e mantenedor;
- atividade/manutenção;
- CVEs e advisories;
- transitivas;
- política de atualização;
- possibilidade de typosquatting/dependency confusion;
- package source/registry esperado.

## Referências públicas

- OWASP ASVS 5.0.0: requisitos técnicos verificáveis para aplicações.
- NIST SSDF: conjunto de práticas de desenvolvimento seguro integráveis a diferentes SDLCs.
- SLSA 1.2: níveis/tracks, attestations e provenance para supply chain.
- Sigstore: assinatura baseada em identidade, certificados efêmeros e transparency log como implementação de referência.
