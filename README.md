# ZeroAI

ZeroAI is the local-first assistant runtime planned for **ZeroOS**, a Debian 13 (Trixie)
distribution with KDE Plasma. It is developed in this repository, independently of ZeroOS.

## Current status

**Pre-alpha: project bootstrap only (Phase 01).** There is no assistant functionality yet.

Implemented today:

- an importable `zeroai` Python package with a single version source (`src/zeroai/version.py`);
- a `zeroai` command that prints help or its version, and nothing else;
- tooling: Ruff (lint and format), mypy (strict), pytest with coverage, Bandit;
- a GitHub Actions workflow running those checks on Python 3.13.

Not implemented (planned for later phases, see
[`docs/architecture/overview.md`](docs/architecture/overview.md)): local API, Ollama chat,
tool registry, approval workflow, system monitoring, desktop UI and the `systemd --user` service.

## Target platform

| Item | Value |
|---|---|
| OS | Debian 13 Trixie, AMD64 (development on Ubuntu 24.04) |
| Desktop | KDE Plasma, Wayland targeted |
| Python | 3.13 baseline |
| Hardware reference | 16 GB RAM, Intel iGPU + NVIDIA RTX 4060 (8 GB VRAM) |

## Quick start

Requires [uv](https://docs.astral.sh/uv/). Full instructions and a non-uv alternative are in
[`docs/development/setup.md`](docs/development/setup.md).

```bash
uv python install 3.13
uv sync --all-groups --python 3.13
uv run zeroai --version
```

## Checks

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src tests
uv run pytest --cov=zeroai --cov-report=term-missing
```

## License

**The project license has not yet been selected.** Until a license is added, no permission is
granted to use, copy, modify or redistribute this code, even though the repository may be
publicly visible.
