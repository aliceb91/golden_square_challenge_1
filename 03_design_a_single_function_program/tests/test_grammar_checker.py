from lib.grammar_checker import grammar_checker

def test_checks_correct_punctuation():
    """
    Given a string with correct punctuation
    It returns a string denoting that the punctuation is correct.
    """
    result = grammar_checker("This string is ok.")
    assert result == "No errors detected, good job!"

def test_checks_no_capital_letter():
    """
    Given the string with no capital letter at the start
    It returns a string denoting that there is no capital letter on the string.
    """
    result = grammar_checker("this string is not ok.")
    assert result == "Error: No capital letter."

def test_checks_no_end_punctuation():
    """
    Given a string with no valid punctuation at the end
    It returns a string denoting that there is no valid punctuation at the end of the string.
    """
    result = grammar_checker("This string is not ok")
    assert result == "Error: No valid punctuation at end of string."

def test_checks_no_capital_or_punctuation():
    """
    Given a string with no capital letter or valid punctuation
    It returns a string denoting that these elements are missing from the string.
    """
    result = grammar_checker("this string is really not correct")
    assert result == "Error: No starting capital letter or valid punctuation at end of string."

def test_checks_empty_string():
    """
    Given an empty string
    It returns a string denoting that both required elements are missing from the string.
    """
    result = grammar_checker("")
    assert result == "Error: No starting capital letter or valid punctuation at end of string."

def test_checks_whitespace():
    """
    Given a string of a single whitespace
    It returns a string denoting that both requierd elements are missing from the string.
    """
    result = grammar_checker(" ")
    assert result == "Error: No starting capital letter or valid punctuation at end of string."

def test_checks_only_punctuation():
    """
    Given a string of a single item of punctuation
    It returns a string denoting that there is no capital letter present at start of string.
    """
    result = grammar_checker(".")
    assert result == "Error: No capital letter."