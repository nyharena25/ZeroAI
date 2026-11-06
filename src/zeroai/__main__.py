"""Command-line entry point.

Only prints help or version information; it performs no I/O beyond stdout/stderr.
"""

import argparse
from collections.abc import Sequence

from zeroai.version import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="zeroai",
        description="ZeroAI: local-first assistant runtime for ZeroOS (bootstrap skeleton).",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    parser.parse_args(argv)
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
