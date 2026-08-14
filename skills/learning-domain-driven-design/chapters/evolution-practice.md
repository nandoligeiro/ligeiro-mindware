# Evolution and Practice

## Capítulos Cobertos

- Cap. 11 — Evolving Design Decisions
- Cap. 13 — Domain-Driven Design in the Real World

## Ideia-Mãe

Design DDD é uma aposta informada, não uma fotografia eterna. Domínios, organizações, conhecimento e escala mudam; fronteiras e padrões precisam evoluir.

## Vetores de Mudança

### Mudança no Domínio

Subdomínios podem mudar de categoria. Um generic pode virar core se a empresa decide competir ali; um core pode virar commodity com o tempo.

### Mudança Organizacional

Estrutura de times influencia bounded contexts e vice-versa. Ownership confuso costuma gerar modelos confusos.

### Mudança no Conhecimento

À medida que especialistas e desenvolvedores aprendem mais, a linguagem muda. Refatorar nomes e fronteiras é parte do processo.

### Crescimento

Carga, escala, base de usuários e número de times podem transformar decisões boas em gargalos.

## Modernização Incremental

1. Entenda o domínio atual.
2. Mapeie contexts existentes, mesmo que implícitos.
3. Ache core subdomains mal protegidos.
4. Crie anticorruption layers nas fronteiras mais tóxicas.
5. Extraia ou redesenhe por fatias de capacidade de negócio.
6. Não comece separando tudo em microservices.

## DDD no Mundo Real

DDD raramente começa em laboratório perfeito. Use-o como ferramenta para melhorar comunicação e decisões, não como checklist rígido.

Boas intervenções pequenas:

- renomear conceitos ambíguos;
- desenhar um context map;
- rodar EventStorming de um processo crítico;
- isolar uma regra core em domain model;
- criar uma ACL onde um sistema legado contamina o novo;
- transformar um serviço genérico em solução comprada.
