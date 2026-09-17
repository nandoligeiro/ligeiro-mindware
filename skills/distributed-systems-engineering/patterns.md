# Patterns e Anti-padrões

## Patterns

### Idempotent consumer

Use uma operation/message id durável para transformar duplicate delivery em no-op ou retorno do resultado já produzido.

### Transactional outbox

Persista estado de negócio e intenção de publicação na mesma transação local.

### Inbox / dedupe table

Persista processamento recebido junto do efeito local para proteger o consumidor.

### Lease + fencing

Use ownership temporário com token monotônico aceito pelo recurso protegido.

### Reconciliation loop

Compare periodicamente estados entre sistemas e corrija divergências de forma idempotente.

### Bounded retry

Retry apenas para falhas classificadas como transitórias, com budget, backoff e jitter.

### Load shedding

Rejeite ou degrade trabalho antes que saturação se transforme em cascading failure.

## Anti-padrões

### Retry cego

Repetir qualquer exceção sem conhecer efeito remoto ou idempotência.

### Novo UUID a cada retry

Destrói a identidade lógica da operação e torna dedupe inútil.

### Ack antes do efeito durável

Pode perder trabalho após crash quando o broker considera a mensagem concluída.

### Ack só depois de efeito não-idempotente sem proteção

Pode duplicar efeito quando o processo cai depois do efeito e antes do ack.

### Dual write ingênuo

Atualizar banco e publicar remotamente em duas operações independentes sem recovery semantics.

### Lease sem fencing

Worker antigo pode continuar escrevendo após perder ownership.

### Fila infinita

Esconde overload até memória, disco, latência ou downstream colapsarem.

### DLQ como cemitério

Enviar para DLQ sem owner, reason code, replay seguro e prazo de tratamento.

### Exactly-once por marketing

Assumir garantia global porque um componente oferece exactly-once dentro de uma fronteira específica.

### Distributed lock como primeira escolha

Adicionar coordenação central onde unique constraint, version/CAS ou idempotência resolveriam com menos fragilidade.

### CAP como etiqueta

Chamar um sistema inteiro de CP/AP sem especificar operação, partição e comportamento requerido.
