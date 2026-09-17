---
name: ai-assisted-software-engineering
description: Use esta skill para planejar, executar, verificar e evoluir trabalho de engenharia de software assistido por IA quando houver agentes, subagentes, tools, MCP, skills, automação de código, investigação técnica ou necessidade de evals e gates. Não use para perguntas simples sobre um produto específico de IA nem para substituir engenharia de software básica.
---

# AI-assisted software engineering

Trate IA como parte de um sistema de engenharia, não como um gerador autônomo de verdade.

## Ative quando

- a tarefa envolve agente, subagente, skill, tool use, MCP ou harness;
- há mudança de código ou infraestrutura feita com assistência de IA;
- é preciso decidir contexto, permissões, gates, evals ou estratégia de verificação;
- existe risco de loops, contexto excessivo, ferramentas destrutivas ou aceitação de saída não verificada;
- é necessário comparar execução humana, agentic ou híbrida.

## Não ative quando

- o pedido é só uma dúvida de sintaxe ou conceito de linguagem/framework;
- o usuário quer apenas saber onde clicar em um produto específico;
- não há decisão de engenharia ligada ao uso de IA;
- outra skill técnica cobre integralmente o problema e IA é apenas meio incidental.

## Modelo mental

Diferencie sempre:

- **prompt**: instrução local enviada ao modelo;
- **context**: evidência, estado, arquivos, restrições e histórico necessários para decidir;
- **skill**: conhecimento/procedimento reutilizável carregado sob demanda;
- **tool**: capacidade externa com contrato e efeitos observáveis;
- **agent**: loop que escolhe ações e ferramentas para atingir um objetivo;
- **subagent**: agente delegado para uma tarefa com escopo próprio;
- **harness**: infraestrutura que gerencia contexto, tools, execução, estado, limites e coordenação;
- **eval**: cenário que verifica ativação, comportamento, resultado ou regressão.

## Fluxo obrigatório

Siga:

```text
intent -> context -> plan -> execute -> verify -> evaluate -> learn
```

### 1. Intent

Defina objetivo, escopo e resultado observável. Não comece pela ferramenta.

### 2. Context

Carregue apenas o contexto necessário para a próxima decisão. Separe fatos, suposições e referências.

Evite despejar repositório, histórico ou documentação inteira sem necessidade.

### 3. Plan

Quebre a mudança em unidades pequenas e verificáveis. Identifique:

- arquivos/serviços afetados;
- riscos;
- ferramentas necessárias;
- permissões mínimas;
- gates de aceitação;
- pontos que exigem revisão humana.

### 4. Execute

Use ferramentas com escopo mínimo. Prefira ações reversíveis e commits/incrementos pequenos.

Para tarefas longas, delegue subagentes por fronteira clara, não por quantidade arbitrária.

### 5. Verify

Nunca aceite a saída só porque o agente declarou sucesso.

Use evidência determinística quando disponível:

- compilação;
- testes;
- linters;
- validação de schema/contrato;
- diff;
- smoke test;
- logs/telemetria;
- checagens de segurança;
- inspeção do artefato final.

### 6. Evaluate

Verifique também a qualidade do comportamento agentic:

- resolveu a tarefa correta?
- usou contexto relevante?
- escolheu tools adequadamente?
- respeitou limites/permissões?
- produziu evidência suficiente?
- criou regressão?

Transforme falhas repetíveis em evals.

### 7. Learn

Preserve conhecimento durável como skill, regra, fixture, eval ou documentação curta. Não preserve chain-of-thought nem ruído de sessão.

## Heurísticas

### Contexto

Use progressive disclosure: descubra -> carregue -> execute -> descarte o que não ajuda mais.

Se o contexto estiver grande, não assuma que mais tokens melhoram a resposta. Procure reduzir entropia e aumentar evidência relevante.

### Tools e MCP

Trate cada tool como API privilegiada:

- contrato de entrada/saída explícito;
- autenticação e autorização;
- escopo mínimo;
- efeitos colaterais claros;
- confirmação quando a ação for destrutiva/irreversível;
- idempotência quando aplicável;
- observabilidade e auditoria.

MCP é um protocolo de interoperabilidade; não substitui permissionamento, validação de parâmetros ou políticas do sistema chamado.

### Subagentes

Use quando houver fronteira natural de contexto ou responsabilidade, por exemplo investigação, implementação e revisão.

Não use subagentes só para paralelizar perguntas simples. Coordenação também custa contexto, latência e dinheiro.

### Geração probabilística x gates determinísticos

Permita criatividade na geração, mas torne determinístico o que define pronto.

Exemplos:

- agente escreve migration; banco/validator confirma schema;
- agente altera API; contract tests confirmam compatibilidade;
- agente cria código; testes + static analysis + revisão confirmam aceitação.

## Human-in-the-loop

Exija decisão humana quando houver:

- alteração destrutiva ou irreversível;
- impacto financeiro/material relevante;
- mudança de segurança/permissão;
- requisito ambíguo com trade-off de negócio;
- falha dos gates automáticos;
- conflito entre evidências.

Não use revisão humana como desculpa para não automatizar verificações objetivas.

## Failure modes

Procure explicitamente por:

- contexto velho ou incorreto;
- prompt injection vindo de dados externos;
- tool selection errada;
- parâmetros inventados;
- loops sem limite;
- subagentes duplicando trabalho;
- mudança ampla demais para revisar;
- testes inexistentes ou fracos;
- agente aceitando seu próprio output como prova;
- permissões excessivas;
- custo/latência sem orçamento;
- memória persistindo erro como verdade.

## Anti-padrões

- **Vibe coding sem gates**: aceitar código porque parece correto.
- **Context dump**: enviar tudo para o modelo sem estratégia de recuperação.
- **Agent loop infinito**: ausência de budget, stop condition ou escalonamento.
- **Tool god-mode**: conceder escrita/admin quando leitura bastaria.
- **LLM as judge único**: usar outra chamada probabilística como única evidência de correção.
- **Provider-shaped architecture**: desenhar o processo inteiro em torno de detalhes efêmeros de um produto.
- **Memory as truth**: persistir conclusão sem proveniência/evidência.
- **Hidden automation**: agente faz mudanças sem diff, log ou artefato auditável.

## Saída esperada

Ao analisar um fluxo assistido por IA, produza no mínimo:

1. objetivo e resultado verificável;
2. contexto necessário e fonte;
3. plano de execução;
4. tools/permissões;
5. gates determinísticos;
6. riscos/failure modes;
7. evals ou regressões a preservar;
8. pontos de revisão humana.

Leia `patterns.md` para patterns/anti-patterns, `cheatsheet.md` para decisões rápidas e `references/` apenas quando precisar aprofundar harness, MCP ou evals.
