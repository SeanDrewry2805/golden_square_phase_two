'''
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
'''

from lib.SongTracker import *

def test_song_tracker_list():
    # will initialise a song tracker then make sure it is initialised with an empty list
    song_tracker = SongTracker()
    assert song_tracker.songs == []

def test_song_tracker_add_song():
    # will initialise a song tracker
    # will add a song to the tracker with add_song()
    # will check the list to make sure the song has been added
    song_tracker = SongTracker()
    song_tracker.add_song('Teenage Dream')
    assert song_tracker.songs == ['Teenage Dream']

def test_song_tracker_show_songs():
    # will initialise a song tracker
    # will add several songs to the list
    # call show_song() and expect a formatted string as the return
    song_tracker = SongTracker()
    song_tracker.songs = []
    song_tracker.add_song('Teenage Dream')
    song_tracker.add_song('Hey Jude')
    song_tracker.add_song('All I Want for Christmas')
    assert song_tracker.show_songs() == 'Teenage Dream, Hey Jude, All I Want for Christmas'
