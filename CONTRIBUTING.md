# Contributing

Thank you for improving DocWise. Contributions should keep document processing
safe, testable, and easy to review.

## Development Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
pre-commit install
cp .env.example .env
```

Install Tesseract OCR locally before testing OCR-specific workflows.

## Branching

- Create a focused branch for each change.
- Keep application behavior changes separate from formatting or compliance
  maintenance.
- Use conventional commit messages where possible, for example
  `feat: add receipt export` or `fix: handle empty OCR text`.

## Required Checks

Run these checks before opening a merge request:

```bash
ruff format --check .
ruff check .
mypy .
flake8 .
pylint app.py database.py export.py image_processing.py main.py ocr.py parser.py tests test_pipeline.py
vulture . --min-confidence 80
bandit -c pyproject.toml -r .
pip-audit -r requirements.txt
semgrep scan --config .semgrep.yml --error
gitleaks detect --source . --config .gitleaks.toml --no-banner --redact
pytest
```

## Merge Request Expectations

- Include a clear summary and testing notes.
- Update `README.md`, `USER_MANUAL.md`, or specs when behavior changes.
- Add or update tests for parser, export, persistence, or OCR helper changes.
- Never commit secrets, local databases, private documents, or generated caches.
