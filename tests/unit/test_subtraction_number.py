from ZvolvArithmetic.arithmetic_opertion import sub_number

def test_subtraction_positive_numbers():
    assert sub_number(5, 2) == 3

def test_subtraction_negative_numbers():
    assert sub_number(-5, -2) == -3

def test_subtraction_mixed_numbers():
    assert sub_number(3, -2) == 5
