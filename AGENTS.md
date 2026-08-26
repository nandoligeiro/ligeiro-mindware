# Ligeiro Mindware — instruções do repositório

## Objetivo

Este repositório transforma conhecimento técnico em Agent Skills reutilizáveis, portáveis e verificáveis. As skills devem funcionar como unidades de contexto e procedimento, não como cópias integrais de livros, documentos privados ou bases de conhecimento proprietárias.

## Organização

- `skills/`: catálogo autoral de skills; cada skill começa em seu próprio diretório com `SKILL.md`.
- `evals/`: cenários de ativação, comportamento esperado e casos de não ativação.
- `docs/`: decisões de arquitetura e convenções do projeto.
- `tools/`: conversores, validadores e utilitários de engenharia.

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

## Portabilidade

O contrato principal é o padrão `SKILL.md`. A fonte fica em `skills/`; o `apm.yml` define como distribuí-la para os alvos suportados. Devin/Codex usam o catálogo convergente `.agents/skills`, enquanto Claude Code usa `.claude/skills`. Arquivos específicos de um provedor são opcionais e não devem substituir o conteúdo portátil da skill.

## Critério de pronto

Uma alteração está pronta quando a skill é encontrada no caminho esperado, ativa nos cenários positivos, não ativa nos cenários negativos, executa o fluxo descrito e produz uma saída verificável sem depender de contexto implícito.