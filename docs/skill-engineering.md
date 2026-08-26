# Engenharia de skills

## Arquitetura

O projeto separa cinco preocupações:

```text
evidência -> WSA/Skill-IR -> SKILL.md -> evals -> pacote ou instalação
```

- **Evidência**: problema, documentação, código, traços de execução e feedback.
- **WSA/Skill-IR**: modelo de projeto interno para tornar explícitos roteamento, workflow, semântica, anexos e proveniência.
- **`SKILL.md`**: contrato portátil consumido por agentes compatíveis com Agent Skills.
- **`evals/`**: cenários que verificam ativação, execução, saída e não ativação.
- **Pacote ou instalação**: distribuição direta em `.agents/skills`, `.claude/skills` ou empacotamento determinístico com `apm.yml`.

WSA/Skill-IR é uma disciplina de autoria e avaliação; não é um requisito adicional do runtime. O runtime deve continuar enxergando um `SKILL.md` simples.

## Estrutura atual

```text
ligeiro-mindware/
├── AGENTS.md
├── apm.yml
├── skills/
│   ├── <domain-skill>/
│   │   ├── SKILL.md
│   │   ├── cheatsheet.md
│   │   ├── glossary.md
│   │   ├── patterns.md
│   │   └── chapters/
│   └── <engineering-skill>/
├── evals/
├── docs/
└── tools/
```

## Ciclo de vida

1. Capturar uma tarefa repetível e seus critérios de sucesso.
2. Criar ou atualizar a skill com fronteiras de ativação explícitas.
3. Mover detalhes para referências e automatizar apenas o que for determinístico.
4. Criar cenários positivos, negativos, incompletos e de borda.
5. Validar a estrutura e executar os cenários.
6. Validar com o catálogo local e com `apm run validate`.
7. Empacotar ou instalar sem duplicar fontes de verdade.
8. Refinar a partir de traços reais e preservar regressões.

## Compatibilidade entre agentes

A fonte de autoria fica em `skills/<slug>/` e cada distribuição adapta apenas o caminho de descoberta:

- **Devin Desktop/Local**: catálogo `.agents/skills`.
- **Claude Code**: `.claude/skills` no projeto ou `~/.claude/skills` no usuário.
- **Claude.ai/Cowork**: ZIP de uma skill individual enviado pela área de Skills; em Team/Enterprise, compartilhamento depende da governança da organização.
- **Codex e outros agentes compatíveis**: diretório de skills suportado pelo produto.

O conteúdo continua sendo o mesmo `SKILL.md`. Recursos específicos do agente devem ser opcionais, porque recursos exclusivos do Claude Code — como injeção dinâmica, hooks ou execução em subagente — não são portáveis para Claude.ai, Devin ou outros runtimes.
