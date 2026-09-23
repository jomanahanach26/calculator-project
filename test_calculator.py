from calculator import calculate


def test_addition():
    result = calculate(10, 5, "+")
    assert result == 15