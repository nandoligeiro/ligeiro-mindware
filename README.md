# Ligeiro Mindware

> Conhecimento que deixa de ser arquivo e passa a ser capacidade.

Biblioteca pessoal de **mindware**: skills, referências e ferramentas que transformam livros, documentações e frameworks em conhecimento estruturado, reutilizável e acionável por agentes de IA.

O projeto nasce integrado ao Codex, mas a ideia é maior do que uma ferramenta específica: criar uma camada pessoal de conhecimento que possa evoluir, ser combinada e aplicada em diferentes contextos.

## O que é mindware?

Mindware é conhecimento empacotado para uso prático. Em vez de apenas armazenar notas, este repositório organiza conceitos, padrões, decisões e instruções em skills que um agente consegue consultar e aplicar.

Cada skill pode reunir:

- instruções operacionais em `SKILL.md`;
- resumos e cheatsheets;
- glossários;
- padrões e exemplos;
- capítulos ou referências complementares.

O contrato portátil de cada skill é o padrão `SKILL.md`, com `name` e `description` no frontmatter. O catálogo pode ser instalado em agentes compatíveis e, em uma etapa posterior, empacotado com APM.

## Estrutura

```text
ligeiro-mindware/
├── AGENTS.md
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md
│       ├── cheatsheet.md
│       ├── glossary.md
│       ├── patterns.md
│       └── chapters/
├── evals/
├── docs/
└── tools/
    ├── book-to-skill/
    ├── docs-to-skill/
    └── skill-engineering/
```

## Fluxo para novas skills

1. Coloque o livro ou documento localmente fora do Git — ou em `sources/` apenas durante o processamento.
2. Use o conversor adequado em `tools/`.
3. Grave o resultado final em `skills/<slug>/`.
4. Revise e valide `skills/<slug>/SKILL.md`.
5. Crie ou atualize cenários em `evals/` quando mudar ativação, fluxo ou saída.
6. Faça commit apenas dos artefatos derivados permitidos, nunca dos arquivos-fonte protegidos.

Validação estrutural:

```bash
python3 tools/skill-engineering/validate_skills.py
```

## Instalação em agentes compatíveis

Para uso direto em ferramentas que descobrem o padrão `.agents/skills`, copie a pasta da skill desejada para o catálogo do projeto ou do usuário.

### Windows — PowerShell

```powershell
Copy-Item -Recurse -Force .\skills\<slug> "$env:USERPROFILE\.agents\skills\<slug>"
```

### macOS ou Linux

```bash
mkdir -p ~/.agents/skills
cp -R ./skills/<slug> ~/.agents/skills/<slug>
```

Esse formato é compatível com o Devin Desktop/Local quando a skill está no catálogo `.agents/skills`. Para instalações legadas do Codex, `~/.codex/skills` continua sendo uma alternativa local.

O manifesto e o fluxo de empacotamento APM serão adicionados depois de validarmos a separação entre fonte de autoria e artefato distribuível; isso evita manter duas cópias divergentes das mesmas skills.

## Princípios

- **Conhecimento acionável:** menos arquivo morto, mais capacidade aplicável.
- **Estrutura antes de volume:** uma skill útil vale mais do que uma pasta cheia de notas.
- **Portabilidade:** o conteúdo não deve depender para sempre de um único agente ou plataforma.
- **Avaliação:** ativação correta, fluxo correto e saída verificável fazem parte da qualidade.
- **Curadoria humana:** automação acelera; julgamento continua sendo responsabilidade de quem usa.
- **Respeito às fontes:** síntese e transformação não significam redistribuição indevida.

## Política para o repositório público

Este repositório contém material autoral, referências públicas e sínteses transformativas. As skills não substituem as fontes originais e não devem reproduzir trechos extensos de livros, cursos ou documentações protegidas.

Não versione PDFs, EPUBs, exports privados, credenciais, dados pessoais, documentos internos, snapshots integrais de documentação ou qualquer arquivo-fonte que não possa ser redistribuído legalmente. Consulte sempre a licença e os termos da fonte antes de reutilizar o conteúdo.

O arquivo `LICENSE` cobre apenas código, ferramentas e outros artefatos originais explicitamente produzidos neste projeto. Marcas, APIs, livros, documentações e demais conteúdos de terceiros permanecem sujeitos aos seus respectivos titulares e termos.

---

**Ligeiro Mindware** — conhecimento organizado para pensar melhor, decidir melhor e construir melhor.