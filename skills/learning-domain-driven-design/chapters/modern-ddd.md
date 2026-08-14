# Modern DDD

## Capítulos Cobertos

- Cap. 12 — EventStorming
- Cap. 14 — Microservices
- Cap. 15 — Event-Driven Architecture
- Cap. 16 — Data Mesh

## EventStorming

EventStorming é uma técnica colaborativa para descobrir processos usando eventos como linha temporal.

Elementos comuns:

- domain events;
- commands;
- actors;
- policies;
- external systems;
- hotspots;
- read models;
- aggregates ou candidate boundaries.

Use quando:

- precisa descobrir linguagem ubíqua;
- há processo com muitos stakeholders;
- há conhecimento tácito;
- o sistema legado precisa ser compreendido;
- quer identificar boundaries antes de desenhar serviços.

## Microservices

Microservice bom é serviço profundo: interface pequena, comportamento significativo e fronteira de domínio clara.

Não confunda:

- bounded context com microservice;
- aggregate com microservice;
- endpoint pequeno com serviço bem modelado.

Boas fronteiras vivem entre:

- maiores que aggregates;
- iguais ou menores que bounded contexts;
- alinhadas com capacidade de negócio e ownership.

## Event-Driven Architecture

Eventos podem desacoplar no tempo, mas também podem criar caos sem semântica e contratos claros.

Tipos úteis:

- **Event notification**: avisa que algo ocorreu; consumidor busca detalhes.
- **Event-carried state transfer**: carrega estado suficiente para o consumidor.
- **Domain event**: expressa fato relevante na linguagem do domínio.

Use EDA com DDD quando eventos representam fatos reais e contexts têm contratos explícitos.

## Data Mesh

Data mesh aplica pensamento de domínio a dados analíticos. Em vez de centralizar tudo em um lago/armazém monolítico, trata dados como produtos pertencentes a domínios.

Princípios:

- decompor dados por domínio;
- tratar data products como produtos;
- habilitar plataforma self-service;
- governança federada.

Relação com DDD:

- bounded contexts ajudam a definir ownership de dados;
- linguagem ubíqua melhora semântica dos datasets;
- diferença entre OLTP e OLAP deve ser explícita.
