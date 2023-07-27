import pytest

class MusicTracker():
    def __init__(self):
        self.track_list = []

    def add_track(self, name, artist):
        """
        Adds the specified track to a list of tracks.

        Parameters:
            name: The name of the track.
            artist: The artist who produced the track.

        Returns:
            The updated track list.

        Side effects:
            The track list stroed in the calss' state will be updated with the new track.
        """
        if not isinstance(name, str) or not isinstance(artist, str):
            raise Exception("String input required for both track name and artist")
        self.track_list.append({"Name": name, "Artist": artist})
        return self.track_list

    def view_track_list(self):
        """
        Allows the user to view a list of currently stored tracks.

        Parameters:
            This method takes no aditional pramaets.

        Returns:
            The current track list.

        Side effects:
            This method does not print anything or influence any other functions.
        """
        return self.track_list
