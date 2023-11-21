class SongTracker():

    songs = []

    def __init__(self):
        pass

    def add_song(self, title):
        # will take an argument for the song title and add it to a list of songs
        self.songs.append(title)

    def show_songs(self):
        # will return a formatted string with a list of songs the user has added
        text = ', '.join(self.songs)
        return text