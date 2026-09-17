# Cheatsheet — AI-assisted software engineering

## Fluxo

`intent -> context -> plan -> execute -> verify -> evaluate -> learn`

## Perguntas rápidas

- Qual resultado observável define sucesso?
- Qual contexto é realmente necessário para a próxima decisão?
- O agente precisa de leitura, escrita ou ação destrutiva?
- Qual tool/MCP server executa o efeito real?
- Qual gate determinístico prova que a mudança está correta?
- O agente está julgando o próprio output sem evidência externa?
- Há stop condition, budget e fallback para o loop?
- A falha descoberta virou eval/regressão?

## Decisões

### Use skill quando
Há procedimento reutilizável e contexto especializado que deve ser carregado sob demanda.

### Use tool quando
Há capacidade externa com contrato e efeito observável.

### Use subagent quando
Há fronteira clara de responsabilidade/contexto que justifica delegação.

### Use MCP quando
A interoperabilidade padronizada entre agente e capability externa agrega valor; ainda aplique authn/authz, validação e least privilege.

## Gates comuns

- build/compile
- unit/integration/contract tests
- schema validation
- static analysis/lint
- security checks
- diff/review
- smoke test
- artifact inspection
- telemetry/log evidence

## Red flags

- contexto inteiro do repo sem recuperação seletiva
- permissões de admin por conveniência
- agente mudando muitos arquivos antes de validar
- retry infinito
- outro LLM como única validação
- memória persistindo hipótese não verificada
- tool write sem idempotência/auditoria quando necessário
