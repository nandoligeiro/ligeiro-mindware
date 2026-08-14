# Fundamentos

## Capítulos Cobertos

- Cap. 1 — What Is Observability?
- Cap. 2 — How Debugging Practices Differ Between Observability and Monitoring
- Cap. 3 — Lessons from Scaling Without Observability
- Cap. 4 — How Observability Relates to DevOps, SRE, and Cloud Native
- Cap. 9 — How Observability and Monitoring Come Together

## Ideia-Mãe

Observabilidade em software é a capacidade de entender qualquer estado do sistema, inclusive novo ou estranho, por meio de dados externos ricos e consultáveis. Ela é especialmente necessária em sistemas distribuídos, cloud native, com deploys frequentes e comportamento emergente.

## Monitoring Não Morreu

Monitoring continua útil para:

- condições conhecidas;
- infraestrutura estável;
- thresholds simples;
- tendências agregadas;
- disponibilidade básica.

Mas ele falha quando:

- a falha é nova;
- o sintoma não foi previsto;
- dashboards não têm a dimensão necessária;
- a investigação exige correlação entre usuário, versão, rota, região, deploy e dependências.

## Observability Como Debugging Exploratório

Observabilidade troca “olhar gráficos esperados” por “formular perguntas novas”. A prática central é comparar populações e descobrir quais dimensões explicam a diferença.

Exemplos:

- requests lentos vs rápidos;
- erros em uma versão vs versão anterior;
- tenants afetados vs não afetados;
- região problemática vs regiões saudáveis;
- tráfego com feature flag ligada vs desligada.

## Por Que Agora?

DevOps, SRE e cloud native aumentam necessidade de observabilidade porque:

- deploys são mais frequentes;
- arquiteturas são distribuídas;
- infraestrutura é dinâmica;
- falhas emergem de interação entre componentes;
- preprodução não consegue simular tudo;
- times são responsáveis por operar o que constroem.

## Princípio

Se sua prática exige saber de antemão quais perguntas serão necessárias, você está limitado ao passado. Observabilidade existe para reduzir o tempo entre surpresa e entendimento.
