---
name: software-testing-engineering
description: "Ligeiro Mindware para projetar estratégia de testes orientada a risco e feedback: unit, integration, contract, end-to-end, Testcontainers, property-based testing, mutation testing, deterministic tests, consumer-driven contracts, fault injection, chaos testing e testability. Use quando o usuário precisar decidir o que testar, em qual nível, com qual evidência de sucesso e com qual custo de feedback."
metadata:
  short-description: Engenharia de testes orientada a risco e feedback
---

# Software Testing Engineering — Ligeiro Mindware

Use esta skill para transformar risco de software em evidência verificável. O objetivo não é aumentar contagem de testes; é reduzir incerteza com o menor custo de feedback possível.

## Ative quando
- for preciso desenhar estratégia de testes para serviço, integração, pipeline ou arquitetura;
- houver dúvida entre unit, integration, contract, component ou end-to-end;
- existirem flaky tests, excesso de mocks ou suíte lenta;
- for necessário provar comportamento em falhas, concorrência, contratos ou dependências reais;
- a discussão envolver Testcontainers, property-based, mutation testing, fault injection ou chaos.

## Não ative quando
- a dúvida for apenas sintaxe de JUnit/Mockito sem decisão de estratégia;
- o problema principal for confiabilidade distribuída, idempotência ou consistência; use `distributed-systems-engineering`;
- o foco for exclusivamente observabilidade em produção; use `observability-engineering`.

## Modelo mental

```text
risco -> hipótese -> nível de teste -> ambiente -> oráculo -> evidência -> feedback
```

Um teste é útil quando detecta uma classe relevante de defeito com custo aceitável e resultado confiável.

## Heurística de escolha

1. Nomeie o risco que precisa ser coberto.
2. Escolha o nível mais barato capaz de observar o comportamento real.
3. Evite mocks quando o risco está na integração.
4. Use contratos quando produtor e consumidor evoluem independentemente.
5. Use E2E apenas para jornadas críticas que exigem prova ponta a ponta.
6. Use property-based quando invariantes importam mais que exemplos específicos.
7. Use mutation testing para medir se a suíte detecta mudanças defeituosas reais.
8. Use fault injection/chaos quando a hipótese depende de falhas que o happy path nunca exercita.

## Matriz rápida

| Risco | Teste preferencial |
|---|---|
| regra pura | unit/property-based |
| mapping/serialização/SQL | integration |
| protocolo entre serviços | contract |
| banco/broker/cache real | integration + Testcontainers |
| jornada crítica | E2E seletivo |
| resiliência | fault injection/chaos |
| qualidade da própria suíte | mutation testing |

## Anti-padrões
- mockar tudo e chamar de integração;
- testar implementação em vez de comportamento;
- E2E como primeira linha de defesa;
- sleeps para sincronização;
- fixtures gigantes e compartilhadas;
- testes não determinísticos aceitos como “normal”;
- perseguir cobertura percentual sem conectar a risco;
- ignorar tempo de feedback da suíte.

## Saída esperada
Ao propor estratégia, explicite:
1. risco coberto;
2. tipo/nível de teste;
3. dependências reais ou simuladas;
4. evidência de sucesso;
5. custo/tempo de feedback;
6. falhas que continuam sem cobertura.

## Carregue sob demanda
- `references/test-levels.md`
- `references/advanced-techniques.md`
- `patterns.md`
- `cheatsheet.md`
