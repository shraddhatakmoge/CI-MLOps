import pytest

def cube(n):
    return n**3


@pytest.mark.parametrize(
    "n, expected",
    [
        (1,1),
        (2,8),
        (3,27),
        (4,64),
        (5,125)
    ]
)
def test_cube(n, expected):
    assert cube(n) == expected