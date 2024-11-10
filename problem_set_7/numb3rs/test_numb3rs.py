from numb3rs import validate


def test_validate_true():
    assert validate("123.123.123.123")
    assert validate("0.0.0.0")


def test_validate_false():
    assert validate("123.123.123") == False
    assert validate("AAA.AAA.AAA.AAA") == False
    assert validate("-123.123.123.123") == False
    assert validate("123.AAA.123.123") == False
    assert validate("123.123.AAA.123") == False
    assert validate("123.123.123.AAA") == False
    assert validate("300.123.123.123") == False
    assert validate("123.300.123.123") == False
    assert validate("123.123.300.123") == False
    assert validate("123.123.123.300") == False
