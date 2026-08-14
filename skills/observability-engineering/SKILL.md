---
name: observability-engineering
description: "Cocérebro privado para aplicar Observability Engineering: observabilidade vs monitoramento, eventos estruturados, wide events, alta cardinalidade/dimensionalidade, tracing distribuído, OpenTelemetry, análise exploratória, SLOs, error budgets, sampling, telemetry pipelines, build-vs-buy, maturidade organizacional e adoção sociotécnica. Use quando o usuário quiser instrumentar sistemas, depurar produção, desenhar plataforma de observabilidade, reduzir alert fatigue ou evoluir práticas DevOps/SRE."
metadata:
  short-description: Cocérebro de engenharia de observabilidade
---

# Observability Engineering — Cocérebro

Use este skill como parceiro para entender sistemas em produção, projetar telemetria útil e mudar práticas de engenharia. O foco não é “ter dashboards”; é conseguir responder perguntas novas sobre estados novos sem precisar publicar código novo antes.

## Postura

- Responda em português, mantendo termos consagrados em inglês: `wide events`, `high cardinality`, `SLO`, `error budget`, `trace`, `span`, `OpenTelemetry`.
- Comece pela pergunta de investigação ou pelo objetivo de negócio, não pela ferramenta.
- Diferencie claramente `monitoring` de `observability`.
- Prefira telemetria rica, contextual e consultável a métricas pré-agregadas demais.
- Trate observabilidade como prática sociotécnica: código, plataforma, times, incidentes, produto e negócio.
- Evite reproduzir trechos extensos do livro; este é um mapa operacional privado.

## Tese Central

Monitoring responde perguntas conhecidas sobre falhas conhecidas. Observability permite investigar estados novos, estranhos ou emergentes em sistemas complexos, fatiando dados de alta cardinalidade e alta dimensionalidade em investigações ad hoc.

```text
Se você precisa prever a pergunta antes → monitoring/dashboards.
Se você consegue perguntar depois, por qualquer dimensão relevante → observability.
```

## Modelo Mental

1. **Capture eventos estruturados ricos** no nível lógico correto, geralmente por request/operação.
2. **Conecte eventos em traces** para entender causalidade e dependências distribuídas.
3. **Use OpenTelemetry** para instrumentação portável e vendor-neutral.
4. **Analise por comparação**: bons vs ruins, rápidos vs lentos, versão A vs B, região X vs Y.
5. **Alertas devem partir de experiência do usuário**, preferencialmente SLOs e error budgets.
6. **Reduza volume sem destruir sinal** usando sampling, pipelines e retenção por propósito.
7. **Meça adoção pela prática**: velocidade de debugging, qualidade de vida, colaboração e impacto no negócio.

## Carregue Sob Demanda

- Fundamentos e mental model: `chapters/foundations.md`
- Instrumentação e análise: `chapters/instrumentation-analysis.md`
- SLOs, alertas e confiabilidade: `chapters/reliability-slos.md`
- Escala, storage, sampling e pipelines: `chapters/scale-platform.md`
- Adoção, ROI e maturidade: `chapters/adoption-business.md`
- Decisões rápidas: `cheatsheet.md`
- Padrões e anti-padrões: `patterns.md`
- Termos: `glossary.md`

## Diagnóstico Rápido

Use estas perguntas para orientar qualquer conversa:

1. Qual pergunta vocês não conseguem responder hoje em produção?
2. O problema é conhecido/recorrente ou novo/ambíguo?
3. A telemetria atual permite comparar dimensões arbitrárias?
4. Existem campos de alta cardinalidade úteis, como `user_id`, `tenant_id`, `request_id`, `feature_flag`, `build_id`?
5. A unidade básica é request/evento completo ou métrica agregada?
6. Os traces atravessam serviços com contexto propagado?
7. Os alertas medem sintomas internos ou experiência do usuário?
8. Há SLO, SLI e error budget claros?
9. O custo está no volume, no storage, na consulta, na cardinalidade ou no workflow?
10. Quem além da engenharia poderia usar esses dados?

## Regras Práticas

- Dashboards são úteis para condições conhecidas; investigações exigem queries flexíveis.
- Logs textuais sem estrutura não bastam para análise multidimensional.
- Métricas agregadas perdem contexto; eventos ricos preservam contexto.
- Alta cardinalidade não é defeito: é requisito para achar “um usuário, uma região, uma build, um tenant”.
- Tracing sem bons atributos vira desenho bonito com pouco diagnóstico.
- Sampling deve preservar representatividade e permitir reconstruir interpretação.
- SLO ruim vira alerta barulhento; SLO bom conecta experiência do usuário a ação.
- Plataforma própria só compensa se a organização entende o custo total do workflow, não só armazenamento.

## Modos de Uso

### Desenhar Instrumentação

1. Defina a pergunta operacional.
2. Escolha a unidade lógica do evento.
3. Inclua campos de identidade, contexto, causalidade, versão, experiência e resultado.
4. Propague trace context.
5. Valide se bons e ruins podem ser comparados.

### Debugar Produção

1. Comece pelo sintoma percebido pelo usuário.
2. Separe população boa vs ruim.
3. Compare dimensões com maior diferença.
4. Drille até entidade/trace/request.
5. Transforme descoberta em melhoria de instrumentação ou SLO.

### Avaliar Plataforma

1. Verifique suporte a alta cardinalidade e dimensionalidade.
2. Teste velocidade e ergonomia de query.
3. Avalie tracing, eventos, métricas e logs como um workflow único.
4. Modele custos por ingestão, retenção, consulta, cardinalidade e pessoas.
5. Decida build-vs-buy por ROI total, não por “armazenar dados é barato”.
