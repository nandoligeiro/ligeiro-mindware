# Software Engineer 2026 — capability roadmap

Este documento organiza o catálogo de skills pela capacidade que um engenheiro de software moderno precisa exercer, evitando crescimento orientado apenas por frameworks.

## Princípio

O catálogo deve evoluir de uma coleção forte em Java/Spring para um conjunto equilibrado de capacidades de engenharia: domínio, sistemas distribuídos, qualidade, segurança, entrega, plataforma, dados, operação e engenharia assistida por IA.

## Cobertura atual

| Capability | Estado | Skills relacionadas |
|---|---|---|
| Java/JVM moderno | forte | `optimizing-cloud-native-java` |
| Spring ecosystem | forte | `spring-framework`, `spring-data`, `spring-data-redis`, `spring-kafka`, `spring-security` |
| Domain-driven design | forte | `learning-domain-driven-design` |
| Ports & Adapters | forte | `ports-and-adapters` |
| Event streaming | forte | `kafka-definitive-guide`, `spring-kafka` |
| Observability / SRE fundamentals | forte | `observability-engineering` |
| Application security | parcial | `spring-security` |
| Distributed systems | parcial | tópicos dispersos em Kafka, DDD e Java |
| Testing / quality engineering | parcial | tópicos dispersos nas skills existentes |
| API / contract engineering | parcial | sem skill dedicada |
| Cloud / platform engineering | parcial | cobertura indireta em cloud-native Java |
| CI/CD / release engineering | lacuna | sem skill dedicada |
| Software supply chain | lacuna | sem skill dedicada |
| AI-assisted engineering | lacuna | meta-skills existem, mas não há skill operacional do ciclo de engenharia com agentes |
| Database engineering | lacuna | Spring Data não substitui fundamentos de banco |
| Networking | lacuna | sem skill dedicada |
| Incident / resilience engineering | lacuna | observabilidade cobre diagnóstico, mas não o ciclo completo de incidentes e resiliência |

## Próximas skills

### P0 — fundação obrigatória

1. `distributed-systems-engineering`
   - partial failures, timeouts, retries e backoff;
   - idempotency, dedupe, claim, lease e fencing;
   - ordering, consistency, availability e partitions;
   - sagas, outbox/inbox, distributed transactions;
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
   - OWASP ASVS como requisitos verificáveis;
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
   - guardrails, permissions, sandboxing e human-in-the-loop;
   - observabilidade e custo de agentes.

### P1 — capacidade de entrega

5. `api-contract-engineering`
   - REST, OpenAPI e AsyncAPI;
   - backward compatibility e schema evolution;
   - consumer-driven contracts;
   - versioning e deprecation;
   - idempotency e error contracts.

6. `platform-engineering`
   - golden paths e paved roads;
   - internal developer platforms;
   - Kubernetes, GitOps e policy-as-code;
   - scaffolding e developer experience;
   - self-service com guardrails.

7. `software-delivery-engineering`
   - CI/CD;
   - trunk-based development;
   - artifact immutability e promotion;
   - progressive delivery, canary e feature flags;
   - rollback, roll-forward e change safety;
   - DORA metrics e feedback loops.

8. `database-engineering`
   - modeling e access patterns;
   - indexes e query plans;
   - transactions, MVCC e isolation;
   - locking e contention;
   - partitioning, replication e migrations;
   - relational vs document vs key-value trade-offs.

### P2 — profundidade operacional

9. `networking-for-software-engineers`
   - TCP, HTTP/2, HTTP/3 e connection lifecycle;
   - DNS, TLS/mTLS e certificates;
   - proxies, gateways, NAT e load balancing;
   - keep-alive, pools e timeout budgets.

10. `incident-resilience-engineering`
    - incident command e triage;
    - RCA e blameless postmortem;
    - resilience patterns;
    - graceful degradation e load shedding;
    - game days e failure drills;
    - follow-up verificável.

## Regra de priorização

Uma nova skill deve entrar no catálogo quando satisfizer pelo menos um destes critérios:

- reduz risco recorrente de produção;
- melhora decisão arquitetural em mais de um stack/projeto;
- cobre capacidade transversal hoje ausente;
- transforma conhecimento em procedimento verificável;
- elimina dependência excessiva de uma tecnologia específica.

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
