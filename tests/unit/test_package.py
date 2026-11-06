import re

import zeroai
from zeroai.version import __version__


def test_package_exposes_version() -> None:
    assert zeroai.__version__ == __version__


def test_version_is_pep440_like() -> None:
    assert re.fullmatch(r"\d+\.\d+\.\d+(\.dev\d+|a\d+|b\d+|rc\d+)?", __version__)
