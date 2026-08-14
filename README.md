# Cocérebro Skills

Repositório privado para manter skills pessoais de livros, documentos e frameworks que viram extensões cognitivas reutilizáveis no Codex.

## Estrutura

```text
skills/
  learning-domain-driven-design/
    SKILL.md
    cheatsheet.md
    glossary.md
    patterns.md
    chapters/
tools/
  book-to-skill/
sources/
  README.md
```

## Fluxo Para Novas Skills

1. Coloque o livro/documento localmente fora do Git ou em `sources/` apenas temporariamente.
2. Rode o conversor em `tools/book-to-skill/`.
3. Grave a skill final em `skills/<slug>/`.
4. Valide `skills/<slug>/SKILL.md`.
5. Faça commit apenas dos artefatos de skill, não dos PDFs/EPUBs originais.

## Instalação Local no Codex

Para usar uma skill no Codex, copie a pasta da skill para:

```powershell
$env:USERPROFILE\.codex\skills\<slug>
```

Exemplo:

```powershell
Copy-Item -Recurse -Force .\skills\learning-domain-driven-design $env:USERPROFILE\.codex\skills\learning-domain-driven-design
```

Depois, reinicie o Codex para carregar novas skills.

## Privacidade

Este repo deve permanecer privado. As skills podem conter sínteses estruturais de livros comerciais ou documentos internos. Não versionar arquivos-fonte com copyright, como PDFs, EPUBs ou exports privados.
