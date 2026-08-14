# Padrões e Anti-Padrões de Observabilidade

## Padrões

### Wide Events

Emita eventos estruturados ricos por unidade lógica de trabalho, com todas as dimensões que podem explicar comportamento.

**Use quando:** precisa investigar perguntas não previstas.

**Sinal bom:** você consegue filtrar por usuário, tenant, versão, endpoint, região, feature flag e erro sem criar métrica nova.

### High-Cardinality Investigation

Use campos com muitos valores únicos para achar casos específicos.

**Use quando:** problemas afetam “alguns usuários”, “um tenant”, “uma build”, “um shard”, “um endpoint”.

**Anti-padrão:** remover campos úteis só porque sistemas antigos cobram/sofrem com cardinalidade.

### Distributed Tracing

Conecte spans em uma árvore causal por request ou fluxo.

**Use quando:** uma operação cruza serviços, filas, bancos ou chamadas externas.

**Sinal ruim:** traces existem, mas não têm atributos úteis para explicar diferença entre rápido/lento ou sucesso/falha.

### OpenTelemetry-First

Instrumente com padrão aberto e exporte para backends substituíveis.

**Use quando:** quer reduzir lock-in e padronizar bibliotecas, collectors e contexto.

### Compare Good vs Bad

Compare populações contrastantes para encontrar dimensões explicativas.

**Use quando:** há latência, erro, regressão, falha parcial ou comportamento bizarro.

### SLO-Based Alerting

Alerta quando experiência do usuário consome error budget, não quando um sintoma interno cruza threshold arbitrário.

**Use quando:** quer reduzir alert fatigue e priorizar confiabilidade com linguagem de negócio.

### Telemetry Pipeline

Use pipelines para rotear, filtrar, enriquecer, amostrar, mascarar e isolar workloads de telemetria.

**Use quando:** há múltiplos produtores, consumidores, requisitos de segurança, custos e retenções.

## Anti-Padrões

### Dashboard-Driven Debugging

Ficar pulando entre dashboards tentando encaixar um problema novo em gráficos antigos.

**Correção:** use eventos ricos e comparação exploratória.

### Metrics-Only Observability

Chamar coleção de métricas de observabilidade.

**Correção:** preserve contexto em eventos/traces; métricas são complemento, não substituto.

### Log Soup

Logs textuais demais, pouca estrutura e nenhum campo comum para correlação.

**Correção:** normalizar campos e emitir eventos estruturados.

### Alert Fatigue

Alertas por sintomas internos, thresholds frágeis e baixa ação.

**Correção:** SLOs, burn rate e runbooks guiados por dados observáveis.

### Instrument Once and Forget

Tratar instrumentação como tarefa única.

**Correção:** instrumentação evolui com incidentes, features e perguntas novas.

### Build Platform Because Storage Looks Cheap

Subestimar query engine, UX, operação, escala, retenção, suporte e adoção.

**Correção:** calcular ROI total e comparar workflow completo.

### Sampling Blindness

Amostrar de modo que remove justamente os eventos raros e importantes.

**Correção:** preservar erros, outliers e traces relevantes; registrar taxa de amostragem.
