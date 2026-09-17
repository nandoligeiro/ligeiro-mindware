# Técnicas avançadas

## Property-based testing
Defina invariantes e gere muitos exemplos automaticamente. Útil para parsers, cálculos, serialização, estruturas de dados, regras financeiras e transformações com grande espaço de entrada. Sempre preserve seeds/counterexamples que revelarem regressões.

## Mutation testing
Altere o programa artificialmente e verifique se a suíte falha. Mutantes sobreviventes indicam assertions fracas, caminhos não exercitados ou comportamento irrelevante. Não use score como KPI isolado.

## Consumer-driven contracts
Útil quando múltiplos consumidores dependem de um produtor e releases são independentes. O contrato deve representar expectativas reais, não duplicar toda a especificação do serviço.

## Determinismo
Controle relógio, aleatoriedade, concorrência, locale/timezone, fixtures e dependências externas. Não corrija flakiness com retry automático sem descobrir a causa.

## Fault injection
Introduza timeouts, indisponibilidade, resposta inválida, disconnects, latência, duplicação e reordering para verificar comportamento de resiliência.

## Chaos testing
Use em ambientes controlados quando a hipótese é sistêmica e a blast radius é conhecida. Defina steady state, hipótese, limite de impacto, abort condition e observabilidade antes do experimento.

## Testability como arquitetura
Design testável tende a possuir fronteiras explícitas, dependências controláveis, efeitos observáveis, relógio/IDs injetáveis e responsabilidades coesas. Se testar exige subir o universo inteiro, o teste pode estar expondo um problema de design.
