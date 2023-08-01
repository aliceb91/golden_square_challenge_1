from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_return_list_of_multiple_entries():
    # Given a number of diary entries
    # It returns these entries in a list.
    entry_1 = DiaryEntry("Good morning!", "Hello.")
    entry_2 = DiaryEntry("Good afternoon!", "How are you?")
    entry_3 = DiaryEntry("Good evening!", "Goodbye.")
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    result = diary.all()
    assert result == [entry_1, entry_2, entry_3]

def test_return_word_count_of_specific_entry():
    # Given a specific diary entry
    # It returns the word count of this entry
    entry_1 = DiaryEntry("Good morning!", "Hello.")
    entry_2 = DiaryEntry("Good afternoon!", "How are you?")
    entry_3 = DiaryEntry("Good evening!", "Goodbye.")
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    target_diary = diary.entries[1]
    result = target_diary.count_words()
    assert result == 3

def test_return_word_count_of_all_entries():
    # Given a list of diary entries
    # It returns the total word count of all diary entries.
    entry_1 = DiaryEntry("Good morning!", "Hello.")
    entry_2 = DiaryEntry("Good afternoon!", "How are you?")
    entry_3 = DiaryEntry("Good evening!", "Goodbye.")
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    result = diary.count_words()
    assert result == 5

def test_reading_time_of_all_entries():
    # Given a list of diary entries
    # It returns the total reading time of all entries given a specific wpm.
    entry_1 = DiaryEntry("Good morning!", (("Hello " * 200)[:-1]))
    entry_2 = DiaryEntry("Good afternoon!", (("Hello " * 400)[:-1]))
    entry_3 = DiaryEntry("Good evening!", (("Hello " * 600)[:-1]))
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    result = diary.reading_time(200)
    assert result == 6

def test_find_best_entry():
    entry_1 = DiaryEntry("Good morning!", (("Hello " * 200)[:-1]))
    entry_2 = DiaryEntry("Good afternoon!", (("Hello " * 400)[:-1]))
    entry_3 = DiaryEntry("Good evening!", (("Hello " * 600)[:-1]))
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    result = diary.find_best_entry_for_reading_time(200, 2)
    assert result == entry_2

def test_find_chunk_of_entry():
    # Given a specified diary entry
    # It returns a chunk of the entry that can be read in the specified time at a specified speed.
    entry_1 = DiaryEntry("Good morning!", (("Hello " * 200)[:-1]))
    entry_2 = DiaryEntry("Good afternoon!", (("Hello " * 400)[:-1]))
    entry_3 = DiaryEntry("Good evening!", (("Hello " * 600)[:-1]))
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    target = diary.entries[1]
    target.reading_chunk(200, 1)
    result = target.reading_chunk(150, 1)
    assert result == ("Hello " * 150)[:-1]