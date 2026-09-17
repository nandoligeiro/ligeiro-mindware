# API Contract Engineering — Patterns

## Patterns

### Additive evolution
Prefira mudanças que preservem consumidores existentes: campos opcionais, novas operações e extensões com defaults explícitos.

### Parallel contract migration
Quando a semântica muda de verdade, rode contrato antigo e novo em paralelo, meça adoção e só depois faça sunset.

### Consumer-driven contract
Consumidores publicam expectativas executáveis e o provider as valida antes de release.

### Compatibility gate
Compare schema/contract atual contra baseline publicada e bloqueie breaking change não autorizada.

### Semantic changelog
Documente mudança de significado, não apenas diff estrutural.

### Observed deprecation
Deprecação só termina quando telemetry mostra que consumers reais migraram.

## Anti-patterns

### Schema equals contract
Assumir que JSON/OpenAPI/Avro válido prova compatibilidade semântica.

### Version everything
Criar `/v2` para qualquer mudança pequena e acumular contratos órfãos.

### Silent semantic change
Manter o mesmo campo/tipo e trocar significado, unidade, default ou timezone.

### Consumer guessing
Provider altera comportamento sem inventariar consumidores e suas expectativas.

### Breaking enum expansion
Adicionar valor de enum supondo que todos os consumers toleram desconhecidos.

### Eternal deprecation
Marcar como deprecated sem owner, deadline, telemetry ou plano de remoção.

### Contract test theater
Mock provider e consumer do mesmo jeito, sem validar o contrato publicado ou o transporte relevante.