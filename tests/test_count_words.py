from lib.count_words import count_words

def test_returns_0_if_empty_string():
    result = count_words("")
    assert result == 0

def test_returns_1_for_single_word_string():
    result = count_words("Hello")
    assert result == 1
def test_returns_correctly_for_multi_word_string():
    result = count_words("Hello to all of you")
    assert result == 5

def test_returns_0_if_white_space_given():
    result = count_words(" ")
    assert result == 0

def test_returns_correctly_despite_punctuation():
    result = count_words("Where, if you know, is the toilet?")
    assert result == 7

def test_returns_0_if_characters_are_not_words():
    result = count_words(", ! ? # ^")
    assert result == 0

def test_returns_correctly_with_mixed_string():
    result = count_words("Hello ! darkness ? my @ old : friend ^")
    assert result == 5
