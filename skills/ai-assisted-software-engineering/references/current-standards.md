# Referências atuais — 2026

Use estas fontes como evidência para conceitos duráveis; não replique detalhes de produto no fluxo principal da skill.

## OpenAI Agents API — 2026-09-10

A OpenAI descreve agentes úteis como dependentes de um harness que gerencia contexto, tools, coordenação de subagentes e execução confiável de longa duração. Isso sustenta a separação entre modelo e harness e reforça que autonomia operacional exige infraestrutura, não apenas prompting.

Fonte pública: https://openai.com/index/introducing-the-agents-api/

## Model Context Protocol — specification 2026-07-28

A versão 2026-07-28 introduz core stateless, extensions, melhorias de autorização e evolução dos SDKs. Use MCP como protocolo de interoperabilidade entre agente e capabilities externas; mantenha controles de autorização, validação e policy no sistema integrado.

Fonte pública: https://blog.modelcontextprotocol.io/posts/2026-07-28/

## Agent Skills

Agent Skills organiza instruções, scripts e recursos em capacidades carregadas sob demanda. O conceito é útil como forma portável de encapsular procedimento e contexto especializado, separado do runtime do agente.

Fonte pública: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

## Princípio de atualização

Se versões ou produtos mudarem, preserve os invariantes da skill:

- contexto seletivo;
- tools com contrato e least privilege;
- harness com limites e estado;
- evals e regressões;
- gates determinísticos;
- evidence before acceptance;
- human escalation para decisões de alto impacto.
