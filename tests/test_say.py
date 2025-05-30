from fizzbuzz.say import is_fizz

def test_fizz_1_is_false():
    assert is_fizz(1) is False

def test_fizz_3_is_true():
    assert is_fizz(3) is True

def test_fizz_5_is_false():
    assert is_fizz(5) is False

def test_fizz_6_is_true():
    assert is_fizz(3) is True
