# Development setup

## Prerequisites

- Linux AMD64 (Ubuntu 24.04 for development, Debian 13 as the target).
- Git.
- [uv](https://docs.astral.sh/uv/) (recommended), installed for your user, without sudo.
- Python 3.13. uv can provide it without touching the system Python:

  ```bash
  uv python install 3.13
  ```

Never use `sudo pip` and never install project dependencies into the system Python.

## Create the environment and install dependencies

```bash
uv sync --all-groups --python 3.13
```

This creates `.venv/` in the repository, installs the runtime and development dependencies
exactly as pinned in `uv.lock`, and installs `zeroai` in editable mode.

Check the result:

```bash
uv run zeroai --version
```

## Quality checks

```bash
uv run ruff check .              # lint
uv run ruff format --check .     # formatting (use `uv run ruff format .` to apply)
uv run mypy src tests            # strict type checking
uv run pytest --cov=zeroai --cov-report=term-missing
uv run bandit -c pyproject.toml -r src   # optional security hygiene scan
```

CI (`.github/workflows/ci.yml`) runs lint, format check, mypy and pytest on Python 3.13 with
`uv sync --locked`.

## Changing dependencies

Edit `pyproject.toml`, then run `uv lock` and commit the updated `uv.lock`. CI fails when
the lockfile is out of date.

## Without uv

You can use a project-local virtual environment instead. This installs the latest versions
allowed by `pyproject.toml` rather than the `uv.lock` pins.

```bash
python3.13 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e . bandit mypy pytest pytest-cov ruff
pytest --cov=zeroai --cov-report=term-missing
```

## Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `ModuleNotFoundError: No module named 'zeroai'` | The environment is not installed. Run `uv sync --all-groups`, or use `uv run …`. |
| `python3.13: command not found` | Run `uv python install 3.13`, or install Python 3.13 from your distribution. |
| `uv sync --locked` fails in CI | `uv.lock` is stale. Run `uv lock` and commit it. |
| mypy reports missing stubs for a new dependency | Add a typed alternative or a stub package. Do not disable strict mode globally. |
