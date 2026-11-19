---
name: assess-solution-architecture
description: Criar, conduzir e revisar Solution Architecture Assessment (SAA) para consolidação de aplicações, modernização, seleção de soluções, análises AS-IS/TO-BE, alternativas, trade-offs, ADRs, roadmaps e projetos desenvolvidos com Vibe Coding ou IA.
---

# Solution Architecture Assessment

Produzir assessments arquiteturais orientados a evidências e decisões, úteis a stakeholders técnicos e executivos.

## Estrutura obrigatória

Preservar exatamente esta ordem e numeração, independentemente do formato final:

1. Contexto e problema de negócio.
2. Stakeholders e expectativas.
3. Capacidades das soluções.
4. Arquitetura atual (AS-IS).
5. Requisitos funcionais e atributos de qualidade.
6. Alternativas de solução e trade-offs.
7. Arquitetura recomendada (TO-BE).
8. Roadmap evolutivo e riscos.

Ler `assets/saa-template.md` antes de redigir o SAA. Ler `references/assessment-method.md` antes de realizar comparações ou avaliações.

## Fluxo de execução

1. Compreender a decisão esperada, as soluções candidatas, o problema e as restrições. Fazer poucas perguntas relevantes de cada vez; se o usuário quiser um exemplo, avançar com hipóteses explicitamente rotuladas.
2. Identificar fontes disponíveis: demonstrações, entrevistas, código, pipelines, testes, métricas, diagramas e relatórios. Não presumir acesso nem fabricar resultados.
3. Classificar cada achado como **Confirmado** (evidência direta), **Informado** (relato identificado), **Hipótese** (a testar) ou **Desconhecido**.
4. Construir as oito seções. Distinguir capacidade operacional de maturidade arquitetural; sistemas úteis podem ser incompletos.
5. Avaliar software criado por IA/Vibe Coding pelos mesmos critérios de engenharia de qualquer software: comportamento, segurança, qualidade, manutenção e operação. O método de autoria não comprova falhas.
6. Comparar opções de modo simétrico: status quo quando pertinente, evoluir A, evoluir B, integração/composição incremental e reconstrução quando defensável.
7. Aplicar critérios eliminatórios de segurança, compliance e viabilidade antes de qualquer pontuação; números e pesos hipotéticos não constituem decisão.
8. Relacionar recomendação aos requisitos, evidências, alternativas descartadas e ADRs; manter **proposta condicional** se o assessment estiver incompleto.
9. Construir roadmap incremental com owners, critérios de saída, continuidade, reversibilidade, rollback, migração e descomissionamento.
10. Encerrar a seção 8 com parecer executivo, confiança, pendências e próximo gate decisório. Não criar uma nona seção.

## Regras de saída

- Quando solicitado **exemplo/template**, entregar documento preenchido com dados ilustrativos claramente identificados; não só explicação das seções.
- Quando solicitado **template em branco**, usar os campos e tabelas de `assets/saa-template.md`.
- Quando solicitado **Discovery**, guiar entrevistas e gerar backlog de evidências.
- Quando solicitado **revisão**, indicar lacunas, vieses, contradições, decisões não sustentadas e ações corretivas.
- Priorizar Markdown com tabelas de rastreabilidade e diagramas Mermaid quando úteis. Gerar outro formato se solicitado.
- Não inventar métricas, avaliações de código, prazos, autorizações, riscos comprovados ou decisões aprovadas.
- Evitar recomendar tecnologias, microsserviços, DDD ou reescrita sem trade-offs demonstrados.
- Usar nomes de sistemas e dados sensíveis apenas quando fornecidos e apropriados ao documento.
