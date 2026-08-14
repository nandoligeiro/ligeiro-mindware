# Repositories, Mapping e TTL

## Redis Repositories

Redis repositories mapeiam objetos para hashes e keyspaces.

Use quando:

- o acesso é por chave/id;
- o modelo encaixa em hash;
- queries são simples;
- TTL por entidade é natural.

## TTL

TTL é parte do modelo:

- sessão;
- token;
- cache;
- janela de rate limit;
- estado temporário de workflow.

Sem TTL, Redis tende a acumular lixo ou depender apenas de eviction.

## Índices Secundários

Índices em Redis têm custo e manutenção. Use só quando a consulta justifica.
