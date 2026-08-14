# Padrões e Anti-Padrões Spring

## Padrões

### Constructor Injection

Use construtor para dependências obrigatórias. Isso torna o objeto válido após criação e facilita testes.

### Configuration as Composition Root

Use `@Configuration` e `@Bean` para compor dependências externas, infraestrutura e adaptações.

### Thin Controller, Rich Application Service

Controllers lidam com HTTP; serviços coordenam caso de uso; domínio guarda regra de negócio.

### Declarative Transactions at Service Boundary

Coloque `@Transactional` na fronteira de serviço que representa unidade de trabalho.

### Controller Advice for HTTP Errors

Centralize tradução de exceções para respostas HTTP em `@ControllerAdvice`.

### Test Pyramid Spring-Aware

Use muitos testes unitários puros, alguns slices/contextos focados e poucos testes end-to-end.

## Anti-Padrões

### Field Injection Everywhere

Dependências invisíveis e mutáveis dificultam teste e design.

**Correção:** constructor injection.

### God ApplicationContext

Buscar beans manualmente no contexto durante regra de negócio.

**Correção:** injete dependências explicitamente.

### Transactional Self-Invocation

Um método do bean chama outro método `@Transactional` do mesmo bean esperando proxy.

**Correção:** mover fronteira transacional para outro bean ou refatorar unidade de trabalho.

### Reactive by Decoration

Usar `Mono`/`Flux` por cima de dependências blocking sem isolamento.

**Correção:** use stack reativa real ou fique em MVC/blocking.

### Context-Heavy Unit Tests

Subir Spring para testar lógica simples.

**Correção:** teste unidade sem container; use Spring TestContext quando integração importa.

### Annotation Soup

Resolver design ruim adicionando anotação em cima de anotação.

**Correção:** simplifique fronteiras, configuração e responsabilidades.
