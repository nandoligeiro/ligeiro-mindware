#!/usr/bin/env python3
"""Validate Agent Skills stored below a catalog directory."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_END = "---"


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != FRONTMATTER_END:
        return {}, ["SKILL.md precisa começar com frontmatter YAML"]

    end = None
    for index in range(1, len(lines)):
        if lines[index].strip() == FRONTMATTER_END:
            end = index
            break
    if end is None:
        return {}, ["frontmatter YAML não foi encerrado"]

    values: dict[str, str] = {}
    errors: list[str] = []
    current_key: str | None = None
    for raw_line in lines[1:end]:
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):(?:[ \t]+(.*))?$", raw_line)
        if match:
            current_key = match.group(1)
            values[current_key] = (match.group(2) or "").strip().strip("\"'")
            continue
        if current_key in {"description"} and raw_line.startswith((" ", "\t")):
            values[current_key] = (values[current_key] + " " + raw_line.strip()).strip()
            continue
        errors.append(f"linha de frontmatter inválida: {raw_line}")
    return values, errors


def validate_skill(skill_dir: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_dir}: SKILL.md ausente"], []

    if not NAME_PATTERN.fullmatch(skill_dir.name):
        errors.append(f"{skill_dir}: nome de diretório inválido")

    values, frontmatter_errors = parse_frontmatter(skill_file)
    errors.extend(f"{skill_file}: {error}" for error in frontmatter_errors)
    name = values.get("name", "")
    description = values.get("description", "")
    if not name:
        errors.append(f"{skill_file}: campo name ausente")
    elif not NAME_PATTERN.fullmatch(name):
        errors.append(f"{skill_file}: name inválido: {name}")
    elif name != skill_dir.name:
        errors.append(f"{skill_file}: name não coincide com o diretório")
    if not description:
        errors.append(f"{skill_file}: campo description ausente ou vazio")
    elif len(description) > 1024:
        errors.append(f"{skill_file}: description excede 1024 caracteres")

    line_count = len(skill_file.read_text(encoding="utf-8").splitlines())
    if line_count > 500:
        warnings.append(f"{skill_file}: {line_count} linhas; considere mover detalhes para referências")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("skills"), help="catálogo de skills")
    parser.add_argument("--strict", action="store_true", help="trata avisos como erros")
    args = parser.parse_args()

    if not args.root.is_dir():
        print(f"ERROR: catálogo não encontrado: {args.root}", file=sys.stderr)
        return 2

    skill_dirs = sorted(path for path in args.root.iterdir() if path.is_dir())
    if not skill_dirs:
        print(f"ERROR: nenhum diretório de skill em {args.root}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    for skill_dir in skill_dirs:
        skill_errors, skill_warnings = validate_skill(skill_dir)
        errors.extend(skill_errors)
        warnings.extend(skill_warnings)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors or (args.strict and warnings):
        return 1
    print(f"OK: {len(skill_dirs)} skill(s) validada(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())