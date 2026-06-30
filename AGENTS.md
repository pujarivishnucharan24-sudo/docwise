# Agents

AI agents in this project help with document processing, automation, compliance,
and safe development workflows.

## Operating Principles

- Preserve existing application behavior unless a task explicitly asks for a
  behavior change.
- Prefer small, reviewable edits with tests and documented validation.
- Never commit secrets, private receipts, generated databases, virtual
  environments, or cache directories.
- Use repository tooling before hand-written cleanup: Ruff for formatting and
  lint fixes, pytest for behavior, and configured security scanners for risk.
- Keep OCR and document handling local unless a future specification explicitly
  approves a network service.

## Compliance Tasks

When improving repository compliance, update the relevant documentation,
configuration, CI jobs, tests, and spec files together so GitLab CI reflects the
same checks developers can run locally.
