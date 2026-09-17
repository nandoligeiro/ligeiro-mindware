# Threat Modeling

## Objetivo

Threat modeling aqui é uma ferramenta de engenharia para descobrir attack paths antes de transformar o sistema em produção, não um ritual documental.

## Passo 1 — Assets

Liste o que precisa ser protegido:

- dados pessoais/financeiros;
- credenciais e tokens;
- operações privilegiadas;
- integridade de eventos e comandos;
- artifacts de build;
- configuração e secrets;
- disponibilidade de capacidades críticas.

## Passo 2 — Trust boundaries

Marque pontos em que confiança muda:

```text
user -> edge -> service -> broker -> worker -> database
                 |
                 +-> third party

source -> CI runner -> registry -> deployment
```

Toda mudança de identidade, conta, rede, processo ou administração é candidata a boundary.

## Passo 3 — Threats

Pergunte, para cada boundary:

- identidade pode ser falsificada?
- input pode alterar comando/query/config?
- ator pode acessar recurso de outro usuário/tenant?
- mensagens/artefatos podem ser modificados ou reproduzidos?
- segredo pode vazar em logs, build, trace, crash ou source?
- dependência ou action externa executa com quais privilégios?
- operação cara pode ser abusada para degradar disponibilidade?

STRIDE pode ajudar como checklist mental, mas não substitui o conhecimento do domínio.

## Passo 4 — Attack paths

Evite listar vulnerabilidades soltas. Modele caminhos:

```text
attacker controls input
  -> input reaches privileged parser
  -> parser calls internal service
  -> internal service trusts caller
  -> sensitive operation executes
```

Um caminho claro melhora a escolha do controle.

## Passo 5 — Controles

Priorize:

1. remover a capacidade perigosa quando possível;
2. reduzir privilégio/blast radius;
3. validar/autorização perto do recurso;
4. separar boundaries e identidades;
5. proteger integridade/confidencialidade;
6. detectar abuso e permitir resposta.

## Passo 6 — Evidência

Exemplos:

- teste negativo para acesso cruzado entre tenants;
- policy que bloqueia artifact não assinado;
- teste de token expirado/audience incorreta;
- pipeline que falha quando secret é detectado;
- teste de autorização por ownership;
- auditoria de permission scopes do CI.

## Residual risk

Nenhum controle zera risco. Registre o que permanece possível, o impacto, a detectabilidade e o mecanismo de resposta.
