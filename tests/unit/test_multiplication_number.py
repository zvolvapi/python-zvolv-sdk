from ZvolvArithmetic.arithmetic_opertion import mul_number

def test_multiplication_positive_numbers():
    assert mul_number(2, 3) == 6

def test_multiplication_negative_numbers():
    assert mul_number(-2, -3) == 6

def test_multiplication_mixed_numbers():
    assert mul_number(2, -3) == -6