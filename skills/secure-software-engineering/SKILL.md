---
name: secure-software-engineering
description: Use esta skill para projetar, revisar ou endurecer software com foco em secure-by-design, threat modeling, controles verificáveis, proteção de segredos, autorização, criptografia aplicada, dependências, CI/CD e software supply chain. Ative quando a tarefa exigir transformar riscos em controles e evidências. Não use para dúvidas puramente de configuração do Spring Security ou para compliance jurídico sem contexto técnico.
---

# Secure Software Engineering

## Objetivo

Ajudar a tomar decisões de segurança como parte da engenharia de software, conectando ameaça, controle e evidência verificável ao longo do ciclo de desenvolvimento.

## Princípio central

Segurança não é uma lista de scanners nem um checklist de OWASP. Para cada risco relevante, determine:

```text
asset -> threat -> attack path -> control -> verification -> residual risk
```

Prefira controles preventivos e verificáveis. Use detecção e resposta como camadas complementares, não substitutos de design seguro.

## Quando ativar

Ative para tarefas como:

- threat modeling de serviços, APIs, jobs, pipelines e integrações;
- revisão de autenticação, autorização, privilégio e trust boundaries;
- proteção de segredos, chaves e dados sensíveis;
- requisitos de segurança testáveis;
- dependências vulneráveis e software supply chain;
- SBOM, provenance, artifact signing e verificação de origem;
- gates de segurança no CI/CD;
- desenho de controles contra abuso, tampering e privilege escalation;
- revisão de exposição de endpoints, storage, filas ou ferramentas internas.

## Quando não ativar

Não use esta skill quando:

- a pergunta é somente sintaxe/configuração de Spring Security;
- o problema é apenas infraestrutura de rede sem implicação de aplicação;
- o usuário pede interpretação jurídica/compliance sem decisão técnica;
- a tarefa é somente resposta a incidente já em andamento sem necessidade de redesign.

## Fluxo de decisão

1. **Defina o asset e o impacto.** Identifique dados, operações, credenciais, artefatos ou privilégios que precisam ser protegidos.
2. **Mapeie trust boundaries.** Marque entradas externas, mudanças de identidade, saltos entre serviços, CI, registry, secrets store e runtime.
3. **Modele ameaças realistas.** Considere spoofing, tampering, elevation of privilege, data exposure, dependency compromise, secret leakage e abuse paths.
4. **Escolha controles próximos da causa.** Prefira least privilege, validação server-side, autorização por recurso, segregação, assinatura/verificação, provenance, isolamento e imutabilidade.
5. **Defina evidência.** Cada controle importante deve ter uma forma de teste, policy, attestação, log ou verificação automática.
6. **Avalie residual risk.** Registre o que permanece possível e quais sinais permitem detectar abuso.
7. **Evite teatro de segurança.** Não trate scanner, WAF, SAST, Top 10 ou checklist como prova de segurança por si só.

## Heurísticas essenciais

### Threat -> control -> evidence

Não recomende um controle sem explicar qual ameaça ele reduz e como verificar que funciona.

### Autorização

Autenticação responde quem é; autorização responde o que pode fazer. Verifique autorização no lado servidor, por operação e por recurso sensível.

### Segredos

Segredo em código, imagem, log, artifact, variável exposta em build ou histórico Git deve ser tratado como comprometido. Rotação e revogação fazem parte da correção.

### Criptografia

Não invente primitivas, formatos ou protocolos. Prefira bibliotecas e protocolos consolidados. Criptografia sem gestão de chaves e limites de confiança explícitos é incompleta.

### Dependências

Uma dependência é código executado com seus privilégios. Analise origem, versionamento, manutenção, vulnerabilidades conhecidas, transitive dependencies e capacidade de atualização.

### Supply chain

Para artefatos de produção, busque responder:

```text
qual fonte? -> qual build? -> quais inputs? -> quem/que identidade produziu? -> artefato foi alterado? -> consumidor verifica?
```

SBOM melhora inventário, mas não prova integridade. Provenance descreve como o artefato foi produzido; assinatura e verificação ligam integridade a uma identidade ou processo confiável.

### CI/CD

Pipelines são sistemas privilegiados. Reduza permissões, use credenciais efêmeras quando possível, proteja ambientes e aprovações, fixe dependências/actions por referência confiável e separe build de deploy.

## Saída esperada

Quando analisar um problema de segurança, produza preferencialmente:

1. assets e trust boundaries;
2. ameaças principais;
3. controles recomendados;
4. evidência/verificação por controle;
5. residual risks;
6. prioridades por impacto e explorabilidade.

## Anti-padrões

- OWASP Top 10 usado como checklist de arquitetura;
- autenticação forte com autorização fraca;
- segredo "oculto" em variável, YAML, imagem ou log;
- scanner aprovado tratado como prova de ausência de vulnerabilidade;
- dependências atualizadas sem verificar origem ou build;
- SBOM tratada como assinatura/provenance;
- artefato assinado mas nunca verificado no consumo;
- pipeline com token permanente e privilégio amplo;
- controles somente no cliente;
- "criptografia própria" para resolver requisito sensível.

## Referências internas

Consulte sob demanda:

- `references/threat-modeling.md`
- `references/supply-chain.md`
- `patterns.md`
- `cheatsheet.md`

## Base de referência pública

Use como orientação, sem transformar a skill em cópia normativa:

- OWASP ASVS 5.0.0 para requisitos verificáveis de segurança de aplicação;
- NIST SSDF para práticas de desenvolvimento seguro integráveis ao SDLC;
- SLSA 1.2 para supply-chain integrity e provenance;
- Sigstore como exemplo de assinatura e verificação baseada em identidade e transparency log.
