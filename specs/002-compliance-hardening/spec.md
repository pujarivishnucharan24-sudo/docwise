# Feature Specification: Compliance Hardening

## Status

Accepted

## Problem

The repository needs a complete compliance baseline so GitLab can validate
documentation, licensing, test coverage, Python quality, security scanning, and
spec-driven development artifacts.

## Goals

- Provide required project documentation and AGPLv3 licensing metadata.
- Configure Python quality tools with enforceable CI behavior.
- Add security scanning for source, dependencies, and secrets.
- Add a reusable specification structure for future features.

## Non-Goals

- Changing OCR, parsing, export, or dashboard behavior.
- Adding production deployment infrastructure.

## Requirements

- CI must fail on lint, type, test, coverage, or security failures.
- Tool configuration must exclude virtual environments, uploads, generated
  reports, caches, and backup files.
- At least one automated test must pass.
- Coverage must enforce a configured fail-under threshold.
- Changelog generation must be configured with Git-Cliff.

## Security and Privacy

- `.env.example` may contain placeholders only.
- `.env`, local databases, reports, uploads, and caches are ignored by Git.
- Secret scanning is required before merge.

## Acceptance Criteria

- `pytest` passes.
- Static quality and security tools are configured in repository files.
- GitLab CI contains quality, test, and security stages.
- Documentation names local validation commands.

## Test Plan

- Run formatting, linting, type checking, tests, coverage, Bandit, Semgrep,
  pip-audit, and Gitleaks locally.
- Confirm `.gitlab-ci.yml` uses the same checks without `|| true`.
