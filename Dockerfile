FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -U pip pytest pytest-cov ruff mypy bandit pylint flake8 vulture semgrep pyupgrade pip-audit pre-commit
CMD ["python", "main.py"]
