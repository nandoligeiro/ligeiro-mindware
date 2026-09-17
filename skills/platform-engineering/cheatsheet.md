# Platform Engineering — Cheatsheet

## 10 perguntas
1. Quem é o usuário interno?
2. Qual job repetitivo estamos simplificando?
3. Qual capability é comum a vários times?
4. O que deve ser self-service?
5. Qual interface encaixa no fluxo real?
6. Quais defaults devem ser seguros por padrão?
7. O que precisa continuar visível para debug/custo/segurança?
8. Qual escape hatch existe?
9. Como medimos adoção e redução de fricção?
10. Quem é owner da capability?

## Atalhos
| Situação | Direção inicial |
| --- | --- |
| muitos tickets repetidos | self-service + automação |
| setups divergentes | golden path + policy as code |
| portal sem automação | resolver capability/backend primeiro |
| abstração escondendo falha | expor diagnostics e limites |
| caso especial legítimo | escape hatch explícito |
| baixa adoção | medir jobs, fricção e feedback antes de impor |

## Red flags
- portal = plataforma
- self-service com aprovação manual sempre
- template sem lifecycle
- abstração que impede diagnóstico
- golden path obrigatório para qualquer caso
- nenhuma métrica de uso/valor