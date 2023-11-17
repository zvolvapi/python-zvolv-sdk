from ZvolvArithmetic.arithmetic_opertion import add_numbers
def test_addition_positive_numbers():
    assert add_numbers(1, 2) == 3

def test_addition_negative_numbers():
    assert add_numbers(-1, -2) == -3

def test_addition_mixed_numbers():
    assert add_numbers(3, -2) == 1