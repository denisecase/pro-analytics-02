""".github/scripts/check_leakage.py: Check project for copy/paste leakage.

ALL-PY-REPOS
Updated: 2026-08-16

Detects the copy-paste failure modes seen across the fleet:
  1. Identity mismatch: a metadata file naming a DIFFERENT project than the
     repo it lives in (e.g. pup-check's name left in ml-vizkit's pyproject).
  2. src/ package drift: --cov target or wheel package pointing at a package
     directory that does not exist under src/ (silently breaks coverage/build).
  3. Foreign project names: another fleet project mentioned where it should not be.
  4. Version disagreement across pyproject.toml / CITATION.cff / CHANGELOG.md.

Dependency-free (stdlib + regex). Exit code is non-zero if anything is found.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

# ============================================================
# Patterns
# ============================================================

# WHY: These two pyproject.toml fields name the importable package under src/.
# A copied pyproject keeps the SOURCE repo's package name here, which is silent:
# a wrong wheel path ships broken/empty packages, and a wrong --cov target
# measures nothing (making the coverage gate meaningless). Both are checked
# against the actual src/<pkg> directory on disk, not against a naming rule.

# Captures <pkg> from:  packages = ["src/<pkg>"]  (hatch wheel target)
#   packages\s*=\s*\[   the "packages = [" opener, tolerant of spacing
#   \s*"src/           the opening quote and required src/ prefix
#   ([^"\]]+)          <pkg>: everything up to the closing quote or bracket
_WHEEL_PACKAGES_RE = re.compile(r'packages\s*=\s*\[\s*"src/([^"\]]+)"')

# Captures <pkg> from:  --cov=<pkg>  (inside addopts)
#   --cov=            the literal coverage-target flag
#   ([A-Za-z0-9_]+)   <pkg>: an import name (letters, digits, underscores)
_COV_TARGET_RE = re.compile(r'--cov=([A-Za-z0-9_]+)')

# Identity fields that should name THIS repo. If they name something else,
# it is almost always leftover copy-paste from a source template/repo.
_PROJECT_NAME_RE = re.compile(r'(?m)^\s*name\s*=\s*"([^"]+)"')
_VERSION_FILE_RE = re.compile(r'version-file\s*=\s*"src/([^/"]+)/')
_CITATION_TITLE_RE = re.compile(r'(?m)^\s*title:\s*"?([^"\n]+)"?')

# Version fields that must all agree.
_VERSION_PATTERNS: dict[str, re.Pattern[str]] = {
    "pyproject.toml (fallback-version)": re.compile(
        r'fallback-version\s*=\s*"([0-9]+\.[0-9]+\.[0-9]+)"'
    ),
    "pyproject.toml (version)": re.compile(
        r'(?m)^\s*version\s*=\s*"([0-9]+\.[0-9]+\.[0-9]+)"'
    ),
    "CITATION.cff (version)": re.compile(
        r'(?m)^\s*version:\s*"?([0-9]+\.[0-9]+\.[0-9]+)"?'
    ),
    "CHANGELOG.md (top release)": re.compile(r'##\s*\[([0-9]+\.[0-9]+\.[0-9]+)\]'),
}

# ============================================================
# Fleet namespace: EDIT THIS to list every project you own.
# A name here, appearing in a repo that ISN'T it, flags as a possible leak.
# ============================================================
KNOWN_PROJECTS = [
    "pup-core",
    "pup-up",
    "pup-check",
    "pup-clean",
    "pro-analytics-01",
    "pro-analytics-02",
    "pro-analytics",
    "datafun-toolkit",
    "datafun-streaming",
    "composable-data-core",
    "ml-vizkit",
    "se-manifest-schema",
    "se-codeowners",
    "applied-computing-foundations",
]


# ============================================================
# Helpers
# ============================================================
def norm(name: str) -> str:
    """Compare names ignoring - vs _ and case (penguins-body-mass == penguins_body_mass)."""
    return name.replace("-", "_").lower()


def repo_name(root: Path) -> str:
    """Return the repo name from the root path."""
    return root.resolve().name


def read(root: Path, rel: str) -> str | None:
    """Read a repo-relative text file, or None if absent/unreadable."""
    p = root / rel
    if not p.is_file():
        return None
    try:
        return p.read_text(encoding="utf-8")
    except OSError, UnicodeDecodeError:
        return None


# ============================================================
# Checks
# ============================================================
def check_identity(root: Path) -> list[str]:
    """Metadata identity fields should name THIS repo, not a source repo."""
    repo = norm(repo_name(root))
    problems: list[str] = []

    py = read(root, "pyproject.toml")
    if py is not None:
        for field, pat in (
            ("project.name", _PROJECT_NAME_RE),
            ("version-file", _VERSION_FILE_RE),
        ):
            for m in pat.finditer(py):
                if norm(m.group(1)) != repo:
                    problems.append(
                        f"pyproject.toml: {field} = {m.group(1)!r} does not match repo {repo_name(root)!r}"
                    )

    cff = read(root, "CITATION.cff")
    if cff is not None:
        for m in _CITATION_TITLE_RE.finditer(cff):
            if norm(m.group(1).strip()) != repo:
                problems.append(
                    f"CITATION.cff: title = {m.group(1).strip()!r} does not match repo {repo_name(root)!r}"
                )
    return problems


def check_src_package(root: Path) -> list[str]:
    """The cov target and wheel package must point at a real src/<pkg> dir."""
    text = read(root, "pyproject.toml")
    if text is None:
        return []
    problems: list[str] = []
    src = root / "src"
    actual = (
        {p.name for p in src.iterdir() if p.is_dir() and (p / "__init__.py").exists()}
        if src.is_dir()
        else set()
    )

    for field, pat in (
        ("wheel.packages", _WHEEL_PACKAGES_RE),
        ("cov-target", _COV_TARGET_RE),
    ):
        for m in pat.finditer(text):
            named = m.group(1)
            if actual and named not in actual:
                problems.append(
                    f"pyproject.toml: {field} points at {named!r}, "
                    f"but src/ contains {sorted(actual)}"
                )
    return problems


def check_foreign_projects(root: Path) -> list[str]:
    """A fleet project named in a repo that isn't it is a likely copy-paste leak."""
    repo = norm(repo_name(root))
    problems: list[str] = []
    for filename in ("pyproject.toml", "CITATION.cff", "CHANGELOG.md", "README.md"):
        text = read(root, filename)
        if text is None:
            continue
        for proj in KNOWN_PROJECTS:
            if norm(proj) == repo:
                continue  # naming yourself is fine
            if re.search(rf'(?<![\w-]){re.escape(proj)}(?![\w-])', text):
                problems.append(
                    f"{filename}: mentions other project {proj!r} (copy-paste leak?)"
                )
    return problems


def check_versions(root: Path) -> list[str]:
    """Pyproject / CITATION / CHANGELOG versions should all agree."""
    found: dict[str, str] = {}
    for label, pat in _VERSION_PATTERNS.items():
        fname = label.split(" ")[0]
        text = read(root, fname)
        if text is None:
            continue
        m = pat.search(text)
        if m:
            found[label] = m.group(1)
    if len(set(found.values())) > 1:
        detail = ", ".join(f"{k}={v}" for k, v in found.items())
        return [f"version mismatch across files: {detail}"]
    return []


def check_repo(root: Path) -> list[str]:
    """Run all checks on a repo root, returning a list of problems found."""
    return (
        check_identity(root)
        + check_src_package(root)
        + check_foreign_projects(root)
        + check_versions(root)
    )


# ============================================================
# Entry point
# ============================================================
def main() -> int:
    """Main entry point. Returns 0 if clean, 1 if problems found."""
    ap = argparse.ArgumentParser(description="Detect copy-paste metadata leakage.")
    ap.add_argument("paths", nargs="*", default=["."], help="repo root(s) to check")
    args = ap.parse_args()

    total = 0
    for path in args.paths:
        root = Path(path)
        problems = check_repo(root)
        if problems:
            total += len(problems)
            print(f"\n{repo_name(root)}:")
            for p in problems:
                print(f"  LEAK  {p}")
        else:
            print(f"\n{repo_name(root)}: clean")

    if total:
        print(f"\n{total} potential leak(s) found.")
        return 1
    print("\nNo leakage detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
