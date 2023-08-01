from lib.diary_entry import DiaryEntry

def test_create_diary_entry():
    # Given an entry title and contents
    # It stores these values in the instance state.
    entry = DiaryEntry("Good morning!", "Hello.")
    assert [entry.title, entry.contents] == ["Good morning!", "Hello."]

def test_count_words():
    # Given a diary entry
    # It returns the number of words in it's contents.
    entry = DiaryEntry("Test", "This entry is a test")
    result = entry.count_words()
    assert result == 5

def test_reading_time():
    # Given a diary entry
    # It returns the time taken to read the entry at a given wpm.
    test_contents = ("Hello " * 400)[:-1]
    entry = DiaryEntry("Good morning", test_contents)
    result = entry.reading_time(200)
    assert result == 2

def test_reading_chunk():
    # Given a diary entry
    # It returns a chunk that can be read in teh specified time.
    test_contents = ("Hello " * 400)[:-1]
    entry = DiaryEntry("Good morning", test_contents)
    result = entry.reading_chunk(200, 1)
    assert result == ("Hello " * 200)[:-1]

def test_repeated_chunks():
    # Given multiple chunk requests
    # It returns the next available chunk in the entry.
    test_contents = (("Hello " * 200) + ("Bye " * 150) + ("Hello " * 50))[:-1]
    entry = DiaryEntry("Greetings", test_contents)
    entry.reading_chunk(200, 1)
    result = entry.reading_chunk(150, 1)
    assert result == ("Bye " * 150)[:-1]

def test_chunk_request_beyond_range():
    # Given a chunk request beyond the range of the chunk
    # It returns the remaining available words in the entry.
    test_contents = (("Hello " * 200) + ("Bye " * 150) + ("Hello " * 50))[:-1]
    entry = DiaryEntry("Greetings", test_contents)
    entry.reading_chunk(200, 1)
    entry.reading_chunk(150, 1)
    result = entry.reading_chunk(200, 1)
    assert result == ("Hello " * 50)[:-1]