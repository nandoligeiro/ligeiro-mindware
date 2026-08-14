# Strategic Design

## Capítulos Cobertos

- Cap. 1 — Analyzing Business Domains
- Cap. 2 — Discovering Domain Knowledge
- Cap. 3 — Managing Domain Complexity
- Cap. 4 — Integrating Bounded Contexts

## Ideia-Mãe

Strategic design responde: “o que estamos construindo, por quê, para quem e com quais fronteiras de linguagem?” Antes de discutir código, entenda a estratégia do negócio e como a organização divide conhecimento, responsabilidade e vantagem competitiva.

## Business Domain e Subdomains

- O business domain é a área de atividade da empresa.
- Subdomains são partes menores do problema.
- A classificação de subdomínios guia investimento técnico.

### Core Subdomain

É onde a empresa compete de forma diferenciada. Merece o melhor design, ciclos rápidos de feedback e proteção contra soluções genéricas.

### Generic Subdomain

É complexo, mas comum no mercado. Comprar ou usar ferramentas prontas costuma ser melhor que reinventar.

### Supporting Subdomain

É necessário e específico, mas não diferencia a empresa. Faça com qualidade suficiente, sem gastar energia de core.

## Ubiquitous Language

Linguagem ubíqua é a ferramenta de descoberta e alinhamento. Ela não é glossário decorativo; é o vocabulário operacional usado por especialistas e desenvolvedores.

Use-a para:

- revelar contradições;
- nomear regras;
- reduzir tradução mental;
- orientar testes e APIs;
- detectar fronteiras de modelo.

## Bounded Contexts

Um bounded context protege a consistência de um modelo. O mesmo conceito do mundo real pode ter modelos diferentes em contexts diferentes.

Sinais de que você precisa separar contexts:

- o mesmo termo tem significados diferentes;
- times diferentes mudam regras por motivos diferentes;
- uma entidade acumula campos e comportamentos sem coesão;
- integrações exigem tradução constante;
- ciclos de mudança e ownership são distintos.

## Integração Entre Contexts

Ao integrar bounded contexts, escolha conscientemente a relação:

- **Cooperation**: partnership ou shared kernel.
- **Customer–supplier**: upstream atende downstream com relação explícita.
- **Separate ways**: integração não compensa.
- **Anticorruption layer**: proteja o modelo local quando o externo é instável ou conceitualmente diferente.

## Como Aplicar em Projetos

1. Liste capacidades do negócio.
2. Classifique cada uma como core/supporting/generic.
3. Encontre termos ambíguos e conflitos de linguagem.
4. Desenhe contexts com ownership.
5. Desenhe context map com contratos e relações de poder.
6. Escolha onde investir modelagem profunda.
