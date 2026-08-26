---
name: skill-refiner
description: Refine an Agent Skill using execution traces, failed outputs, user feedback, diffs, or evaluation results. Use when a skill activates incorrectly, skips required work, produces the wrong format, mishandles inputs, or becomes inefficient.
---

# Refinar uma Agent Skill

Corrija a menor área capaz de eliminar a falha e preserve o comportamento já comprovado.

## Diagnóstico

Classifique a falha antes de editar:

- `routing`: ativou tarde, cedo demais ou a skill errada foi escolhida.
- `workflow`: o agente pulou, repetiu ou ordenou mal uma etapa.
- `semantics`: a regra, decisão ou saída ficou incorreta.
- `attachments`: referência, script, asset, ferramenta ou caminho não foi carregado corretamente.

## Processo

1. Reproduza o caso com a entrada original.
2. Separe causa observada de hipótese.
3. Edite descrição, corpo, referência, script ou cenário conforme a classe da falha.
4. Adicione um caso de regressão.
5. Execute novamente os casos positivos, negativos e de borda.
6. Relate o que mudou e qual comportamento deve permanecer inalterado.

Não aumente o prompt da skill para compensar uma referência mal organizada ou um script não determinístico.