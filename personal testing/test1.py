import pytest
from src.tested1 import add, sub, mul, div

def test_add():
    assert add(3,4) == 7
    assert add(5,4) == 9
    assert add(6,4) == 10
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(3,4) == -1
    assert sub(5,4) == 1
    assert sub(6,4) == 2
    assert sub(10, 5) == 5
    assert sub(0, 1) == -1

def test_mul():
    assert mul(3,4) == 12
    assert mul(5,4) == 20
    assert mul(3, 7) == 21
    assert mul(0, 5) == 0
    assert mul(6,4) == 24

def test_div():
    assert div(3,4) == 0.75
    assert div(5,0) == 1.25
    assert div(6,4) == 1.5
    assert div(10, 2) == 5
    assert div(0, 1) == 0

    with pytest.raises(ValueError, match='Cannot divide by zero'):
        div(5, 0)



