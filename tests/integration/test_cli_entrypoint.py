"""Runs the CLI as a real child process via ``python -m zeroai``.

The command is a fixed argv built from ``sys.executable``; no shell is involved.
"""

import subprocess
import sys

from zeroai.version import __version__


def test_python_dash_m_reports_version() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "zeroai", "--version"],
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == f"zeroai {__version__}"
