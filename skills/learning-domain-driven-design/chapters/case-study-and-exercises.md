# Case Study and Exercises

## Apêndices Cobertos

- Appendix A — Applying DDD: A Case Study
- Appendix B — Answers to Exercise Questions

## Como Usar

Use este arquivo para transformar teoria em prática. Quando o usuário trouxer um sistema real, responda como se estivesse conduzindo um estudo de caso.

## Roteiro de Case Study

1. **Descreva a empresa**: mercado, clientes, fonte de receita e vantagem competitiva.
2. **Liste capacidades**: o que o negócio precisa fazer para operar.
3. **Classifique subdomínios**: core, supporting, generic.
4. **Colete linguagem**: termos usados por cada área.
5. **Ache conflitos**: mesmos termos com significados diferentes.
6. **Desenhe contexts**: modelo, dono, propósito e integrações.
7. **Escolha tática**: transaction script, active record, domain model ou event sourcing.
8. **Escolha arquitetura**: layered, ports/adapters, CQRS, eventos.
9. **Defina evolução**: o que monitorar para mudar fronteiras.

## Exercícios Práticos

### Exercício 1 — Classificação

Para cada capacidade, responda:

- Ela diferencia a empresa?
- Há solução pronta confiável?
- A regra muda frequentemente?
- Qual seria o custo de errar?

### Exercício 2 — Linguagem

Liste 10 termos de negócio. Para cada termo:

- quem usa;
- significado;
- sinônimos;
- conflitos;
- exemplo de uso em uma regra.

### Exercício 3 — Context Map

Para cada integração:

- upstream;
- downstream;
- contrato;
- padrão de relação;
- risco de acoplamento;
- estratégia de evolução.

### Exercício 4 — Padrão Tático

Escolha três casos de uso e classifique:

- complexidade;
- volatilidade;
- necessidade de consistência;
- padrão tático recomendado;
- estratégia de testes.
