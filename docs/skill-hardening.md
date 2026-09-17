# Skill hardening

Este documento define gates de qualidade para evitar que o catálogo cresça em quantidade e perca confiabilidade.

## Modelo de maturidade

### L0 — draft

- `SKILL.md` existe;
- frontmatter válido;
- objetivo ainda pode estar amplo;
- sem evidência de ativação e comportamento.

Não deve ser tratada como capacidade confiável do catálogo.

### L1 — structurally valid

- `name` coincide com diretório;
- `description` é válida e específica;
- referências são carregadas sob demanda;
- não contém segredos ou material protegido indevido;
- validator estrutural passa.

### L2 — behavior specified

- sinais de ativação explícitos;
- sinais de não ativação explícitos;
- workflow ou heurística de decisão explícitos;
- critérios de saída observável;
- casos de borda conhecidos;
- pelo menos um cenário positivo e um negativo em `evals/`.

### L3 — regression protected

- cenários positivos, negativos, incompletos e de borda;
- regressões relevantes preservadas como evals;
- alteração de comportamento exige atualização dos cenários;
- outputs importantes possuem assertions verificáveis;
- referências e instruções não contradizem o `SKILL.md`.

### L4 — production learned

- refinada com tarefas reais;
- falhas de roteamento ou execução viraram regressões;
- decisões importantes registram evidência e trade-offs;
- ruído e conteúdo não acionável foram removidos;
- a skill melhora resultado sem exigir contexto implícito do autor.

## Gates para novas skills

Toda nova skill deve responder claramente:

1. Qual tarefa repetível ela resolve?
2. Quando deve ativar?
3. Quando não deve ativar?
4. Qual decisão ou workflow ela melhora?
5. O que é sucesso observável?
6. Quais erros perigosos ela deve evitar?
7. Quais detalhes precisam estar no `SKILL.md` e quais podem ficar em referência?
8. Há dependência desnecessária de um provedor, framework ou produto?
9. Existe pelo menos um cenário de falha ou borda?
10. O conteúdo é conhecimento acionável ou apenas resumo?

## Definition of Done endurecida

Uma skill é considerada pronta para uso confiável quando:

- passa na validação estrutural;
- possui fronteiras de ativação claras;
- possui workflow ou heurísticas executáveis;
- explicita invariantes e anti-padrões relevantes;
- produz saída verificável;
- tem cobertura mínima de evals;
- não depende de memória privada ou contexto implícito;
- evita copiar documentação quando uma referência basta;
- mantém portabilidade entre agentes sempre que possível.

## Cobertura mínima de evals

Cada skill de domínio ou engenharia deve ter, no mínimo:

```text
positive       -> deve ativar e executar o fluxo esperado
negative       -> não deve ativar
incomplete     -> deve pedir/identificar contexto crítico ausente
edge           -> deve preservar uma regra ou trade-off importante
```

Meta-skills podem substituir `incomplete` ou `edge` por casos mais apropriados ao seu workflow, mas devem manter cenários positivos e negativos.

## Assertions recomendadas

Prefira assertions sobre comportamento, não frases exatas:

- conceitos obrigatórios presentes;
- conceito proibido ausente;
- sequência de decisão respeitada;
- riscos explicitados;
- saída contém campos/seções necessárias;
- ferramenta ou framework não é recomendado sem pré-condição;
- não há ativação fora do escopo.

Evite evals frágeis que dependam de wording literal.

## Anti-padrões do catálogo

- **Documentation dump**: converter documentação em milhares de tokens sem workflow.
- **Framework fragmentation**: uma skill para cada módulo quando uma capability transversal seria melhor.
- **Trigger inflation**: descrição tão ampla que a skill ativa para quase tudo.
- **Hidden context**: instrução funciona apenas porque o autor conhece detalhes não escritos.
- **Checklist theater**: listas grandes sem critérios de decisão.
- **Provider lock-in acidental**: comportamento central escrito para um único agente sem necessidade.
- **No regression memory**: corrigir uma falha e não transformá-la em cenário de avaliação.

## Processo de hardening do catálogo existente

Executar em ondas:

### Onda A — capacidades críticas

- `learning-domain-driven-design`
- `ports-and-adapters`
- `kafka-definitive-guide`
- `observability-engineering`
- `optimizing-cloud-native-java`

Objetivo: L3.

### Onda B — Spring operacional

- `spring-framework`
- `spring-security`
- `spring-kafka`
- `spring-data`
- `spring-data-redis`

Objetivo: L2 primeiro; depois L3 conforme uso real.

### Onda C — meta-skills

- `skill-creator`
- `skill-evaluator`
- `skill-organizer`
- `skill-refiner`

Objetivo: validar que o próprio sistema de criação/refino consegue preservar esses gates.

## Próxima automação

O validator atual deve continuar garantindo compatibilidade estrutural. A evolução recomendada é adicionar um validator separado para qualidade/evals, por exemplo:

```bash
python3 tools/skill-engineering/validate_skills.py --strict
python3 tools/skill-engineering/validate_evals.py --strict
```

Separar os validadores permite endurecer o catálogo progressivamente sem transformar dívida histórica de evals em quebra imediata de CI.
