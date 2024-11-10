from plates import is_valid


def test_is_valid():
    assert is_valid("morethansixletters") == False
    assert is_valid("66hello") == False
    assert is_valid("AB88") == True
    assert is_valid("A88ASD") == False
    assert is_valid("8A2ASD") == False
    assert is_valid("882ASD") == False
    assert is_valid(" 1") == False
    assert is_valid("22") == False
    assert is_valid("_!)@#(*A)") == False
    assert is_valid("AB01") == False
    assert is_valid("AAA22A") == False
    assert is_valid("AA.22") == False
