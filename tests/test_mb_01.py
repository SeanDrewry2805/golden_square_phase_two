from mocking_bites.exercise1 import *
from unittest.mock import Mock

#Testing MusicLibrary
def test_add_track():
    library = MusicLibrary()
    fake_track = Mock()
    fake_track.title = 'Teenage Dream'
    fake_track.artist = 'Katy Perry'
    library.add(fake_track)
    assert library.tracks[0].title == 'Teenage Dream'

def test_initial_empoty_track_list():
    library = MusicLibrary()
    assert library.tracks == []

def test_search_returns_track():
    library = MusicLibrary()
    fake_track_01 = Mock()
    fake_track_02 = Mock()
    fake_track_01.title = 'Fashion'
    fake_track_01.artist = 'Lady Gaga'
    fake_track_02.title = 'Back on 74'
    fake_track_02.artist = 'Jungle'
    fake_track_01.matches.return_value = False
    fake_track_02.matches.return_value = True
    library.add(fake_track_01)
    library.add(fake_track_02)
    assert library.search('back') == [fake_track_02]