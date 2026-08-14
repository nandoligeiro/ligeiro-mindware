# docs-to-skill

Ferramenta simples para transformar documentação pública versionada em insumos de skills.

## Objetivo

`docs-to-skill` não copia documentação inteira. Ele cria um snapshot de navegação e fontes oficiais para ajudar a gerar uma skill operacional com:

- links oficiais;
- versão/data de captura;
- mapa de seções;
- tópicos principais;
- arquivos de skill mantidos em `skills/<slug>/`.

## Uso

```powershell
python tools\docs-to-skill\docs_to_skill.py spring-framework
```

O comando gera:

```text
sources/spring-framework-docs-snapshot.json
sources/spring-framework-sources.md
```

## Configuração

Os targets conhecidos ficam em `targets.json`. Para um novo projeto, adicione:

- `slug`
- `name`
- `version_hint`
- `sources`

Depois use o snapshot para criar ou atualizar uma skill.

## Política

Use somente documentação que você pode acessar publicamente ou tem direito de usar. Versione links, mapas e sínteses operacionais; evite copiar páginas inteiras.
