from kata.is_true import is_true


def test_is_true() -> None:
    assert is_true() is True


def test_is_true_again() -> None:
    assert is_true() is not False
