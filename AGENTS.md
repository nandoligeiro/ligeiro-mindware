# Ligeiro Mindware — instruções do repositório

## Objetivo

Este repositório transforma conhecimento técnico em Agent Skills reutilizáveis, portáveis e verificáveis e usa agents como uma camada fina de orquestração sobre essas capacidades. Skills são unidades de contexto e procedimento; agents coordenam responsabilidades, routing, handoffs e critérios de saída.

## Organização

- `agents/`: papéis de orquestração; cada agent começa em `agents/<agent-name>/AGENT.md`.
- `skills/`: catálogo autoral de skills; cada skill começa em seu próprio diretório com `SKILL.md`.
- `evals/`: cenários de ativação, comportamento esperado e casos de não ativação das skills.
- `docs/`: decisões de arquitetura e convenções do projeto.
- `tools/`: conversores, validadores e utilitários de engenharia.

## Modelo

```text
Agent = responsabilidade + workflow + routing + handoff + exit criteria
Skill = conhecimento e procedimento especializado
Tool = capacidade externa
Eval = evidência e proteção contra regressão
```

Agents não devem duplicar conhecimento especializado já disponível nas skills. Um agent seleciona e coordena skills conforme o risco e a etapa do trabalho.

## Regras para criar ou alterar agents

1. Defina uma responsabilidade estável e transversal, não uma tecnologia específica.
2. Mantenha `AGENT.md` focado em quando ativar, workflow, routing, handoffs e critério de saída.
3. Referencie skills por responsabilidade; não copie seus patterns, cheatsheets ou referências para o agent.
4. Evite agents como `java-agent`, `spring-agent` ou `kafka-agent` quando uma skill já cobre a capacidade.
5. Use progressive disclosure: não carregue todo o catálogo por padrão.
6. Exija evidência objetiva antes de concluir uma etapa.
7. Preserve human-in-the-loop para ações destrutivas, segurança, produção, dados sensíveis ou ambiguidade de negócio.
8. Se o agent revelar uma falha repetível em uma skill, encaminhe-a para eval/hardening em vez de esconder o problema na orquestração.

## Regras para criar ou alterar skills

1. Mantenha `SKILL.md` focado no comportamento que o agente deve executar.
2. Use frontmatter YAML válido com `name` e `description`; o nome deve coincidir com o diretório.
3. Escreva a descrição com sinais claros de quando a skill deve ser ativada.
4. Prefira instruções imperativas, critérios de decisão e saídas observáveis.
5. Use `references/`, `scripts/` e `assets/` somente quando agregarem valor; carregue referências sob demanda.
6. Evite instruções específicas de um único provedor quando elas não forem necessárias.
7. Não faça commit de segredos, fontes privadas, dados pessoais ou cópias extensas de conteúdo protegido.
8. Adicione ou atualize cenários em `evals/` quando mudar roteamento, fluxo ou formato de saída.
9. Rode `python3 tools/skill-engineering/validate_skills.py` antes de abrir uma alteração.
10. Para skills L3, rode também `python3 tools/skill-engineering/validate_evals.py --strict`.

## Portabilidade

O contrato principal das skills é o padrão `SKILL.md`. A fonte fica em `skills/`; o `apm.yml` define como distribuí-la para os alvos suportados. Devin/Codex usam o catálogo convergente `.agents/skills`, enquanto Claude Code usa `.claude/skills`.

`AGENT.md` é uma convenção autoral deste repositório para descrever papéis portáveis de orquestração. Integrações específicas de provedor podem adaptar esses papéis, mas não devem virar a única fonte de verdade.

## Critério de pronto

Uma alteração de skill está pronta quando a skill é encontrada no caminho esperado, ativa nos cenários positivos, não ativa nos cenários negativos, executa o fluxo descrito e produz uma saída verificável sem depender de contexto implícito.

Uma alteração de agent está pronta quando sua responsabilidade não sobrepõe indevidamente outra, o routing para skills está claro, handoffs são explícitos e o critério de saída exige evidência observável.
