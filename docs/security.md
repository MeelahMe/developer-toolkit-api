# Security and hardening

CI runs four independent security tools on every push and pull request, in addition to the test suite. All GitHub Actions are pinned to specific commit SHAs, rather than mutable tags, to prevent supply-chain tampering. The same checks run locally through pre-commit hooks before code is pushed.

## Trivy: container vulnerability scanning

Trivy scans the built Docker image for known CVEs in OS packages and Python dependencies. The build fails on any fixable CRITICAL or HIGH severity finding.

An initial scan against `python:3.9-slim` surfaced 78 vulnerabilities (6 CRITICAL, 72 HIGH).

| Issue | Root cause | Fix |
|---|---|---|
| Stale OS packages | Base image packages were outdated relative to available Debian patches | Added `apt-get update && apt-get upgrade -y` at build time |
| Outdated Python version | `python:3.9-slim` blocked upgrading to a patched FastAPI/Starlette | Upgraded base image to `python:3.12-slim` |
| Vulnerable Starlette (CVE-2026-48818, CVE-2026-54283) | Outdated FastAPI pinned an unpatched Starlette transitively | Upgraded FastAPI to 0.141.1 |
| CI/Dockerfile Python version mismatch | CI specified Python 3.9 after the Dockerfile moved to 3.12 | Synchronized both to Python 3.12 |

These changes resolved 61 of 78 findings. The remaining 17 have no upstream Debian fix available and affect OS utilities (`perl`, `gzip`, `ncurses`) not invoked by the application. These are documented as accepted risk in [`.trivyignore`](../.trivyignore) rather than suppressed.

A separate issue was identified later: `requirements.txt` included development tools (`semgrep`, `pytest`, `httpx`), which were consequently installed into the production container image. Dependencies are now split between `requirements.txt` (runtime only) and `requirements-dev.txt` (test, lint, and security tooling).

## gitleaks: secret detection

gitleaks scans full commit history for accidentally committed credentials. It runs independently of the build process.

This control was verified by committing a fake credential on a throwaway branch. The initial test did not trigger detection, because the workflow change adding the gitleaks job had not yet been committed to that branch. After correcting this, gitleaks correctly flagged the fake credential. The test branch was later merged into `master` unintentionally; the fake credential was removed using `git revert -m 1`, preserving a transparent commit history.

## Semgrep: static analysis

Semgrep scans source code, workflow YAML, and the Dockerfile for risky patterns not covered by Trivy or gitleaks.

An initial scan returned 8 findings, all tracing to a single root cause: every GitHub Action reference used a mutable tag (for example, `@v3` or `@master`) rather than a pinned commit SHA. This is a known supply-chain risk; Semgrep's rule documentation cites two real prior incidents involving this exact pattern. Each action was pinned to its verified commit SHA using `git ls-remote --tags`.

## Bandit: Python security linting

Bandit was added after Semgrep's rulesets, including the broader `p/security-audit` set, failed to detect a real vulnerability: the password generator used `random.choices()` rather than `secrets.choice()` (CWE-330, use of insufficiently random values). Bandit identified this immediately (rule `B311`). The fix was verified across pytest, Bandit, and both Semgrep configurations.

## Pre-commit hooks

The same four tools (gitleaks, ruff, ruff-format, Bandit) run locally before a commit completes. This is a faster feedback layer, not a replacement for CI enforcement; hooks can be bypassed and only run on machines where they are installed.
