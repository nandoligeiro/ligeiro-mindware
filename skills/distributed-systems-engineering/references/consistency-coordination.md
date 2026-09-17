# Consistência, Ordering e Coordenação

## Consistência é requisito por operação

Não classifique o sistema inteiro como forte ou eventual. Liste invariantes e pergunte qual operação precisa observar qual estado.

Exemplos:

- saldo disponível pode exigir leitura consistente para autorizar gasto;
- feed ou analytics pode tolerar atraso;
- status de workflow pode convergir eventualmente desde que transições sejam monotônicas.

## Ordering

Mensagens podem chegar fora de ordem por retry, paralelismo, reparticionamento ou múltiplos produtores.

Antes de exigir ordering global, pergunte se ordering por entidade/chave é suficiente. Ordering global reduz paralelismo e aumenta acoplamento.

Técnicas:

- sequence/version por agregado;
- partition key estável;
- optimistic concurrency;
- ignore stale update quando versão recebida <= versão persistida;
- reorder buffer apenas quando custo e janela forem controlados.

## Optimistic concurrency

Use version/CAS quando conflitos são raros e detectar concorrência é suficiente.

Não esconda conflito com retry infinito. Reavalie regra de negócio quando duas decisões concorrentes são legítimas.

## Claim, lease e fencing

### Claim

Registra ownership lógico sobre um trabalho.

### Lease

Ownership expira e permite recuperação se o worker morrer. O lease exige relógio/TTL e política de renovação.

### Fencing token

Cada aquisição recebe token monotônico:

```text
worker A -> token 41
lease expires
worker B -> token 42
worker A wakes up and tries write(41)
storage rejects because 41 < 42
```

Sem fencing, um worker pausado pode continuar executando depois de perder ownership.

## Distributed locks

Use apenas se o recurso protegido consegue respeitar ownership e se a falha do lock service não cria efeito pior que a concorrência original.

Prefira invariantes no storage, unique constraints, versions e idempotency antes de lock distribuído quando possível.

## CAP de forma operacional

Durante partição:

- rejeitar/atrasar operação pode preservar uma invariante;
- aceitar localmente pode priorizar disponibilidade e exigir convergência posterior.

Documente a escolha por endpoint/comando, não como slogan da arquitetura inteira.
