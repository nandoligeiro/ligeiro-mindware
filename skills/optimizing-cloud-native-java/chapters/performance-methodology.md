# Metodologia de Performance

## Capítulos Cobertos

- Cap. 1 — Optimization and Performance Defined
- Cap. 2 — Performance Testing Methodology

## Ideia-Mãe

Performance é ciência experimental: formular perguntas, medir, controlar variáveis e interpretar resultados estatisticamente. Sem isso, otimização vira superstição.

## Defina Performance

Performance pode significar:

- latência;
- throughput;
- utilização de recursos;
- custo;
- capacidade;
- confiabilidade sob carga;
- experiência percebida.

Uma melhoria em uma dimensão pode piorar outra.

## Testes de Performance

Use o teste certo para a pergunta:

- **Latency test**: tempo de transação.
- **Throughput test**: taxa máxima sustentável.
- **Stress test**: ponto de quebra.
- **Load test**: comportamento na carga esperada.
- **Endurance test**: degradação ao longo do tempo.
- **Capacity planning**: recurso limitante e expansão.
- **Degradation test**: comportamento com falha parcial.

## Estatística e Psicologia

- Não confie em uma única execução.
- Olhe distribuição, não apenas média.
- Cuidado com outliers e viés de confirmação.
- Defina sucesso antes de rodar experimento.
- Repita em ambiente representativo.

## Receita de Investigação

1. Escreva a pergunta quantitativa.
2. Defina workload e dados.
3. Registre ambiente: JDK, flags, CPU, memória, container, rede.
4. Rode baseline.
5. Faça uma alteração.
6. Compare percentis, throughput, CPU, memória, GC e custo.
7. Documente conclusão e incertezas.
