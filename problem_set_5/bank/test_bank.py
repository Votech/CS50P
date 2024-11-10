from bank import value


def test_bank():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("bla bla") == 100
    assert value("     meow    ") == 100
    assert value("Hey, there") == 20
