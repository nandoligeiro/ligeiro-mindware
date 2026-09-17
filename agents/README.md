# Agents

Os agents do Ligeiro Mindware são papéis de orquestração sobre o catálogo de skills. Eles não duplicam conhecimento técnico: selecionam capacidades, coordenam fluxo, exigem evidências e fazem handoff entre responsabilidades.

## Modelo

```text
Agent = responsabilidade + workflow + routing + handoff + exit criteria
Skill = conhecimento e procedimento especializado
Tool = capacidade externa
Eval = evidência e proteção contra regressão
```

## Agents disponíveis

- `software-engineering-agent`: conduz trabalho de engenharia de ponta a ponta, do intent à entrega verificável.
- `architecture-review-agent`: revisa decisões arquiteturais, boundaries, contratos e trade-offs antes de implementação ou mudança relevante.
- `production-readiness-agent`: avalia se um sistema está pronto para operar com segurança, observabilidade, resiliência e recuperação.
- `skill-maintainer-agent`: mantém a qualidade do catálogo, transforma falhas reais em evals e promove skills de L3 para L4.

## Regras

1. Prefira skills existentes; não replique conteúdo especializado dentro do agent.
2. Ative somente as skills necessárias ao risco e à decisão atual.
3. Faça progressive disclosure de contexto; não carregue o catálogo inteiro por padrão.
4. Exija evidência objetiva para considerar uma etapa concluída.
5. Faça handoff explícito quando outra responsabilidade assumir o fluxo.
6. Preserve human-in-the-loop para decisões destrutivas, segurança, produção, dados sensíveis ou ambiguidade de negócio.
7. Toda falha repetível deve virar candidato a eval, regra ou melhoria de skill.
