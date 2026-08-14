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

## Estrutura

```text
ligeiro-mindware/
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md
│       ├── cheatsheet.md
│       ├── glossary.md
│       ├── patterns.md
│       └── chapters/
├── tools/
│   ├── book-to-skill/
│   └── docs-to-skill/
└── sources/
    └── README.md
```

## Fluxo para novas skills

1. Coloque o livro ou documento localmente fora do Git — ou em `sources/` apenas durante o processamento.
2. Use o conversor adequado em `tools/`.
3. Grave o resultado final em `skills/<slug>/`.
4. Revise e valide `skills/<slug>/SKILL.md`.
5. Faça commit apenas dos artefatos derivados permitidos, nunca dos arquivos-fonte protegidos.

## Instalação no Codex

Copie a pasta da skill desejada para o diretório local de skills do Codex.

### Windows — PowerShell

```powershell
Copy-Item -Recurse -Force .\skills\<slug> "$env:USERPROFILE\.codex\skills\<slug>"
```

### macOS ou Linux

```bash
cp -R ./skills/<slug> ~/.codex/skills/<slug>
```

Depois, reinicie o Codex para carregar a nova skill.

## Princípios

- **Conhecimento acionável:** menos arquivo morto, mais capacidade aplicável.
- **Estrutura antes de volume:** uma skill útil vale mais do que uma pasta cheia de notas.
- **Portabilidade:** o conteúdo não deve depender para sempre de um único agente ou plataforma.
- **Curadoria humana:** automação acelera; julgamento continua sendo responsabilidade de quem usa.
- **Respeito às fontes:** síntese e transformação não significam redistribuição indevida.

## Privacidade e direitos autorais

Este repositório deve permanecer privado. As skills podem conter sínteses estruturais de livros comerciais, documentações restritas ou materiais internos.

Não versione PDFs, EPUBs, exports privados, credenciais, dados sensíveis ou qualquer arquivo-fonte que não possa ser redistribuído legalmente.

---

**Ligeiro Mindware** — conhecimento organizado para pensar melhor, decidir melhor e construir melhor.
