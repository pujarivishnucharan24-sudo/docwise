# DocWise

DocWise is a Python document-processing project for local receipt OCR, text
parsing, lightweight persistence, and export automation. The repository is
configured for GitLab CI, Python quality gates, security scanning, coverage
reporting, and spec-driven development.

## Features

- OCR helpers for image and PDF receipts.
- Receipt parsing for merchant, date, totals, GST, and line items.
- SQLite persistence helpers for parsed receipts.
- CSV and JSON export utilities.
- Streamlit dashboard for interactive receipt uploads.
- Compliance automation with Ruff, Mypy, Flake8, Pylint, Bandit, Vulture,
  Semgrep, pip-audit, Gitleaks, pytest, coverage, pre-commit, and Git-Cliff.

## Requirements

- Python 3.12 or newer.
- Tesseract OCR installed locally for OCR workflows.
- Git for pre-commit, changelog, and CI workflows.

On Debian or Ubuntu:

```bash
sudo apt-get update
sudo apt-get install -y tesseract-ocr
```

On macOS with Homebrew:

```bash
brew install tesseract
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
```

## Usage

Run the CLI smoke entry point:

```bash
python main.py
```

Run the Streamlit dashboard:

```bash
streamlit run app.py
```

Run the parser tests and coverage gate:

```bash
pytest
```

## Quality Gates

The repository is ready for GitLab CI and local validation with:

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

## Docker

Build and run the project image:

```bash
docker build -t docwise .
docker run --rm -p 8501:8501 docwise
```

The container starts the Streamlit dashboard on `0.0.0.0` and uses the `PORT`
environment variable when one is supplied by a platform such as Render.

## Spec-Driven Development

Project specifications live in `specs/`, and reusable templates live in
`.specify/templates/`. New features should start with a short specification
that captures the problem, requirements, acceptance criteria, security
considerations, and test plan before implementation begins.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for branch, test, lint, and merge
request expectations.

## Security

See [SECURITY.md](SECURITY.md) for vulnerability reporting and supported
security practices. Do not commit secrets, production data, or private
documents.

## License

DocWise is licensed under the GNU Affero General Public License v3.0 or later.
See [LICENSE](LICENSE).
