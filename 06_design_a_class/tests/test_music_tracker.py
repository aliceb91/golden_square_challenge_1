import pytest
from lib.music_tracker import MusicTracker

def test_add_single_track():
    """
    Given an track and artist name
    It returns that track as a single entry in a list
    """
    music_tracker = MusicTracker()
    result = music_tracker.add_track("Tommy the Cat", "Primus")
    assert result == [{"Name": "Tommy the Cat", "Artist": "Primus"}]

def test_add_multiple_tracks():
    """
    Give multiple track and artist names
    It returns a list of track / artist name tuples
    """
    music_tracker = MusicTracker()
    music_tracker.add_track("Tommy the Cat", "Primus")
    result = music_tracker.add_track("Rasputin", "Boney M")
    assert result == [{"Name": "Tommy the Cat", "Artist": "Primus"}, {"Name": "Rasputin", "Artist": "Boney M"}]

def test_for_string_input():
    """
    Given non string inputs for track and artist name
    It reutrns an error message
    """
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add_track(True, 5)
    error_message = str(e.value)
    assert error_message == "String input required for both track name and artist"

def test_for_non_string_track():
    """
    Given a non string track name
    It returns an appropriate error
    """
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add_track(True, "Streetlight Manifesto")
    error_message = str(e.value)
    assert error_message == "String input required for both track name and artist"

def test_for_non_strin_artist():
    """
    Given a non string artist name
    It returns an appropriate error
    """
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add_track("A better place, a better time", {})
    error_message = str(e.value)
    assert error_message == "String input required for both track name and artist"

def test_view_single_track_list():
    """
    Given a single track input
    It returns a list containing that single track
    """
    music_tracker = MusicTracker()
    music_tracker.add_track("Aliens Exist", "Blink-182")
    result = music_tracker.view_track_list()
    assert result == [{"Name": "Aliens Exist", "Artist": "Blink-182"}]

def test_view_multiple_track_list():
    """
    Given multiple track inputs
    It returns a list of all input tracks
    """
    music_tracker = MusicTracker()
    music_tracker.add_track("Tommy the Cat", "Primus")
    music_tracker.add_track("Rasputin", "Boney M")
    music_tracker.add_track("Holy Wars", "Megadeth")
    result = music_tracker.view_track_list()
    assert result == [
        {"Name": "Tommy the Cat", "Artist": "Primus"},
        {"Name": "Rasputin", "Artist": "Boney M"},
        {"Name": "Holy Wars", "Artist": "Megadeth"}
            ]
