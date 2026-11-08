#!/usr/bin/env python3
"""Static integrity gate for the FDE source snapshot.

Checks internal consistency only; it does not validate third-party claims,
live repository permissions, licenses or source URL reachability.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHA = re.compile(r"^[0-9a-f]{40}$")


def validate():
    errors = []
    data = json.loads((ROOT / "registry/snapshot.json").read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        errors.append("unexpected schema_version")
    repos = data.get("repositories", [])
    sources = data.get("sources", [])
    if len(repos) != 7 or len(sources) != 12:
        errors.append(f"baseline count changed: repositories={len(repos)}, sources={len(sources)}")
    names = set()
    for repo in repos:
        name = repo.get("repository")
        if not isinstance(name, str) or name in names:
            errors.append(f"duplicate/missing repository: {name}")
        names.add(name)
        commit = repo.get("commit")
        if not isinstance(commit, str) or not SHA.fullmatch(commit):
            errors.append(f"invalid pinned commit for {name}")
        for asset in repo.get("files", []):
            if not asset.get("path") or asset.get("object_type") not in ("blob", "tree"):
                errors.append(f"invalid source object in {name}")
            sha = asset.get("object_sha")
            if not isinstance(sha, str) or not SHA.fullmatch(sha):
                errors.append(f"invalid object sha in {name}")
    ids = set()
    for source in sources:
        identifier = source.get("id")
        if not identifier or identifier in ids:
            errors.append(f"duplicate/missing source id: {identifier}")
        ids.add(identifier)
        if source.get("repository") not in names:
            errors.append(f"source {identifier} has unknown repository")
        commit = source.get("commit")
        if not isinstance(commit, str) or not SHA.fullmatch(commit):
            errors.append(f"source {identifier} lacks pinned commit")
    return errors


if __name__ == "__main__":
    problems = validate()
    for problem in problems:
        print("FAIL:", problem)
    if problems:
        sys.exit(1)
    print("PASS: snapshot shape, identifiers and pinned SHA references")
    print("NOT VERIFIED: source claims, copyright, live remote state, privacy or runtime behavior")
