import pytest

from zeroai.__main__ import main
from zeroai.version import __version__


def test_version_flag_prints_version_and_exits_zero(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main(["--version"])

    assert exc_info.value.code == 0
    assert capsys.readouterr().out.strip() == f"zeroai {__version__}"


def test_no_arguments_prints_help(capsys: pytest.CaptureFixture[str]) -> None:
    assert main([]) == 0
    assert "usage: zeroai" in capsys.readouterr().out


def test_unknown_argument_is_rejected(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main(["--unknown"])

    assert exc_info.value.code == 2
    assert "unrecognized arguments" in capsys.readouterr().err
