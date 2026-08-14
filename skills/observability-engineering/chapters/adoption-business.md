# Adoção, ROI e Maturidade

## Capítulos Cobertos

- Cap. 10 — Applying Observability Practices in Your Team
- Cap. 14 — Observability and the Software Supply Chain
- Cap. 19 — The Business Case for Observability
- Cap. 20 — Observability’s Stakeholders and Allies
- Cap. 21 — An Observability Maturity Model
- Cap. 22 — Where to Go from Here

## Comece Pelo Maior Ponto de Dor

Não tente “implantar observabilidade” de forma abstrata. Escolha um problema caro:

- incidentes lentos de diagnosticar;
- deploys inseguros;
- alert fatigue;
- CI/CD opaco;
- suporte sem dados;
- churn por baixa confiabilidade;
- custo explosivo de telemetria.

## Adoção em Times

Boas táticas:

- começar com um serviço importante;
- instrumentar iterativamente;
- mostrar investigação real antes/depois;
- treinar pelo workflow, não pela ferramenta;
- criar padrões de atributos;
- incorporar observabilidade no desenvolvimento.

## Software Supply Chain

Observabilidade também vale para CI/CD, builds e deploys.

Instrumente:

- duração de jobs;
- filas;
- cache hit/miss;
- etapa que falhou;
- runner/ambiente;
- commit/build/deploy;
- autor/time;
- dependências externas.

## Business Case

Benefícios que conversam com negócio:

- menor tempo de incidente;
- menos incidentes evitáveis;
- maior velocidade de entrega;
- maior satisfação do cliente;
- menor churn de engenheiros;
- melhor colaboração com suporte, produto e sucesso do cliente.

## Stakeholders e Aliados

Observability pode ajudar:

- suporte a entender casos específicos;
- produto a ver uso real;
- customer success a explicar impacto;
- vendas/executivos a entender confiabilidade;
- segurança/compliance a rastrear fluxos relevantes.

## Maturity Model

Avalie maturidade por capacidades, não por ferramenta comprada:

- qualidade da instrumentação;
- capacidade de responder perguntas novas;
- SLOs e error budgets;
- velocidade de debugging;
- uso durante desenvolvimento;
- colaboração entre times;
- qualidade de vida on-call;
- impacto mensurável no negócio.
