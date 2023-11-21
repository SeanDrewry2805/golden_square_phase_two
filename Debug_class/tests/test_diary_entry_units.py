from lib.Diary import *
from lib.DiaryEntry import *

"""
When we add two tracks
We get the tracks back in the track list
"""
def test_initial_functionality():
    DiaryEntry1 = DiaryEntry("Title1", "This will be title 1 content.")
    DiaryEntry2 = DiaryEntry("Title two", "This is going to be the contents for title 2.")
    assert DiaryEntry1.title == "Title1"
    assert DiaryEntry1.contents == "This will be title 1 content."

def test_count_words():
    DiaryEntry1 = DiaryEntry("Title1", "This will be title 1 content.")
    assert DiaryEntry1.count_words() == 6

def test_reading_time():
    DiaryEntry1 = DiaryEntry("Title1", "This will be title 1")
    assert DiaryEntry1.reading_time(1) == 5
    assert DiaryEntry1.reading_time(2) == 3

def test_reading_chunk():
    DiaryEntry1 = DiaryEntry("Title1", "This will be title 1")
    assert DiaryEntry1.reading_chunk(1, 1) == "This"
    assert DiaryEntry1.reading_chunk(1, 2) == "This will"

