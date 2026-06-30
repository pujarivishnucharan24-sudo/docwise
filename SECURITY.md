# Security Policy

DocWise processes documents that may contain sensitive financial or personal
information. Treat uploaded files, OCR output, exported reports, and local
databases as confidential data.

## Supported Versions

Security fixes are applied to the default branch and the latest tagged release.

## Reporting a Vulnerability

Report vulnerabilities privately to the project maintainers through the GitLab
security issue workflow or a private maintainer contact. Include:

- Affected file, dependency, or workflow.
- Steps to reproduce.
- Impact and suggested mitigation, if known.

Do not publish exploit details, secrets, private receipts, or personal data in a
public issue.

## Security Practices

- Keep `.env` and other secret-bearing files out of Git.
- Run `gitleaks`, `bandit`, `semgrep`, and `pip-audit` before merging changes.
- Review dependency updates and CI changes carefully.
- Prefer local OCR and parsing for private documents.
- Remove generated reports, uploads, and SQLite databases before sharing a
  workspace.
