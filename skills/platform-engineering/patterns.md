# Platform Engineering — Patterns

## Patterns

### Golden path
Caminho opinativo para o caso comum, com defaults seguros e baixa fricção.

### Paved road with escape hatch
O caminho recomendado é suportado e automatizado, mas casos legítimos podem sair dele com contrato claro.

### Capability API
Exponha capacidade estável independentemente do detalhe do provedor sempre que a abstração fizer sentido.

### Self-service provisioning
Usuário solicita e recebe capacidade sem ticket/manual handoff no fluxo suportado.

### Policy as code
Regras de segurança, compliance e plataforma são avaliadas automaticamente.

### Platform telemetry
Meça uso, sucesso, abandono, lead time, falhas e suporte por capability.

## Anti-patterns

### Portal-first platform
Construir UI bonita antes de resolver jobs reais e automação subjacente.

### Ticket-driven self-service
Chamar de self-service um formulário que termina em operação manual.

### Abstraction black box
Esconder logs, custos, limites, identity ou failure modes necessários para operar.

### Mandatory golden cage
Transformar golden path em único caminho e forçar casos inadequados à mesma abstração.

### Template graveyard
Scaffolds gerados uma vez que não recebem evolução, policy ou feedback.

### Platform without product ownership
Infra compartilhada sem users, roadmap, SLO, telemetry ou responsabilidade de produto.