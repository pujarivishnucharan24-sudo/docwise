# Feature Specification: DocWise Receipt Processing

## Status

Accepted

## Problem

Small teams need a local way to extract useful fields from receipts without
uploading private documents to an external service.

## Goals

- Extract OCR text from receipt images and PDFs.
- Parse merchant, date, total, GST, and item lines when present.
- Store parsed receipts locally.
- Export receipt data to CSV and JSON.

## Non-Goals

- Cloud OCR integration.
- Multi-user authorization.
- Production document retention workflows.

## Requirements

- Accept `.png`, `.jpg`, `.jpeg`, and PDF inputs through local helpers or the
  Streamlit dashboard.
- Keep uploaded documents and generated reports out of Git.
- Provide automated tests for parser behavior.
- Preserve local-only processing unless a future spec approves remote services.

## Security and Privacy

- Uploaded documents, OCR text, and reports are sensitive.
- No secrets or private documents should be committed.
- Security checks include Bandit, Semgrep, pip-audit, and Gitleaks.

## Acceptance Criteria

- Parser tests pass with coverage above the configured threshold.
- CI runs lint, type checking, tests, coverage, and security scanning.
- Documentation explains setup, use, contribution, and security expectations.

## Test Plan

- Unit-test parser extraction with representative OCR text.
- Run `pytest` with coverage.
- Run configured static and security checks locally and in GitLab CI.
