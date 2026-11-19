# Solution Architecture Assessment (SAA)

**ID:** SAA-XXX | **Iniciativa:** [nome] | **Área:** [nome]
**Versão/Data:** [valor] | **Status:** Draft / Proposed / Approved
**Responsável/Aprovadores:** [nomes ou pendente]

> Estados de evidência: Confirmado, Informado, Hipótese, Desconhecido. Nunca tratar valores ilustrativos como fatos.

## 1. Contexto e problema de negócio

**Contexto:** [quais soluções, usuários, valor existente]
**Problema:** [dor comprovada, consequência e motivo da decisão]
**Objetivo e escopo:** [resultados, restrições, fora do escopo]

| Indicador | Baseline | Meta | Fonte/Status |
|---|---|---|---|
| [KPI] | [medido/desconhecido] | [proposto] | [fonte] |

## 2. Stakeholders e expectativas

| Stakeholder | Interesse | Papel/decisor | Critério de aceite | Evidência |
|---|---|---|---|---|
| [nome] | [necessidade] | [papel] | [critério] | [origem] |

## 3. Capacidades das soluções

| Capacidade | Solução A | Solução B | Criticidade | Fonte |
|---|---|---|---|---|
| [capacidade] | Completa/Parcial/Ausente/Desconhecida | Completa/Parcial/Ausente/Desconhecida | [nível] | [evidência] |

**Sobreposições:** [itens]. **Exclusividades:** [itens]. **Lacunas:** [itens].

## 4. Arquitetura atual (AS-IS)

**A:** [componentes, integrações, dados, deployment, ownership].
**B:** [componentes, integrações, dados, deployment, ownership].
**Diagramas AS-IS:** [Mermaid/C4 validado ou marcado hipotético].

| Dimensão técnica | A | B | Evidência/Pendência |
|---|---|---|---|
| Segurança | [estado] | [estado] | [fonte] |
| Testes e manutenção | [estado] | [estado] | [fonte] |
| Operação e observabilidade | [estado] | [estado] | [fonte] |
| CI/CD e dependências | [estado] | [estado] | [fonte] |

## 5. Requisitos funcionais e atributos de qualidade

| ID | Tipo | Descrição/cenário | Prioridade | Aceite mensurável | Fonte |
|---|---|---|---|---|---|
| RF-001 | Funcional | [capacidade] | [nível] | [resultado] | [fonte] |
| QA-001 | Qualidade | [estímulo → resposta] | [nível] | [métrica] | [fonte] |

**Restrições e gates:** [segurança, privacidade, compliance, ambiente].

## 6. Alternativas de solução e trade-offs

| Alternativa | Benefício | Custo/esforço | Riscos | Reversibilidade | Evidências |
|---|---|---|---|---|---|
| Manter status quo | [valor] | [valor] | [valor] | [valor] | [fonte] |
| Evoluir A | [valor] | [valor] | [valor] | [valor] | [fonte] |
| Evoluir B | [valor] | [valor] | [valor] | [valor] | [fonte] |
| Composição incremental | [valor] | [valor] | [valor] | [valor] | [fonte] |
| Reconstrução | [valor] | [valor] | [valor] | [valor] | [fonte] |

**Gates eliminatórios:** [status por opção].
**Matriz ponderada:** [apenas se existirem evidências; pesos e sensibilidade].

## 7. Arquitetura recomendada (TO-BE)

**Estado:** [condicional/aprovado/pendente].
**Alternativa:** [identificador ou pendente].
**Justificativa e vínculos com requisitos:** [análise].
**Diagrama TO-BE:** [componentes lógicos, integrações e dados].
**Contratos, segurança e operação:** [detalhes].
**ADRs e consequências:** [identificadores, status].

## 8. Roadmap evolutivo e riscos

| Fase | Entrega | Dependência | Responsável | Critério de saída | Rollback |
|---|---|---|---|---|---|
| Discovery | [evidências] | [item] | [owner] | [critério] | N/A |
| Foundations | [controles] | [item] | [owner] | [critério] | [plano] |
| Integração e migração | [fluxos] | [item] | [owner] | [critério] | [plano] |
| Convergência | [desativação segura] | [item] | [owner] | [critério] | [plano] |

| Risco | Probabilidade | Impacto | Mitigação | Owner |
|---|---|---|---|---|
| [risco] | [nível] | [nível] | [ação] | [owner] |

### Parecer executivo e próximo gate

**Recomendação e confiança:** [análise com limites].
**Questões abertas:** [lacunas prioritárias].
**Próxima decisão:** [quem decide, qual evidência falta].
