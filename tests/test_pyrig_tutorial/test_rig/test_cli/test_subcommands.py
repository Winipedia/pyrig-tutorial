"""Test module."""

from pyrig_tutorial.rig.cli.subcommands import hello, hello2


def test_hello() -> None:
    """Test function."""
    assert hello() is None


def test_hello2() -> None:
    """Test function."""
    assert hello2() is None
