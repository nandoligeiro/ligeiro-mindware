# Software Delivery Engineering — Patterns

## Patterns

### Build once, promote many
Gere uma vez, identifique por digest/versão imutável e promova o mesmo conteúdo entre ambientes.

### Environment-specific configuration
Separe config/secret/policy do artefato para evitar rebuild por ambiente.

### Progressive delivery
Exponha gradualmente com métricas, thresholds e abort criteria definidos antes do rollout.

### Feature flag release
Separe deploy técnico da ativação de comportamento quando isso reduz blast radius.

### Evidence chain
Conecte commit -> artifact digest -> verificações -> promoção -> deployment.

### Rollforward-first when stateful
Quando schema/dados tornam rollback arriscado, prepare correção compatível e convergente.

## Anti-patterns

### Rebuild per environment
Hom e produção recebem conteúdos diferentes embora tenham o mesmo source intent.

### Mutable promoted artifact
Mesma versão pode mudar depois de validada.

### Tag pollution
Cada tentativa operacional cria versão/tag nova sem representar nova mudança de software.

### Stage theater
Muitos ambientes/gates sem risco ou evidência específica que justifique cada etapa.

### Canary without signals
Canary sem métricas, thresholds ou abort policy vira rollout manual mais lento.

### Long-lived integration branch
Mudanças acumulam e só descobrem conflito/incompatibilidade tarde.

### Rollback by wishful thinking
Plano de rollback ignora schema migration, side effects e irreversibilidade de dados.