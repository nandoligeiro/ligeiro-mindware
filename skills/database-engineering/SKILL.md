---
name: database-engineering
description: "Ligeiro Mindware para modelar, migrar e operar bancos com segurança: workload e invariantes, modelagem relacional/documental, índices, planos de execução, transações, concorrência, connection pools, schema evolution, backup/restore, HA, CDC e lifecycle de dados. Use quando persistência, consistência local, performance de consultas ou evolução de schema forem parte central do problema."
metadata:
  short-description: Modelagem, performance e operação de dados
---

# Database Engineering

Projete a persistência a partir de **invariantes + workload + operação**, não apenas do modelo de objetos.

## Ativação
Use esta skill quando houver:
- escolha/modelagem de storage;
- schema e migrations;
- índices, query plans ou performance de consulta;
- transações, isolamento, locks ou optimistic concurrency;
- pool/conexões e saturação;
- backup/restore, HA e recovery;
- CDC/lifecycle de dados;
- crescimento, particionamento ou retenção.

Não ative para:
- sintaxe trivial de ORM/repository;
- regra de domínio sem impacto de persistência;
- consistência entre múltiplos serviços quando o problema principal é distribuído.

## Modelo mental

Separe:
1. **invariants** — o que nunca pode ficar inválido;
2. **workload** — reads/writes, volume, cardinalidade, hot paths;
3. **model** — tabelas/documentos/chaves e relações;
4. **access paths** — índices e consultas reais;
5. **concurrency** — isolation, locks, versions e contention;
6. **evolution** — migrations e compatibilidade app/schema;
7. **operations** — pool, backup, restore, HA, observabilidade e capacity.

## Fluxo de análise
1. Declare invariantes de negócio e atomicidade local necessária.
2. Caracterize workload: padrões de leitura/escrita, volume, crescimento e latência.
3. Modele dados para preservar invariantes e acessos principais.
4. Defina keys, constraints e índices com base em queries reais.
5. Escolha transação/isolation/concurrency control por anomalia que precisa evitar.
6. Planeje schema evolution compatível com versões concorrentes da aplicação.
7. Dimensione connections/pools considerando limite do banco e concorrência total.
8. Defina backup, restore testado, HA e objetivos de recovery.
9. Instrumente slow queries, locks, saturation, replication lag e storage growth.
10. Valide com query plan, carga representativa e exercícios de recovery.

## Heurísticas

### Constraints
Quando o banco pode garantir uma invariável local com unique/FK/check/transaction, prefira enforcement durável a validação apenas na aplicação.

### Indexes
Índice é tradeoff: melhora certos reads e custa write/storage/maintenance. Crie a partir de access pattern e valide no plano.

### Isolation
Escolha pelo tipo de anomalia intolerável; nível maior não é automaticamente melhor se aumenta contention desnecessário.

### Migrations
Prefira expand-and-contract para mudanças que precisam coexistir com múltiplas versões da aplicação.

### Pools
Pool não cria capacidade. Soma de conexões de todas as instâncias deve respeitar capacidade real do banco e headroom operacional.

### Backup
Backup sem restore testado é hipótese, não recovery plan.

## Saída esperada
Declare:
- invariantes e workload;
- modelo/chaves/constraints;
- access paths e evidência de query plan;
- transação/concorrência;
- plano de migration;
- pool/capacity assumptions;
- backup/restore/HA;
- métricas e failure modes residuais.

Consulte `patterns.md` e `cheatsheet.md`.