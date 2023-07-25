from lib.estimated_reading_time import estimated_reading_time

"""
Given a text of 200 words
It returns a string denoting the time of 00:01:00.00
"""
def test_retruns_1_minute_for_200_words():
    test_string = "Hello " * 200
    test_string = test_string[:-1]
    result = estimated_reading_time(test_string)
    assert result == "Estimated reading time: 00:01:00.00"

def test_returns_15sec():
    test_string = "Hello " * 50
    test_string = test_string[:-1]
    result = estimated_reading_time(test_string)
    assert result == "Estimated reading time: 00:00:15.00"
