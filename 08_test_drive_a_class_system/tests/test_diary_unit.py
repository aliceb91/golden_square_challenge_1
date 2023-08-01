from lib.diary import Diary

def test_add_entry_to_diary():
    # Given a diary entry
    # It appends the entry to the entry list.
    diary = Diary()
    class SampleEntry():
        def __init__(self):
            self.title = "Good morning"
            self.contents = "Hello"
    sample_entry = SampleEntry()
    diary.add(sample_entry)
    result = diary.entries
    assert result == [sample_entry]

def test_pull_all_entries():
    # Given a selection of class instances
    # Returns a list containing all of these instances
    diary = Diary()
    class SampleEntry():
        def __init__(self):
            self.title = "Good morning"
            self.contents = "Hello"
    sample_entry_1 = SampleEntry()
    sample_entry_2 = SampleEntry()
    sample_entry_3 = SampleEntry()
    diary.add(sample_entry_1)
    diary.add(sample_entry_2)
    diary.add(sample_entry_3)
    result = diary.all()
    assert result == [sample_entry_1, sample_entry_2, sample_entry_3]
    