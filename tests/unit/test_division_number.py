from ZvolvArithmetic.arithmetic_opertion import div_numbers
import pytest

def test_division_positive_numbers():
    assert div_numbers(6, 2) == 3

def test_division_negative_numbers():
    assert div_numbers(-6, -2) == 3

def test_division_mixed_numbers():
    assert div_numbers(6, -2) == -3

def test_division_by_zero():
    with pytest.raises(ValueError):
        div_numbers(6, 0)