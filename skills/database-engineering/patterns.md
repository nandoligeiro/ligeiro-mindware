# Database Engineering — Patterns

## Patterns

### Constraint-backed invariant
Use unique/FK/check/transaction para invariantes locais que o banco pode proteger de forma durável.

### Query-driven indexing
Parta das consultas e cardinalidades reais; valide com plano de execução e carga representativa.

### Expand-and-contract migration
Adicione estrutura compatível, migre leitores/escritores/dados e só depois remova a forma antiga.

### Optimistic concurrency
Use version/CAS quando conflitos são raros e precisam ser detectados explicitamente.

### Bounded connection pool
Dimensione por capacidade total do banco, concorrência e headroom; trate fila/backpressure na aplicação.

### Tested restore
Execute restauração regularmente e compare RPO/RTO observados com objetivos.

## Anti-patterns

### ORM-shaped database
Modelar storage só para espelhar classes sem considerar invariantes e access patterns.

### Index everything
Criar índice para toda coluna e degradar write/storage sem evidência de workload.

### Higher isolation by default
Subir isolation sem identificar anomalia alvo e custo de contention.

### Breaking migration
Renomear/remover coluna no mesmo deploy em que versões antigas ainda podem executar.

### Pool multiplication
Aumentar pool por instância ignorando soma global de pods/processos.

### Backup theater
Celebrar backup job verde sem provar restore.

### Query tuning by intuition
Alterar índice/query sem olhar plano, cardinalidade e métricas reais.