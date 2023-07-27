from lib.estimated_reading_time import estimated_reading_time

def test_retruns_1_minute_for_200_words():
    """
    Given a text of 200 words
    It returns a string denoting the time of 00:01:00.00
    """
    test_string = "Hello " * 200
    test_string = test_string[:-1]
    result = estimated_reading_time(test_string)
    assert result == "Estimated reading time: 00:01:00.00"

def test_returns_15sec():
    """
    Given a text of 50 words
    It returns a string denoting the time of 00:00:15.00
    """
    test_string = "Hello " * 50
    test_string = test_string[:-1]
    result = estimated_reading_time(test_string)
    assert result == "Estimated reading time: 00:00:15.00"

def test_decimal_values():
    """
    Given a text of 49 words
    It returns a string denoting the time of 00:00:14.70
    """
    test_string = "Hello " *  49
    test_string = test_string[:-1]
    result = estimated_reading_time(test_string)
    assert result == "Estimated reading time: 00:00:14.70"

def test_hour_digit():
    """
    Given a text of 2000 words
    It returns a string denoting the time of 01:00:00.00
    """
    test_string = "Hello " *  12000
    test_string = test_string[:-1]
    result = estimated_reading_time(test_string)
    assert result == "Estimated reading time: 01:00:00.00"

def test_multiple_hours():
    """
    Given a text of 2000 words
    It returns a string denoting the time of 10:00:00.00
    """
    test_string = "Hello " *  120000
    test_string = test_string[:-1]
    result = estimated_reading_time(test_string)
    assert result == "Estimated reading time: 10:00:00.00"