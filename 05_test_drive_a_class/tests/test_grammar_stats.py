from lib.grammar_stats import GrammarStats

def test_checks_correct_punctuation():
    """
    Given a string with correct punctuation
    It returns a string denoting that the punctuation is correct.
    """
    grammar_stats = GrammarStats()
    result = grammar_stats.check("This string is ok.")
    assert result == True

def test_checks_no_capital_letter():
    """
    Given the string with no capital letter at the start
    It returns a string denoting that there is no capital letter on the string.
    """
    grammar_stats = GrammarStats()
    result = grammar_stats.check("this string is not ok.")
    assert result == False

def test_checks_no_end_punctuation():
    """
    Given a string with no valid punctuation at the end
    It returns a string denoting that there is no valid punctuation at the end of the string.
    """
    grammar_stats = GrammarStats()
    result = grammar_stats.check("This string is not ok")
    assert result == False

def test_checks_no_capital_or_punctuation():
    """
    Given a string with no capital letter or valid punctuation
    It returns a string denoting that these elements are missing from the string.
    """
    grammar_stats = GrammarStats()
    result = grammar_stats.check("this string is really not correct")
    assert result == False

def test_checks_empty_string():
    """
    Given an empty string
    It returns a string denoting that both required elements are missing from the string.
    """
    grammar_stats = GrammarStats()
    result = grammar_stats.check("")
    assert result == False

def test_checks_whitespace():
    """
    Given a string of a single whitespace
    It returns a string denoting that both requierd elements are missing from the string.
    """
    grammar_stats = GrammarStats()
    result = grammar_stats.check(" ")
    assert result == False

def test_checks_only_punctuation():
    """
    Given a string of a single item of punctuation
    It returns a string denoting that there is no capital letter present at start of string.
    """
    grammar_stats = GrammarStats()
    result = grammar_stats.check(".")
    assert result == False

def test_checks_percentage_correct():
    """
    Given multiple strings of punctuation
    It returns the percentage of correct punctuation strings that have been entered.
    """
    grammar_stats = GrammarStats()
    for _ in range(0, 6):
        grammar_stats.check("Yes.")
    for _ in range(0, 4):
        grammar_stats.check("no")
    result = grammar_stats.percentage_good()
    assert result == 60

def test_checks_complex_percentage_correct():
    """
    Given multiple strongs of punctuation
    It returns the percentage of correct punctuation strings for a prime number of entries.
    """
    grammar_stats = GrammarStats()
    for _ in range(0, 8):
        grammar_stats.check("Yes.")
    for _ in range(0, 5):
        grammar_stats.check("no")
    result = grammar_stats.percentage_good()
    assert result == 62