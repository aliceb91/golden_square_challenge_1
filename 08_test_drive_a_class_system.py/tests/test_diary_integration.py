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
