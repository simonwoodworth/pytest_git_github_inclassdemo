from mymath import *

def test_add():
    assert add(3,4, 5) == 12

def test_subtract():
    assert subtract(3, 4, 5) == -6

def test_multiply():
    assert multiply(3, 4, 5) == 60

def test_divide():
    assert divide(3, 4, 5) == 0.15

def test_power():
    assert power(3, 2) == 9
    assert power(2, 3) == 8
    assert power(4, 4) == 256

def test_mod():
    assert mod(7, 4) == 3