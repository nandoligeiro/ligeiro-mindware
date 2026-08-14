# Padrões, Anti-Padrões e Sinais

## Padrões Estratégicos

### Ubiquitous Language

Crie uma linguagem compartilhada entre especialistas do domínio e equipe técnica. Ela deve aparecer em conversas, histórias, testes, nomes de objetos, APIs e documentação.

**Use quando:** houver ambiguidade, retrabalho, requisitos contraditórios ou tradução constante entre negócio e tecnologia.

**Sinal de problema:** termos genéricos como `Manager`, `Processor`, `Data`, `Status` escondendo regras de negócio.

### Bounded Context

Defina onde uma linguagem/modelo é válido. Contextos diferentes podem modelar a mesma entidade de formas diferentes.

**Use quando:** áreas distintas usam o mesmo termo com sentidos diferentes, ou quando um modelo fica grande e contraditório.

**Anti-padrão:** tentar unificar todos os conceitos em um único modelo enterprise-wide.

### Context Map

Mapeie relações entre bounded contexts, incluindo upstream/downstream, padrões de integração e ownership dos times.

**Use quando:** dependências entre times e sistemas estão implícitas, gerando surpresa e regressões.

## Padrões Táticos

### Transaction Script

Organiza lógica por casos de uso/procedimentos.

**Bom para:** lógica simples, baixa volatilidade e baixa complexidade.

**Evite quando:** regras começam a se repetir entre scripts ou invariantes ficam difíceis de proteger.

### Active Record

Combina dados e operações simples em objetos persistentes.

**Bom para:** CRUD e validações simples.

**Evite quando:** o banco começa a definir o modelo em vez da linguagem do negócio.

### Domain Model

Modela comportamento rico com entidades, value objects, aggregates, repositories e domain services.

**Bom para:** core subdomains, regras complexas e mudanças frequentes.

**Risco:** confundir modelo de domínio com modelo anêmico de dados.

### Aggregate

Unidade de consistência transacional. Um aggregate protege invariantes internas e expõe comandos claros.

**Regra prática:** mantenha aggregates pequenos; não use aggregate como sinônimo de microservice.

### Domain Event

Registra algo significativo que aconteceu no domínio.

**Use quando:** outros processos precisam reagir a fatos de negócio, ou quando histórico tem valor conceitual.

**Anti-padrão:** usar eventos genéricos de CRUD como se fossem eventos de domínio.

### Event Sourcing

Persiste eventos como fonte da verdade e reconstrói estado por projeção.

**Bom para:** auditoria rica, temporalidade, explicabilidade e domínios onde a sequência de decisões importa.

**Cuidado:** versionamento, migração, idempotência e complexidade operacional.

## Padrões Arquiteturais

### Ports and Adapters

Domínio no centro, tecnologia nas bordas. Adaptadores conectam UI, banco, filas e serviços externos.

**Use quando:** quer testar domínio sem infraestrutura e reduzir dependência tecnológica.

### CQRS

Separa modelo de comandos do modelo de consultas.

**Use quando:** leituras e escritas têm necessidades muito diferentes.

**Cuidado:** não adote CQRS apenas por moda; ele adiciona sincronização e eventual consistency.

### Saga / Process Manager

Orquestra processos longos que atravessam contexts ou aggregates.

**Use quando:** workflow precisa reagir a eventos e emitir comandos ao longo do tempo.

## Anti-Padrões Recorrentes

- **Big ball of mud distribuído:** quebrar em serviços sem fronteiras de domínio.
- **Shared database entre contexts:** integração barata hoje, acoplamento caro amanhã.
- **Modelo anêmico:** objetos de domínio sem comportamento, regras espalhadas em services.
- **Cargo cult DDD:** usar aggregates, events e microservices sem complexidade que justifique.
- **Conformist invisível:** aceitar linguagem externa e deixar ela dominar o modelo local.
- **Event soup:** publicar eventos demais, técnicos demais ou sem contrato semântico.
