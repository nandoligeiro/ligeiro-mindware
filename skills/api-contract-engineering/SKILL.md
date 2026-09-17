---
name: api-contract-engineering
description: "Ligeiro Mindware para projetar, evoluir e verificar contratos entre serviços e consumidores: APIs HTTP, eventos, schemas, compatibilidade, versionamento, consumer-driven contracts, depreciação e governança. Use quando a mudança atravessar uma fronteira de integração e puder quebrar consumidores, produtores ou fluxos independentes."
metadata:
  short-description: Engenharia de contratos e compatibilidade
---

# API Contract Engineering

Trate contratos como **comportamento público verificável**, não como arquivo de schema.

## Ativação

Use esta skill quando houver:
- API ou evento consumido por outro processo/time/sistema;
- mudança de request, response, status code, header, schema ou semântica;
- compatibilidade backward/forward em discussão;
- versionamento, depreciação ou migração de consumidores;
- necessidade de contract testing ou governança de interface.

Não ative para:
- sintaxe local de controller/client;
- refactor interno sem efeito observável no consumidor;
- modelagem de domínio sem fronteira de integração;
- tuning de transporte sem mudança contratual.

## Modelo mental

Separe sempre:
1. **shape** — campos, tipos, headers, tópicos, envelopes;
2. **semantics** — significado, invariantes, erros, ordering, idempotência esperada;
3. **compatibility** — quem quebra quando um lado muda;
4. **lifecycle** — ownership, versão, depreciação, sunset e migração;
5. **verification** — como provar que provider e consumer continuam compatíveis.

Um schema válido pode continuar sendo um contrato quebrado se a semântica mudou.

## Fluxo de análise

1. Identifique provider, consumers e fronteira pública.
2. Declare o comportamento atual observado, não apenas o schema.
3. Classifique o contrato: request/response, async event, callback/webhook, batch/file ou outro.
4. Liste invariantes e dependências dos consumidores.
5. Classifique a mudança: additive, restrictive, semantic, removal ou transport-only.
6. Avalie backward e forward compatibility por consumer relevante.
7. Prefira evolução compatível antes de criar nova versão.
8. Defina verificação automatizada: schema, contract test, examples, compatibility check ou replay.
9. Defina rollout/depreciação: telemetry, adoption, deadline, fallback e ownership.
10. Registre risco residual e evidência de sucesso.

## Heurísticas

### Mudanças normalmente mais seguras
- adicionar campo opcional com semântica clara;
- adicionar novo endpoint/operação sem alterar os existentes;
- ampliar enum apenas quando consumidores toleram valores desconhecidos;
- publicar nova versão de evento em paralelo quando a semântica realmente diverge.

### Mudanças potencialmente quebráveis
- tornar campo opcional obrigatório;
- remover/renomear campo;
- mudar significado mantendo o mesmo nome/tipo;
- alterar unidade, timezone, precisão ou default;
- mudar status/error mapping usado por consumidores;
- adicionar enum value quando consumidores fazem switch exaustivo;
- trocar ordering/deduplication semantics sem explicitar.

### Versionamento

Não use nova versão para esconder qualquer mudança. Versione quando não houver caminho compatível razoável ou quando a semântica representar um contrato novo.

### Consumer-driven contracts

Use CDC quando consumers independentes expressam expectativas relevantes que o provider precisa preservar. Não substitui testes de integração reais quando transporte, serializer, auth, proxy ou infraestrutura também fazem parte do risco.

### Async contracts

Para eventos, explicite pelo menos:
- event name/type;
- aggregate/entity identity;
- schema e semântica dos campos;
- ordering esperado, se houver;
- duplicate tolerance/idempotency expectation;
- compatibility policy;
- ownership e replay assumptions.

## Saída esperada

Uma resposta boa deve declarar:
- fronteira, provider e consumers;
- contrato observado e invariantes;
- classificação da mudança;
- compatibilidade e quem pode quebrar;
- estratégia de evolução/versionamento;
- evidência automatizada de compatibilidade;
- rollout/depreciação e risco residual.

Consulte `patterns.md` e `cheatsheet.md` para decisões rápidas.