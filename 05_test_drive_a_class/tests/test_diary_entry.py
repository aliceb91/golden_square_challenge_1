from lib.diary_entry import DiaryEntry

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
    It returns the users estimated reading time of a given diary entry in minutes.
    """
    test_string = ("Hello " * 198)[:-1]
    diary_entry = DiaryEntry("Good afternoon", test_string)
    result = diary_entry.reading_time(200)
    assert result == "0:01"

def test_compelx_reading_time():
    """
    Given a title and contents string, along with a wpm value as an integer
    It returns the users estimated reading time, rounded to the nearest minute.
    """
    test_string = ("Evening " * 801)[:-1]
    diary_entry = DiaryEntry("Good Evening", test_string)
    result = diary_entry.reading_time(200)
    assert result == "0:04"

def test_reading_simple_chunk():
    """
    Given a string of contents, a wpm value as an integer, and a minute value as an integer
    It returns a chunk of the contents that the user could read at that speed.
    """
    test_string = ("Hello " * 398)[:-1]
    diary_entry = DiaryEntry("Good morning", test_string)
    result = diary_entry.reading_chunk(200, 1)
    result_string = "Good morning: " + ("Hello " * 198)[:-1]
    assert result == result_string

def test_reading_complex_chunk():
    """
    Given a string of contents, a wpm value as an integer, and a minute value as an integer
    It returns a chunk of the contents that the user could read based on less obvious paramaters.
    """
    test_string = ("Bye " * 571)[:-1]
    diary_entry = DiaryEntry("Good night", test_string)
    result = diary_entry.reading_chunk(153, 2)
    result_string = "Good night: " + ("Bye " * 304)[:-1]
    assert result == result_string

def test_continues_chunk_when_run_twice():
    """
    Given a repeat chunk method call
    It returns a chunk of the contents that begins where the previous chunk left off.
    """
    test_string = ("Bye " * 1573)[:-1]
    diary_entry = DiaryEntry("Good night", test_string)
    diary_entry.reading_chunk(137, 3)
    result = diary_entry.reading_chunk(137, 3)
    result_string = ("Bye " * 411)[:-1]
    assert result == result_string

def test_continues_chunk_when_at_end_of_String():
    """
    Given a repeat chunk method call
    It returns a chunk of the contents that begins where the previous chunk left off and ends at the end of the string.
    """
    test_string = ("Hello " * 538)[:-1]
    diary_entry = DiaryEntry("Good morning", test_string)
    diary_entry.reading_chunk(234, 1)
    diary_entry.reading_chunk(234, 1)
    result = diary_entry.reading_chunk(234, 1)
    result_string = ("Hello " * 72)[:-1]
    assert result == result_string

def test_continues_chunk_at_appropriate_place():
    """
    Given a repeat chunk method call
    It returns a section of contents that begins where the previous one left off.
    """
    test_string = ("0 1 2 3 4 5 6 7 8 9 " * 100)[:-1]
    diary_entry = DiaryEntry("Numbers", test_string)
    diary_entry.reading_chunk(501, 1)
    result = diary_entry.reading_chunk(500, 1)
    result_string = ("0 1 2 3 4 5 6 7 8 9 " * 50)[:-1]
    assert result == result_string