# Software Engineer 2026 — capability roadmap

Este documento organiza o catálogo de skills pela capacidade que um engenheiro de software moderno precisa exercer, evitando crescimento orientado apenas por frameworks.

## Princípio

O catálogo evoluiu de uma coleção forte em Java/Spring para um conjunto mais equilibrado de capacidades de engenharia: domínio, sistemas distribuídos, qualidade, segurança, entrega, plataforma, dados, operação e engenharia assistida por IA.

A primeira expansão planejada do catálogo foi concluída em três ondas:

- P0 — fundação obrigatória;
- P1 — capacidade de entrega;
- P2 — profundidade operacional.

O foco agora deixa de ser expansão automática e passa a ser hardening, uso real, regressões observadas e evolução de maturidade.

## Cobertura atual

| Capability | Estado | Maturidade / observação | Skills relacionadas |
|---|---|---|---|
| Java/JVM moderno | forte | cobertura madura de performance e operação cloud native | `optimizing-cloud-native-java` |
| Spring ecosystem | forte | cobertura ampla do framework e integrações principais | `spring-framework`, `spring-data`, `spring-data-redis`, `spring-kafka`, `spring-security` |
| Domain-driven design | forte | fundamentos e heurísticas explícitas | `learning-domain-driven-design` |
| Ports & Adapters | forte | fronteiras, adapters e dependências explícitas | `ports-and-adapters` |
| Event streaming | forte | Kafka e integração Spring cobertos | `kafka-definitive-guide`, `spring-kafka` |
| Observability / SRE fundamentals | forte | sinais, instrumentação e diagnóstico cobertos | `observability-engineering` |
| Application security | forte | L3 — regression protected | `secure-software-engineering`, `spring-security` |
| Software supply chain | forte | L3 — SBOM, provenance, signing e verification | `secure-software-engineering` |
| Distributed systems | forte | L3 — failure modes, idempotência, ownership, recovery e backpressure | `distributed-systems-engineering` |
| Testing / quality engineering | forte | L3 — estratégia orientada a risco e feedback | `software-testing-engineering` |
| API / contract engineering | forte | L3 — semântica, compatibilidade, lifecycle e contract tests | `api-contract-engineering` |
| Cloud / platform engineering | forte | L3 — platform as product, self-service e guardrails | `platform-engineering`, `optimizing-cloud-native-java` |
| CI/CD / release engineering | forte | L3 — artifact promotion, progressive delivery e change safety | `software-delivery-engineering` |
| AI-assisted engineering | forte | L3 — harness, context, tools, permissions, evals e verification | `ai-assisted-software-engineering` |
| Database engineering | forte | L3 — modelagem, índices, concorrência, migrations e recovery | `database-engineering` |
| Networking | forte | L3 — diagnóstico por estágio, timeouts, TLS, proxies e connection lifecycle | `networking-for-software-engineers` |
| Incident / resilience engineering | forte | L3 — detect, stabilize, recover, explain e learn | `incident-resilience-engineering`, `observability-engineering` |

## Estado da primeira expansão

### P0 — fundação obrigatória — concluído

1. `distributed-systems-engineering`
   - partial failures, timeouts, retries e backoff;
   - idempotency, dedupe, claim, lease e fencing;
   - ordering, consistency, availability e partitions;
   - sagas, outbox/inbox e recovery;
   - backpressure, load shedding e concurrency control;
   - failure modes e trade-offs verificáveis.

2. `software-testing-engineering`
   - unit, integration, contract e end-to-end tests;
   - Testcontainers e ambientes reproduzíveis;
   - property-based e mutation testing;
   - determinismo, fixtures e test data;
   - fault injection e chaos testing;
   - estratégia de testes orientada a risco.

3. `secure-software-engineering`
   - threat modeling e secure-by-design;
   - requisitos verificáveis;
   - secrets, authn/authz, crypto e data protection;
   - dependency security e vulnerability management;
   - SBOM, provenance, signing e software supply chain;
   - security gates no SDLC.

4. `ai-assisted-software-engineering`
   - context engineering;
   - agent, subagent, skill e tool use;
   - MCP e integração com ferramentas;
   - harness engineering;
   - evals, verification e regression loops;
   - permissions, sandboxing e human-in-the-loop;
   - observabilidade, custo e bounded agent loops.

### P1 — capacidade de entrega — concluído

5. `api-contract-engineering`
   - contratos síncronos e assíncronos;
   - backward compatibility e schema evolution;
   - consumer-driven contracts;
   - versioning, deprecation e telemetry de adoção;
   - semântica, ownership e error contracts.

6. `platform-engineering`
   - platform as product;
   - golden paths e paved roads;
   - self-service real;
   - policy-as-code e guardrails;
   - scaffolding, developer experience e escape hatches.

7. `software-delivery-engineering`
   - CI/CD e integração frequente;
   - build once e promoção do mesmo artefato imutável;
   - progressive delivery, canary e feature flags;
   - rollback, roll-forward e change safety;
   - configuração por ambiente sem rebuild.

8. `database-engineering`
   - modelagem orientada a invariantes e access patterns;
   - indexes e query plans;
   - transactions, isolation e optimistic concurrency;
   - expand-and-contract migrations;
   - connection pool como budget global;
   - backup, restore e recovery testados.

### P2 — profundidade operacional — concluído

9. `networking-for-software-engineers`
   - diagnóstico `DNS -> route -> connect -> TLS -> protocol -> application`;
   - connection lifecycle e timeout budgets;
   - DNS, TLS/mTLS e certificates;
   - proxies, gateways, NAT, load balancing e service mesh;
   - keep-alive, pools e portas efêmeras.

10. `incident-resilience-engineering`
    - detect, stabilize, recover, explain e learn;
    - SLO, error budget e symptom-based detection;
    - circuit breaker, bulkhead, load shedding e graceful degradation;
    - failover/DR com RTO/RPO testados;
    - postmortem e follow-up verificável.

## Maturidade atual

A cobertura das capabilities planejadas agora é forte, mas cobertura não é sinônimo de aprendizado de produção.

As novas capabilities P0, P1 e P2 têm alvo e proteção L3 — regression protected:

- ativação e não ativação explícitas;
- workflow e heurísticas verificáveis;
- cenários positive, negative, incomplete e edge;
- regressões preservadas por `validate_evals.py`;
- comportamento vendor-neutral quando possível.

O próximo alvo é L4 — production learned:

```text
real task
  -> trace / evidence
  -> failure or friction
  -> regression scenario
  -> skill refinement
  -> re-evaluation
  -> learned experience
```

Uma capability só deve ser considerada L4 quando tiver sido refinada por uso real recorrente, incluindo falhas observadas e trade-offs comprovados.

## Próximo ciclo — hardening, não P3 automático

Não existe um P3 pré-definido.

O próximo ciclo deve priorizar:

1. levar skills existentes de L1/L2 para L3;
2. usar as capabilities P0/P1/P2 em tarefas reais;
3. transformar failures, misses e ambiguidades em evals de regressão;
4. medir sobreposição e conflitos de ativação entre skills;
5. remover duplicação e dependência implícita de contexto;
6. promover para L4 apenas capacidades sustentadas por evidência de produção;
7. criar novas skills somente quando gaps reais aparecerem no uso.

## Regra de priorização

Uma nova skill deve entrar no catálogo quando satisfizer pelo menos um destes critérios:

- reduz risco recorrente de produção;
- melhora decisão arquitetural em mais de um stack/projeto;
- cobre capacidade transversal realmente ausente;
- transforma conhecimento em procedimento verificável;
- elimina dependência excessiva de uma tecnologia específica;
- existe evidência de tarefas reais mal atendidas pelas skills atuais.

Evite criar skills que apenas fragmentem documentação de frameworks já cobertos.

## North Star

```text
intent
  -> domain understanding
  -> architecture
  -> implementation
  -> verification
  -> security
  -> delivery
  -> production feedback
  -> learned experience
```

O catálogo deve ajudar humanos e agentes a percorrer esse ciclo com critérios explícitos, evidência e trade-offs claros.

A direção agora é sair de `coverage forte + L3` para `uso real + regressões reais + L4`.