# Architecture and Communication

## Capítulos Cobertos

- Cap. 8 — Architectural Patterns
- Cap. 9 — Communication Patterns

## Ideia-Mãe

Arquitetura DDD deve impedir que a lógica de negócio se espalhe e deve tornar explícitas as fronteiras de comunicação. A pergunta não é “qual stack?”, mas “como protegemos o modelo e os contratos?”.

## Layered Architecture

Camadas comuns:

- Presentation/UI;
- Application;
- Business/domain logic;
- Infrastructure/data access.

Use para separar responsabilidades, mas cuide para não transformar a camada de aplicação em depósito de regra de negócio.

## Ports and Adapters

Também chamada hexagonal. O domínio fica no centro; bancos, filas, APIs e frameworks ficam nas bordas.

Use quando:

- infraestrutura muda;
- você quer testar domínio sem banco/fila;
- integrações externas não devem contaminar a linguagem local.

## CQRS

Separar comandos e consultas ajuda quando a escrita precisa preservar invariantes e a leitura precisa de modelos otimizados.

Use quando há:

- múltiplas projeções;
- leituras muito diferentes da escrita;
- necessidade de escalar leitura e escrita separadamente;
- UI/reporting com modelos específicos.

Evite quando o problema é CRUD simples.

## Model Translation

Contexts diferentes exigem tradução. Ela pode ser:

- stateless, quando uma mensagem é traduzida diretamente;
- stateful, quando é preciso acumular ou combinar dados;
- síncrona, quando o consumidor precisa da resposta agora;
- assíncrona, quando eventos/mensagens bastam.

## Integração de Aggregates

Não viole fronteiras de aggregate para manter tudo síncrono. Use eventos de domínio, process managers ou consistência eventual quando a regra de negócio permitir.

## Process Manager / Saga

Use para coordenar processos longos e multi-contexto. Ele observa eventos, mantém estado de orquestração e dispara comandos.

Sinal de uso: “quando A acontecer, espere B ou C; se C não chegar, faça D”.

## Outbox

Use quando precisa publicar mensagens de forma confiável junto com uma mudança local. A escrita no banco e o registro da mensagem ficam na mesma transação local; um publicador entrega depois.
