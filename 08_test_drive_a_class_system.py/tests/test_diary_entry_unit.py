from lib.diary_entry import DiaryEntry

def test_create_diary_entry():
    # Given an entry title and contents
    # It stores these values in the instance state.
    entry = DiaryEntry("Good morning!", "Hello.")
    assert [entry.title, entry.contents] == ["Good morning!", "Hello."]