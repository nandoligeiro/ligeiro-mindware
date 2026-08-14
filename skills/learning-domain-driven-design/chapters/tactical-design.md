# Tactical Design

## Capítulos Cobertos

- Cap. 5 — Implementing Simple Business Logic
- Cap. 6 — Tackling Complex Business Logic
- Cap. 7 — Modeling the Dimension of Time
- Cap. 10 — Design Heuristics

## Ideia-Mãe

Tactical design responde: “como implementar a lógica deste bounded context de modo proporcional à sua complexidade?” Nem todo problema merece domain model; nem todo CRUD deve virar aggregate.

## Transaction Script

Use quando a lógica é procedural, curta e pouco mutável. O caso de uso coordena validações, persistência e efeitos.

Riscos:

- regras duplicadas;
- transações implícitas;
- dificuldade de proteger invariantes;
- crescimento para scripts frágeis.

## Active Record

Serve para modelos CRUD com comportamento simples. É útil quando estrutura de dados e persistência dominam o problema.

Risco principal: deixar o banco virar o modelo mental do negócio.

## Domain Model

Use quando o domínio tem regras, invariantes e comportamento que precisam ser expressos na linguagem ubíqua.

Blocos típicos:

- **Value Objects** para conceitos por valor;
- **Entities** para identidade e ciclo de vida;
- **Aggregates** para consistência transacional;
- **Repositories** para abstrair coleção/persistência;
- **Domain Services** para operações de domínio que não pertencem naturalmente a uma entidade.

## Aggregates

Um aggregate é uma fronteira de consistência, não um “objeto grande”. Ele deve proteger invariantes e expor operações de negócio.

Boas perguntas:

- Que invariantes precisam ser atômicas?
- Quais mudanças podem ser eventualmente consistentes?
- Este aggregate está grande porque o domínio exige ou porque estou evitando integração?

## Event Sourcing

Use quando a dimensão temporal é parte do domínio: auditoria, explicação, reconstrução histórica, compliance ou decisões baseadas em sequência de eventos.

Não use só para “ter histórico”. Logs tradicionais podem ser suficientes.

## Heurística de Decisão

```text
Baixa complexidade + baixa volatilidade → transaction script
CRUD simples → active record
Regras ricas + core/supporting importante → domain model
Estado derivado de histórico + temporalidade relevante → event sourcing
Leituras variadas + escrita protegida → CQRS/projeções
```

## Estratégia de Testes

- Transaction script: testes de caso de uso e integração transacional.
- Active record: testes de persistência e validação.
- Domain model: muitos testes unitários de regras e invariantes.
- Event sourcing: testes de comando → eventos e eventos → estado/projeção.
