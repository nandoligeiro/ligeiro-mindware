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
- **Pacote ou instalação**: distribuição direta em `.agents/skills` ou empacotamento com APM.

WSA/Skill-IR é uma disciplina de autoria e avaliação; não é um requisito adicional do runtime. O runtime deve continuar enxergando um `SKILL.md` simples.

## Estrutura atual

```text
ligeiro-mindware/
├── AGENTS.md
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
6. Empacotar ou instalar sem duplicar fontes de verdade.
7. Refinar a partir de traços reais e preservar regressões.

## Devin Desktop/Local

A compatibilidade prática é obtida mantendo o formato portátil e instalando a skill no catálogo `.agents/skills` do projeto ou do usuário. A configuração específica do agente deve permanecer opcional. O mesmo catálogo pode ser consumido no ambiente pessoal e, em uma etapa posterior, no ambiente corporativo autorizado.