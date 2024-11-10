from seasons import Season


def test_seasons():
    season = Season("1994-01-01")
    assert (
        season.seasons_of_love()
        == "Sixteen million, two hundred twenty-five thousand, nine hundred twenty minutes"
    )
