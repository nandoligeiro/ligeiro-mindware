---
name: ports-and-adapters
description: "Cocérebro baseado no NotebookLM Arquitetura Hexagonal: Prática e Sustentabilidade de Aplicações. Use quando o usuário quiser projetar, revisar, refatorar ou explicar Ports and Adapters / Arquitetura Hexagonal; isolar domínio de frameworks, banco, HTTP e mensageria; comparar controller-service-persistence com domínio/portas/adaptadores; desenhar APIs e SPIs; implementar em Java/Spring Boot; criar testes com stubs; ou avaliar acoplamento, dependências e anti-padrões arquiteturais."
---

# Ports and Adapters — Cocérebro

Use esta skill para proteger lógica de negócio por meio de arquitetura hexagonal: domínio no centro, portas como contratos e adaptadores como tradução técnica.

## Fonte

- NotebookLM: `https://notebooklm.google.com/notebook/7fa36b45-2fa9-4945-8774-d3c038829acc`
- Nota de extração: `sources/ports-and-adapters-notebooklm-sources.md`

## Como Pensar

Arquitetura hexagonal não é uma organização bonita de pastas. É uma regra de dependência: decisões técnicas dependem do domínio; o domínio não depende das decisões técnicas.

O objetivo é separar:

- **Complexidade essencial**: regras de negócio, invariantes, casos de uso e linguagem do domínio.
- **Complexidade mandatória**: banco, HTTP, filas, frameworks, serialização, autenticação, rede.
- **Complexidade acidental**: dívida criada quando tecnologia invade regra de negócio.

## Carregue Sob Demanda

- Fundamentos, vocabulário e comparação com camadas: `references/principles.md`
- Implementação Java/Spring Boot: `references/java-spring-boot.md`
- Refatoração e revisão arquitetural: `references/refactoring-review.md`
- Testes, stubs e critérios de qualidade: `references/testing-review.md`

## Diagnóstico Inicial

1. Qual regra de negócio precisa ficar protegida?
2. Quais atores dirigem o sistema: REST, fila, job, CLI, UI, outro serviço?
3. Quais recursos externos o domínio precisa: banco, API, cache, broker, filesystem?
4. Quais tipos estão vazando para o domínio: `ResponseEntity`, `@Entity`, `Pageable`, DTO, JSON, JDBC, JPA, Kafka, Redis?
5. A porta expressa uma intenção de negócio ou apenas espelha CRUD/persistência?
6. O domínio pode ser testado sem Spring, banco, container e rede?
7. Existe barreira de build/ArchUnit impedindo dependências técnicas no domínio?
8. O adaptador está atuando como camada anticorrupção ou está repassando sujeira externa para dentro?

## Regras Práticas

- Faça dependências apontarem para dentro.
- Modele portas com linguagem de negócio, não com detalhes de transporte ou persistência.
- Use API/porta de entrada para capacidades oferecidas pelo domínio.
- Use SPI/porta de saída para necessidades que o domínio delega ao mundo externo.
- Coloque Spring, JPA, Jackson, Kafka, Redis e HTTP nos adaptadores.
- Não serialize entidades de domínio diretamente em controllers.
- Não anote o domínio com `@Entity`, `@Table`, `@JsonProperty`, `@Service`, `@Component` ou `@Autowired`.
- Use DTOs/resources nos adaptadores de entrada e mapeadores explícitos na fronteira.
- Faça adaptadores de saída limparem paginação, tipos estranhos, nulos, strings mágicas e protocolos externos.
- Trave a arquitetura com módulo separado, Maven Enforcer, Gradle constraints ou ArchUnit.

## Resposta Padrão

Ao responder sobre design hexagonal:

1. Nomeie o caso de uso em linguagem de negócio.
2. Separe domínio, APIs de entrada, SPIs de saída e adaptadores.
3. Mostre o sentido das dependências.
4. Aponte quais tipos não podem atravessar a fronteira.
5. Proponha testes rápidos do domínio e testes focados dos adaptadores.
6. Chame atenção para sobre-engenharia quando o caso for CRUD simples sem regra relevante.
