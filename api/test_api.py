from .api import get_info


def test_integer_succeeds():
    result = get_info(5)
    assert result  # not an empty string


def test_float_fails():
    result = get_info(2.5)
    assert result == ""




