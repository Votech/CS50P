from twttr import shorten


def test_removes_vowels():
    assert shorten("twitter") == "twttr"


def test_removes_capitalized_vowels():
    assert shorten("TWITTER") == "TWTTR"


def test_omites_numbers():
    assert shorten("1234567890") == "1234567890"


def test_omites_punctuation():
    assert shorten(",.:") == ",.:"
