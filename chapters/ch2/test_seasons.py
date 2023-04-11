from chapters.ch2.seasons import season


def test_input_returns_corresponding_output():
    season_related_word = season('winter')
    assert season_related_word == 'snow'

    season_related_word_2 = season('spring')
    assert season_related_word_2 == 'flowers'

    season_related_word_3 = season('summer')
    assert season_related_word_3 == 'beach'

    season_related_word_4 = season('fall')
    assert season_related_word_4 == 'leaves'

    season_related_word_5 = season('autumn')
    assert season_related_word_5 == 'leaves'


def test_case_sensitivity_does_not_matter():
    season_related_word = season('Fall')
    assert season_related_word == 'leaves'

    season_related_word_2 = season('SUMMER')
    assert season_related_word_2 == 'beach'


def test_non_season_returns_correctly():
    season_related_word = season('Spring Onions')
    assert season_related_word == 'I don\'t know this season'

    season_related_word_2 = season('365')
    assert season_related_word_2 == 'I don\'t know this season'
