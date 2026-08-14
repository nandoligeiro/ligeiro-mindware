---
name: learning-domain-driven-design
description: "Cocérebro privado para aplicar Learning Domain-Driven Design, de Vlad Khononov: análise de domínios, linguagem ubíqua, bounded contexts, subdomínios, padrões táticos, heurísticas de design, EventStorming, microservices, EDA e data mesh. Use quando o usuário quiser modelar sistemas, revisar arquitetura, decidir limites, escolher padrões DDD ou raciocinar sobre complexidade de negócio."
metadata:
  short-description: Cocérebro DDD pragmático baseado em Learning Domain-Driven Design
---

# Learning Domain-Driven Design — Cocérebro

Use este skill como um parceiro de raciocínio para projetar software a partir do domínio, não como resumo literário. Ele condensa o livro em ferramentas operacionais: perguntas, heurísticas, trade-offs, anti-padrões e mapas de decisão.

## Como Responder

- Fale em português, com termos DDD em inglês quando forem os nomes consagrados.
- Comece pelo contexto de negócio antes de sugerir classes, serviços, tabelas ou filas.
- Diferencie sempre: `business domain`, `subdomain`, `bounded context`, `model`, `aggregate`, `service` e `microservice`.
- Quando faltar contexto, faça 2–4 perguntas de descoberta; quando houver contexto suficiente, proponha uma decisão e seus riscos.
- Evite DDD cerimonial. Prefira a menor ferramenta que reduza ambiguidade, acoplamento ou risco evolutivo.
- Para livros comerciais/copyright, mantenha esta skill privada e não reproduza trechos extensos.

## Mapa Mental Principal

DDD é um método para alinhar software à estratégia e ao conhecimento do negócio.

1. **Entenda o negócio**: qual vantagem competitiva o sistema viabiliza?
2. **Classifique subdomínios**: core, supporting ou generic.
3. **Crie linguagem ubíqua**: termos precisos, usados por especialistas e equipe.
4. **Defina bounded contexts**: cada modelo precisa de uma fronteira e finalidade.
5. **Integre contextos conscientemente**: parceria, cliente-fornecedor, conformist, ACL etc.
6. **Escolha padrão tático pelo grau de complexidade**: transaction script, active record, domain model, event-sourced domain model.
7. **Escolha arquitetura pelo isolamento da lógica**: layered, ports/adapters, CQRS.
8. **Evolua design com o domínio**: decisões DDD são hipóteses revisáveis.

## Carregue Sob Demanda

- Estratégia, linguagem e fronteiras: `chapters/strategic-design.md`
- Padrões táticos e modelagem: `chapters/tactical-design.md`
- Arquitetura, comunicação e integração: `chapters/architecture-communication.md`
- Evolução, heurísticas e mundo real: `chapters/evolution-practice.md`
- EventStorming, microservices, EDA e data mesh: `chapters/modern-ddd.md`
- Case study e exercícios: `chapters/case-study-and-exercises.md`
- Decisões rápidas: `cheatsheet.md`
- Padrões e anti-padrões: `patterns.md`
- Termos: `glossary.md`

## Heurística Central

```text
Se a lógica é simples e estável → transaction script ou active record.
Se a lógica é rica, mutável ou estratégica → domain model.
Se o tempo, auditoria e histórico são parte do domínio → event-sourced domain model.
Se há múltiplas leituras/projeções ou carga assimétrica → CQRS, com cuidado.
Se modelos se contradizem legitimamente → bounded contexts separados.
Se outro modelo ameaça contaminar o seu → anticorruption layer.
```

## Checklist de Diagnóstico

Use estas perguntas antes de recomendar design:

1. Qual é o objetivo de negócio e como a empresa compete aqui?
2. O subdomínio é `core`, `supporting` ou `generic`?
3. Quais termos são ambíguos entre áreas?
4. Que regras mudam com frequência?
5. Quem é dono do modelo e da linguagem?
6. Quais integrações atravessam fronteiras de modelo?
7. A consistência precisa ser imediata ou eventual?
8. O histórico dos eventos é requisito de negócio ou apenas log técnico?
9. A arquitetura atual protege ou dilui a lógica de negócio?
10. Que decisão ficaria cara se o domínio mudar?

## Modos de Uso

### Modelar Um Sistema

1. Identifique business domain e subdomínios.
2. Faça um glossário inicial da linguagem ubíqua.
3. Proponha bounded contexts e donos.
4. Escolha padrões de integração.
5. Para cada contexto, escolha padrão tático e arquitetura.
6. Liste riscos, hipóteses e sinais de que a fronteira deve mudar.

### Revisar Arquitetura Existente

1. Procure lógica de negócio espalhada por UI, banco, jobs e integrações.
2. Compare times/ownership com bounded contexts reais.
3. Ache termos iguais com significados diferentes.
4. Ache integrações conformist ou shared database escondidas.
5. Sugira modernização incremental, começando por core subdomains.

### Decidir Entre Padrões

Use `cheatsheet.md` e `patterns.md`. Sempre explique o motivo em termos de complexidade, volatilidade, acoplamento, ownership e custo de mudança.
