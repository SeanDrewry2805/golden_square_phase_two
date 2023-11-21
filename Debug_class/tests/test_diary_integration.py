from lib.Diary import *
from lib.DiaryEntry import *

"""
When we add two tracks
We get the tracks back in the track list
"""
diary = Diary()
DiaryEntry1 = DiaryEntry("Title1", "This will be title 1 content.")
DiaryEntry2 = DiaryEntry("Title two", "This is going to be the contents for title 2.")
diary.add(DiaryEntry1)
diary.add(DiaryEntry2)
assert diary.all() == [DiaryEntry1, DiaryEntry2]

# """
# When we add two tracks
# And we search for a word in the title
# We get the matching track back
# """
# library = MusicLibrary()
# track_1 = Track("Always The Hard Way", "Terror")
# track_2 = Track("Higher Place", "Malevolence")
# library.add(track_1)
# library.add(track_2)
# library.search_by_title("Way") # => [track_1]

# """
# When we add two tracks
# And we search for a small part of a word in the title
# We get the matching track back
# """
# library = MusicLibrary()
# track_1 = Track("Always The Hard Way", "Terror")
# track_2 = Track("Higher Place", "Malevolence")
# library.add(track_1)
# library.add(track_2)
# library.search_by_title("lace") # => [track_2]

# """
# When we add two tracks
# And we search for a word not in any track title
# We get an empty list back
# """
# library = MusicLibrary()
# track_1 = Track("Always The Hard Way", "Terror")
# track_2 = Track("Higher Place", "Malevolence")
# library.add(track_1)
# library.add(track_2)
# library.search_by_title("zzz") # => []

# """
# Given a track with a title and artist
# #format returns a string like TITLE by ARTIST
# """
# track = Track("Higher Place", "Malevolence")
# track.format() # => "Higher Place by Malevolence"