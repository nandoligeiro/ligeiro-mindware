---
name: skill-evaluator
description: Evaluate whether an Agent Skill activates at the right time and follows its required workflow. Use when testing a new skill, diagnosing missed or incorrect activation, comparing skill revisions, or creating regression scenarios.
---

# Avaliar uma Agent Skill

Avalie a skill como um comportamento observável, não apenas como um documento bem escrito.

## Matriz mínima

Crie cenários para:

- `should-trigger`: o pedido contém sinais suficientes e a skill deve ativar.
- `should-not-trigger`: o pedido é próximo, mas pertence a outra skill ou não precisa de skill.
- `incomplete`: faltam dados; a skill deve pedir somente o necessário.
- `edge`: há ambiguidade, conflito de instruções, falha de ferramenta ou entrada fora do formato.

## Para cada cenário, verifique

1. A ativação esperada.
2. O uso das ferramentas e referências corretas.
3. A sequência mínima de trabalho.
4. O formato e os critérios da saída.
5. Comportamentos proibidos, como inventar dados, ignorar pré-condições ou executar uma ação irreversível sem autorização.
6. O custo: contexto carregado, chamadas, tempo e trabalho redundante.

Registre os casos em `evals/` e transforme cada falha reproduzível em regressão.