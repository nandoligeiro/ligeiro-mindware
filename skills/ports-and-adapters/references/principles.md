# Fundamentos de Ports and Adapters

## Ideia Central

Ports and Adapters, ou Arquitetura Hexagonal, isola a lógica de negócio em um núcleo que não conhece banco, HTTP, fila, framework ou serialização. O sistema passa a ter um centro estável, cercado por adaptadores substituíveis.

Use a metáfora do hexágono como fronteira: o domínio fala por contratos; qualquer tecnologia precisa traduzir sua linguagem para a linguagem do domínio.

## Complexidades

- **Essencial**: comportamento que existe porque o negócio existe.
- **Mandatória**: tecnologia inevitável para executar o negócio.
- **Acidental**: custo criado por acoplamento indevido entre negócio e tecnologia.

O design hexagonal tenta impedir que complexidade mandatória vire complexidade acidental.

## Comparação com Controller-Service-Persistence

No desenho clássico, o fluxo costuma ser:

`Controller -> Service -> Repository -> Database`

Esse modelo fica perigoso quando:

- controllers decidem regra de negócio;
- services viram orquestradores de frameworks;
- repositories influenciam o formato do domínio;
- entidades de persistência são também objetos de resposta HTTP;
- mudanças no banco quebram serviço e controller;
- testes de regra dependem de Spring, banco ou container.

No desenho hexagonal, o fluxo conceitual vira:

`Driving Adapter -> Input Port -> Domain/Application -> Output Port -> Driven Adapter`

O domínio define o que oferece e o que precisa. A infraestrutura apenas implementa traduções.

## Vocabulário

- **Domínio**: regras, invariantes, entidades, value objects e políticas centrais.
- **Application service / use case**: coordena uma intenção de negócio sem saber detalhes técnicos externos.
- **Porta de entrada / API**: contrato que permite acionar uma capacidade do domínio.
- **Porta de saída / SPI**: contrato que expressa uma necessidade do domínio para fora.
- **Adaptador de entrada / driving adapter**: REST controller, consumidor Kafka, job, CLI, GraphQL resolver, UI handler.
- **Adaptador de saída / driven adapter**: JPA repository adapter, HTTP client, broker producer, cache adapter, filesystem adapter.
- **Camada anticorrupção**: tradução que impede formatos externos ruins de contaminar o domínio.

## Heurísticas de Design

- Nomeie portas com verbos de negócio: `RegisterCustomer`, `ApproveLoan`, `QuoteShipment`.
- Nomeie SPIs pelo que o domínio precisa: `LoadCustomer`, `ReserveCredit`, `PublishInvoiceApproved`.
- Evite portas genéricas como `CustomerRepository` quando o caso de uso exige intenção mais específica.
- Evite que portas retornem tipos técnicos como `Page`, `ResponseEntity`, `Optional` de entidade JPA, `ConsumerRecord` ou `ResultSet`.
- Aceite que mapeamento é trabalho arquitetural legítimo; ele protege o domínio.

## Quando Não Forçar

Evite exagerar em casos CRUD triviais, protótipos descartáveis ou contextos sem regra de negócio relevante. Mesmo nesses casos, mantenha uma fronteira mínima para não expor domínio diretamente por HTTP ou persistência.
