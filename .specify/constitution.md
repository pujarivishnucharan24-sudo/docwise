# DocWise Constitution

## Principles

1. Specifications before implementation: meaningful feature work starts with a
   short spec that defines the problem, users, requirements, acceptance
   criteria, risks, and tests.
2. Privacy by default: documents, receipts, OCR text, reports, and databases are
   treated as sensitive local data.
3. Automated quality gates: formatting, linting, type checks, tests, coverage,
   dependency audits, static security analysis, and secret scanning run in CI.
4. Reviewable changes: edits should be small enough to understand and should
   preserve existing behavior unless the spec calls for a change.
5. Reproducible operations: local commands and GitLab CI should exercise the
   same quality and security controls.

## Governance

- Specs live in `specs/`.
- Templates live in `.specify/templates/`.
- CI must fail when required quality, test, or security gates fail.
- Exceptions require documentation in the relevant spec or merge request.
