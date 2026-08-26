---
name: skill-creator
description: Design and create reusable Agent Skills from a goal, workflow, document, codebase, or repeated task. Use when a new skill is needed, an existing procedure must become portable, or a skill needs clearer triggers, boundaries, references, scripts, assets, or evaluation scenarios.
---

# Criar uma Agent Skill

Converta uma necessidade repetível em uma skill pequena, explícita e verificável.

## Processo

1. Defina o objetivo operacional em uma frase.
2. Liste sinais de ativação e casos parecidos que não devem ativar a skill.
3. Descreva entradas, pré-condições, ferramentas permitidas, passos, decisões e formato de saída.
4. Separe conhecimento estável do procedimento: mantenha a orientação principal no `SKILL.md` e mova detalhes consultáveis para `references/`.
5. Adicione `scripts/` apenas para operações determinísticas que o agente não deve reimplementar a cada uso.
6. Para skills complexas, registre um modelo de projeto WSA: roteamento, fluxo de trabalho, semântica, anexos e proveniência.
7. Crie pelo menos um cenário positivo, um negativo e um caso incompleto em `evals/`.
8. Valide frontmatter, nome, caminhos e tamanho; faça uma execução de teste antes de concluir.

## Resultado esperado

Entregue o diretório completo da skill, explique quando ela deve e não deve ser usada e aponte os cenários que comprovam o comportamento. Não inclua fontes privadas, segredos ou cópias extensas de material protegido.