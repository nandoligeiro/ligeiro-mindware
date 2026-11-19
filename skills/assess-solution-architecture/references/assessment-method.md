# Método de Solution Architecture Assessment

## Evidências por seção

| Seção | Perguntas | Evidência/entrega |
|---|---|---|
| 1 | Por que agir, qual dor, custo e objetivo? | Problem statement e KPIs com baseline |
| 2 | Quem usa, mantém, influencia e aprova? | Mapa de stakeholders e expectativas |
| 3 | Quais fluxos existem, se sobrepõem ou faltam? | Matriz de capacidades e demonstrações |
| 4 | Como componentes, dados e deploy realmente funcionam? | Diagramas verificados, repositórios, pipelines, logs |
| 5 | O que entregar e como medir qualidade? | RFs, restrições e cenários mensuráveis |
| 6 | Quais opções e consequências? | Matriz de trade-offs, riscos, custo total e confiança |
| 7 | Qual hipótese arquitetural atende aos requisitos? | HLD candidato, contratos e ADRs |
| 8 | Como migrar sem interromper usuários? | Fases, owners, rollback, riscos e critérios de saída |

## Protocolo de classificação

- **Confirmado:** fonte rastreável, local/data e comportamento verificado.
- **Informado:** pessoa e data do relato; confirmar se material à decisão.
- **Hipótese:** dizer o que medir ou testar, quem e quando.
- **Desconhecido:** marcar lacuna; não converter ausência de evidência em nota ruim.

## Cenários de qualidade

Para cada atributo prioritário registrar: origem do estímulo, estímulo, contexto, componente afetado, resposta esperada e medida objetiva. Exemplo: acrescentar um novo módulo funcional sem alterar módulos existentes; testes de contrato aprovados; medir arquivos alterados, lead time e defeitos.

## Matriz de decisão

1. Definir critérios e pesos (total 100%) com os stakeholders.
2. Aplicar gates eliminatórios: segurança, privacidade, compliance e viabilidade operacional (Aprovado/Reprovado/Não avaliado).
3. Atribuir notas 1–5 somente com justificativa e evidência. Caso contrário N/A; não gerar ranking definitivo.
4. Comparar reaproveitamento, cobertura funcional, custo de implantação e operação, esforço de migração, segurança, testabilidade, observabilidade, evolutividade, prazo e reversibilidade.
5. Registrar análise de sensibilidade dos pesos e incerteza das estimativas.
6. Separar avaliação, recomendação condicional e ADR efetivamente aprovado.

## Checklist para sistemas criados com IA

- Build reproduzível, versionamento e dependências; SAST/SCA e segredos.
- Autenticação, autorização, trilha de auditoria, privacidade e dados sintéticos.
- Testes de caracterização, contrato, regressão e cenários negativos.
- Timeout, retry, idempotência, recuperação e isolamento de falhas quando aplicáveis.
- Logs correlacionados, métricas, rastreabilidade de execução e runbooks.
- Código modificável por terceiros, documentação, owners e CI/CD.
- Exercício prático de extensibilidade: acrescentar um gerador, medir alterações, testes e regressões.

## Checklist de conclusão

Oito seções na ordem; fatos e hipóteses separados; decisões ligadas a requisitos; opções comparadas; riscos críticos e gates explícitos; ADR não inventado; roadmap com continuidade do serviço.
