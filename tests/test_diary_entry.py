from lib.diary_entry import DiaryEntry
import datetime

def test_format_method():
    """
    Given a title and contents string
    It returns a formatted string in the form "Title: Contents"
    """
    diary_entry = DiaryEntry("Hello", "This is me saying hello")
    result = diary_entry.format()
    assert result == "Hello: This is me saying hello"

def test_more_formatting():
    """
    Given a title and contents string
    It returns a different formatted string in the form "Title: Contents"
    """
    diary_entry = DiaryEntry("Goodbye", "This is me saying goodbye")
    result = diary_entry.format()
    assert result == "Goodbye: This is me saying goodbye"

def test_number_of_words():
    """
    Given a title and contents string
    It returns the total number of words within a diary entry
    """
    diary_entry = DiaryEntry("Hello", "This is me saying hello")
    result = diary_entry.count_words()
    assert result == 6

def test_number_of_other_words():
    """
    Given a title and contents string
    It returns the total number of words within a different diary entry
    """
    diary_entry = DiaryEntry("Good afternoon", "What lovely weather we are having!")
    result = diary_entry.count_words()
    assert result == 8

def test_reading_time():
    """
    Given a title and contents string, along with a wpm value as an integer
    It returns the users estimated reading time of a given diary entry.
    """
    test_string = ("Hello " * 200)[:-1]
    diary_entry = DiaryEntry("Good afternoon", test_string)
    result = diary_entry.reading_time(200)
    assert result == str(datetime.timedelta(seconds = 60))