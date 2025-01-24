from src.main import func
import pytest

def test_func():
    assert func(3) == 6

@pytest.mark.parametrize(
    "a, b",
    [
        (2, 4),
        (5, 10),
        (3, 6),
    ]
)
def test_fun_param(a, b):
    assert func(a) == b

