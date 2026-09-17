# Patterns e anti-patterns

## Pattern — Progressive context disclosure

Carregue contexto conforme a próxima decisão exige. Comece por índices, metadados e arquivos de maior sinal; aprofunde sob demanda.

## Pattern — Deterministic acceptance gate

Separe geração probabilística de aceitação. Um agente pode propor a mudança; build, testes, contratos, políticas e inspeções definem pronto.

## Pattern — Least-privilege tool use

Conceda apenas as capabilities necessárias para a etapa atual. Eleve permissão explicitamente e reduza depois.

## Pattern — Bounded agent loop

Defina budget, stop condition, evidência de progresso e fallback/escalonamento. Iteração sem critério não é autonomia; é consumo sem controle.

## Pattern — Specialized subagent

Delegue investigação, implementação ou revisão quando cada atividade tem contexto e critério de saída próprios. Exija handoff curto e verificável.

## Pattern — Eval-driven regression memory

Quando um agente falhar de maneira reproduzível, preserve o cenário como eval. A memória útil é a regressão verificável, não a narrativa da sessão.

## Pattern — Tool contract

Modele tools como APIs: schema, erro, autenticação, autorização, idempotência, side effects e observabilidade.

## Pattern — Human escalation boundary

Defina antes da execução quais decisões exigem humano: ações irreversíveis, mudança de privilégio, ambiguidade de negócio, custo material ou falha de gate.

## Anti-pattern — Vibe coding

Código é aceito porque parece plausível ou porque o agente afirma ter terminado.

**Correção:** gates objetivos e diff revisável.

## Anti-pattern — Context dump

Repo, docs e histórico inteiros enviados em todas as etapas.

**Problema:** custo, distração, conflito entre fontes e pior recuperação do sinal.

## Anti-pattern — LLM judge monoculture

Uma segunda chamada ao modelo é a única checagem da primeira.

**Correção:** combine avaliações semânticas com verificadores determinísticos quando a propriedade for objetivamente testável.

## Anti-pattern — Tool god-mode

Agente recebe credencial ou capability ampla por conveniência.

**Correção:** scopes por ação e ambiente, sandbox quando aplicável, aprovação para elevação.

## Anti-pattern — Subagent swarm

Criar vários subagentes sem fronteiras claras de contexto, merge ou responsabilidade.

**Correção:** delegação só quando reduz carga cognitiva/tempo com handoff controlável.

## Anti-pattern — Infinite self-healing

Agente falha, tenta de novo indefinidamente e altera cada vez mais coisas.

**Correção:** limite de tentativas, rollback/checkpoint e escalonamento.

## Anti-pattern — Provider-shaped process

Workflow depende de um nome de feature ou detalhe efêmero de um fornecedor.

**Correção:** descreva capacidades duráveis: model, context, tool, skill, agent, harness, eval, permission e evidence.
