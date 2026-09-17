# Test levels e feedback

## Unit
Use para regras puras, invariantes locais e lógica determinística. Deve ser rápido, isolado e barato de diagnosticar.

## Integration
Use quando o risco está na integração real: SQL, mapping ORM, serialização, broker, cache, filesystem, HTTP client ou configuração de framework. Prefira dependências efêmeras/reais quando mocks esconderiam comportamento relevante.

## Contract
Use quando a compatibilidade entre produtor e consumidor é o risco. Verifique shape, semântica, versionamento e expectativas mínimas. Contract test não substitui integração completa; protege a fronteira.

## End-to-end
Reserve para poucas jornadas críticas. Alto valor quando existe risco sistêmico que nenhum teste menor consegue observar; alto custo de execução e diagnóstico.

## Diamond vs pyramid
Não trate pirâmide como dogma. Sistemas orientados a integração podem precisar mais testes de integração do que unitários. A forma da suíte deve refletir onde o risco realmente está.

## Testcontainers
Use para banco, broker, cache e dependências compatíveis quando fidelidade de runtime importa. Evite transformar cada teste em bootstrap caro: reutilize setup por escopo adequado e mantenha dados independentes.

## Feedback budget
Classifique a suíte por janela de feedback:
- segundos: PR inner loop;
- poucos minutos: integração principal;
- dezenas de minutos: regressão ampla;
- mais longo: E2E/chaos/agendados.

Uma suíte correta que demora tanto que ninguém roda antes do merge também é um problema de engenharia.
