# DDD Cheatsheet

## Classificação de Subdomínios

| Tipo | Sinal | Estratégia |
|---|---|---|
| Core | Diferencia a empresa e muda bastante | Investir nos melhores modelos, pessoas e feedback rápido |
| Supporting | Necessário, mas não diferencial | Implementar bem o suficiente, sem overengineering |
| Generic | Problema comum de mercado | Comprar, terceirizar ou usar solução pronta quando possível |

## Bounded Context

- Um bounded context é a fronteira onde um modelo e sua linguagem têm significado consistente.
- Um subdomínio é parte do problema; um bounded context é parte da solução/modelagem.
- Um time pode possuir múltiplos contexts; um context deve ter ownership claro.
- Não tente criar “um modelo corporativo único” para todos os usos.

## Escolha Tática

| Situação | Padrão provável | Cuidado |
|---|---|---|
| Fluxo procedural simples | Transaction Script | Transações e duplicação |
| CRUD com pouca lógica | Active Record | Crescimento para big ball of mud |
| Regras ricas e invariantes | Domain Model | Agregados pequenos e consistentes |
| Histórico é o estado | Event-Sourced Domain Model | Versionamento de eventos e projeções |

## Integração Entre Contextos

| Relação | Use quando | Risco |
|---|---|---|
| Partnership | Times colaboram intensamente | Coordenação excessiva |
| Shared Kernel | Pequena parte precisa ser compartilhada | Acoplamento forte |
| Customer–Supplier | Upstream atende downstream conhecido | Downstream fica dependente |
| Conformist | Downstream aceita modelo upstream | Contaminação do modelo |
| Anticorruption Layer | Precisa proteger modelo local | Custo de tradução |
| Open-Host Service | API pública e estável para vários consumidores | Contrato vira produto |
| Published Language | Linguagem comum formalizada | Governança e evolução |
| Separate Ways | Integração custa mais que duplicação | Divergência futura |

## Arquitetura

- **Layered architecture**: separa apresentação, aplicação, domínio e infraestrutura.
- **Ports and adapters**: protege domínio de tecnologia externa.
- **CQRS**: separa escrita e leitura quando modelos/cargas divergem.
- **Microservices**: devem ser serviços profundos, com fronteiras de domínio, não endpoints minúsculos.

## Perguntas Rápidas

- “Que palavra significa coisas diferentes para pessoas diferentes?”
- “Qual regra, se errada, machuca o negócio?”
- “Que mudança esperamos que aconteça nos próximos 6 meses?”
- “Quem precisa aprovar uma alteração neste modelo?”
- “Estamos usando eventos de domínio ou mensagens técnicas disfarçadas?”
- “Essa fronteira reduz complexidade ou só distribui complexidade?”
