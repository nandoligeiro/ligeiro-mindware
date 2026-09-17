---
name: platform-engineering
description: "Ligeiro Mindware para projetar e evoluir plataformas internas como produto: self-service, golden paths, paved roads, abstrações, guardrails, templates, políticas, observabilidade da plataforma, ownership e redução de carga cognitiva. Use quando múltiplos times dependem de capacidades comuns de build, runtime, deploy, segurança ou operação."
metadata:
  short-description: Plataforma interna como produto e self-service
---

# Platform Engineering

Projete a plataforma como **produto para desenvolvedores**, não como coleção de scripts ou portal.

## Ativação
Use esta skill quando houver:
- múltiplos times repetindo setup/infra/CI/runtime;
- necessidade de self-service com guardrails;
- golden paths/paved roads;
- templates, scaffolds, service catalogs ou plataforma interna;
- abstração sobre cloud/Kubernetes/CI/CD;
- discussão de developer experience, cognitive load ou platform adoption.

Não ative para:
- comando isolado de kubectl/Helm;
- configuração pontual de um serviço sem capacidade compartilhada;
- troubleshooting puramente de aplicação.

## Modelo mental

Plataforma boa reduz variabilidade desnecessária sem esconder decisões importantes.

Separe:
1. **user/job** — quem usa e qual tarefa precisa concluir;
2. **capability** — qual capacidade comum a plataforma oferece;
3. **interface** — CLI, API, portal, template, pipeline, operator;
4. **guardrail** — defaults, policy e limites;
5. **escape hatch** — como sair do caminho padrão quando necessário;
6. **feedback** — adoção, tempo, falhas, satisfação e suporte.

## Fluxo de análise
1. Identifique usuários internos e jobs-to-be-done.
2. Meça dor repetida: tempo, incidentes, tickets, setup manual, divergência.
3. Separe capability de implementação/provedor.
4. Defina o menor self-service útil.
5. Escolha interface adequada ao fluxo real do time.
6. Codifique defaults seguros e políticas automáticas.
7. Preserve observabilidade e debuggability da abstração.
8. Defina escape hatch explícito e suportado.
9. Meça adoption, lead time, failure rate e suporte.
10. Trate feedback como backlog de produto da plataforma.

## Heurísticas

### Golden path
Golden path deve ser o caminho mais fácil e mais seguro para o caso comum, não o único caminho possível.

### Abstração
Abstraia variabilidade repetitiva; não esconda sinais necessários para diagnóstico, custo ou segurança.

### Self-service
Self-service real exige provisioning/action sem ticket humano para o fluxo suportado.

### Platform as product
Tenha users, owner, roadmap, SLOs, telemetry de uso e feedback contínuo.

### Guardrails
Prefira enforcement automático e defaults seguros a documentação que depende de memória humana.

### Cognitive load
Remova decisões acidentais; preserve decisões de domínio e tradeoffs arquiteturais importantes.

## Saída esperada
Declare:
- usuários e jobs;
- capability proposta;
- interface/self-service;
- defaults e guardrails;
- escape hatch;
- sinais expostos para debug/ops;
- métricas de adoção e valor;
- riscos de lock-in/acoplamento e mitigação.

Consulte `patterns.md` e `cheatsheet.md`.