# Patterns e anti-patterns

## Patterns

### Risk-to-test mapping
Comece pelo risco e derive o nível de teste. Evita suítes guiadas por hábito de framework.

### Real dependency at the boundary
Quando o risco está em SQL, serialização, broker ou cache, teste a fronteira com implementação real/efêmera em vez de mockar exatamente o comportamento que precisa provar.

### Contract as compatibility firewall
Proteja evolução independente de consumidores e produtores com contratos verificáveis.

### Deterministic fixture
Cada cenário controla seus dados, clock e IDs; execução paralela não interfere em vizinhos.

### Failure rehearsal
Transforme incidentes e bugs reais em testes de regressão, incluindo failure modes e não apenas o happy path.

## Anti-patterns

### Mock theater
Muitos mocks produzem teste verde de um mundo que não existe.

### Coverage worship
Cobertura alta sem assertions úteis cria falsa confiança.

### E2E monoculture
Toda validação depende do ambiente completo; feedback lento e diagnóstico ruim.

### Flaky by design
Sleep, estado global, clock real e dependências compartilhadas tornam o teste probabilístico.

### Happy-path completeness
A suíte parece completa, mas nunca exerce timeout, erro parcial, concorrência ou dados inesperados.

### Test code as disposable
Código de teste sem design acumula duplicação e fragilidade até virar obstáculo de mudança.
