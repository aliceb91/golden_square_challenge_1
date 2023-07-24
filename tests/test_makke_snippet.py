from lib.make_snippet import make_snippet

def test_returns_string_less_than_five_words():
    result = make_snippet("Hello")
    assert result == "Hello"

def test_returns_string_equal_to_five_words():
    result = make_snippet("Hello to the whole world")
    assert result == "Hello to the whole world"

def test_returns_snippet_above_five_words():
    result = make_snippet("This string is long to demonstrate the function")
    assert result == "This string is long to..."

def test_returns_empty_string_when_given_empty_string():
    result = make_snippet("")
    assert result == ""

def test_returns_whitespace_when_given_whitespace():
    result = make_snippet(" ")
    assert result == " "
