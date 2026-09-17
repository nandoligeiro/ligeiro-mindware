#!/usr/bin/env python3
"""Validate minimum regression coverage for L3 Agent Skills.

The validator intentionally uses only the Python standard library. It validates the
small, stable subset of the eval YAML contract that is required by the repository:
skill binding, scenario ids, categories, prompts and expected activation.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REQUIRED_CATEGORIES = {"should-trigger", "should-not-trigger", "incomplete", "edge"}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass
class Scenario:
    scenario_id: str = ""
    category: str = ""
    prompt: str = ""
    expected_activation: str = ""


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"\"", "'"}:
        return value[1:-1]
    return value


def parse_eval(path: Path) -> tuple[str, list[Scenario], list[str]]:
    skill = ""
    scenarios: list[Scenario] = []
    errors: list[str] = []
    current: Scenario | None = None

    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if raw.startswith("skill:"):
            skill = scalar(raw.split(":", 1)[1])
            continue

        match = re.match(r"^\s*-\s+id:\s*(.+)$", raw)
        if match:
            if current is not None:
                scenarios.append(current)
            current = Scenario(scenario_id=scalar(match.group(1)))
            continue

        if current is None:
            continue

        field = re.match(r"^\s+(category|prompt|expected_activation):\s*(.*)$", raw)
        if not field:
            continue
        key, value = field.group(1), scalar(field.group(2))
        if key == "category":
            current.category = value
        elif key == "prompt":
            current.prompt = value
        elif key == "expected_activation":
            current.expected_activation = value.lower()

    if current is not None:
        scenarios.append(current)

    if not skill:
        errors.append(f"{path}: campo skill ausente")
    return skill, scenarios, errors


def load_l3_skills(path: Path) -> tuple[list[str], list[str]]:
    if not path.is_file():
        return [], [f"manifest L3 não encontrado: {path}"]

    skills: list[str] = []
    errors: list[str] = []
    seen: set[str] = set()
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        name = raw.strip()
        if not name or name.startswith("#"):
            continue
        if not NAME_PATTERN.fullmatch(name):
            errors.append(f"{path}:{lineno}: nome inválido: {name}")
            continue
        if name in seen:
            errors.append(f"{path}:{lineno}: skill duplicada: {name}")
            continue
        seen.add(name)
        skills.append(name)
    if not skills:
        errors.append(f"{path}: nenhuma skill L3 registrada")
    return skills, errors


def validate_skill(skill: str, skills_root: Path, evals_root: Path) -> list[str]:
    errors: list[str] = []
    skill_dir = skills_root / skill
    if not (skill_dir / "SKILL.md").is_file():
        errors.append(f"{skill}: SKILL.md não encontrado")

    eval_path = evals_root / f"{skill}.yaml"
    if not eval_path.is_file():
        return errors + [f"{skill}: eval ausente: {eval_path}"]

    bound_skill, scenarios, parse_errors = parse_eval(eval_path)
    errors.extend(parse_errors)
    if bound_skill and bound_skill != skill:
        errors.append(f"{eval_path}: skill '{bound_skill}' não coincide com '{skill}'")

    if not scenarios:
        return errors + [f"{eval_path}: nenhum cenário encontrado"]

    ids: set[str] = set()
    categories: set[str] = set()
    for index, scenario in enumerate(scenarios, start=1):
        prefix = f"{eval_path}: cenário {index}"
        if not scenario.scenario_id:
            errors.append(f"{prefix}: id ausente")
        elif scenario.scenario_id in ids:
            errors.append(f"{prefix}: id duplicado: {scenario.scenario_id}")
        else:
            ids.add(scenario.scenario_id)

        if not scenario.category:
            errors.append(f"{prefix}: category ausente")
        else:
            categories.add(scenario.category)

        if not scenario.prompt:
            errors.append(f"{prefix}: prompt ausente ou vazio")

        if scenario.expected_activation not in {"true", "false"}:
            errors.append(f"{prefix}: expected_activation deve ser true ou false")
        elif scenario.category == "should-trigger" and scenario.expected_activation != "true":
            errors.append(f"{prefix}: should-trigger precisa expected_activation=true")
        elif scenario.category == "should-not-trigger" and scenario.expected_activation != "false":
            errors.append(f"{prefix}: should-not-trigger precisa expected_activation=false")
        elif scenario.category in {"incomplete", "edge"} and scenario.expected_activation != "true":
            errors.append(f"{prefix}: {scenario.category} precisa expected_activation=true")

    missing = REQUIRED_CATEGORIES - categories
    if missing:
        errors.append(f"{eval_path}: categorias L3 ausentes: {', '.join(sorted(missing))}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-root", type=Path, default=Path("skills"))
    parser.add_argument("--evals-root", type=Path, default=Path("evals"))
    parser.add_argument("--manifest", type=Path, default=Path("evals/l3-skills.txt"))
    parser.add_argument("--strict", action="store_true", help="reservado para checks adicionais sem quebrar a interface")
    args = parser.parse_args()

    skills, errors = load_l3_skills(args.manifest)
    for skill in skills:
        errors.extend(validate_skill(skill, args.skills_root, args.evals_root))

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1

    print(f"OK: {len(skills)} skill(s) L3 com cobertura mínima de evals")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
