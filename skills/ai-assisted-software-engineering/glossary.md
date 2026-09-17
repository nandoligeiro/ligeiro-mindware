# Glossário — AI-assisted software engineering

## Agent
Loop que usa modelo, contexto e tools para perseguir um objetivo com algum grau de autonomia.

## Subagent
Agente delegado para uma responsabilidade mais estreita, com contexto e critério de saída próprios.

## Harness
Infraestrutura ao redor do modelo que gerencia contexto, tools, estado, coordenação, limites, execução e recuperação.

## Skill
Pacote reutilizável de instruções, recursos e procedimentos carregado quando relevante para a tarefa.

## Tool
Capability externa invocável pelo agente, com contrato, permissões e possíveis efeitos colaterais.

## MCP
Protocolo de interoperabilidade entre clientes/agentes e servidores que expõem tools, resources ou outras capabilities. Não substitui segurança ou autorização do sistema chamado.

## Context engineering
Disciplina de selecionar, estruturar, recuperar e atualizar o contexto necessário para a próxima decisão do agente.

## Eval
Cenário que verifica ativação, comportamento, resultado ou regressão de um sistema agentic.

## Deterministic gate
Checagem objetiva usada para aceitar ou rejeitar uma mudança, como build, teste, schema validation ou policy check.

## Human-in-the-loop
Intervenção humana em pontos explicitamente definidos, sobretudo quando há ambiguidade, risco material, permissão elevada ou ação irreversível.

## Progressive disclosure
Estratégia de carregar contexto em camadas conforme a necessidade, em vez de fornecer tudo de uma vez.

## Regression memory
Preservação de uma falha real como eval, teste, regra ou fixture verificável.
