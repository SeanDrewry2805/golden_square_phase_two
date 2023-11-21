from lib.Diary import *
from lib.DiaryEntry import *

"""
When we add two tracks
We get the tracks back in the track list
"""
def test_diary_returns_empty_list():   
    diary = Diary()
    assert diary.all() == []

def test_diary_returns_list():
    diary = Diary()
    DiaryEntry1 = DiaryEntry("Title1", "This will be title 1 content.")
    #DiaryEntry2 = DiaryEntry("Title two", "This is going to be the contents for title 2.")
    diary.add(DiaryEntry1)
    assert diary.all() == [DiaryEntry1]

def test_count_words_diary():
    diary = Diary()
    DiaryEntry1 = DiaryEntry("Title1", "This will be title 1 content.")
    DiaryEntry2 = DiaryEntry("Title two", "This is going to be the contents for title 2.")
    diary.add(DiaryEntry1)
    diary.add(DiaryEntry2)
    assert diary.count_words() == 16

def test_reading_time_diary():
    diary = Diary()
    DiaryEntry1 = DiaryEntry("Title1", "This will be title 1 content.")
    DiaryEntry2 = DiaryEntry("Title two", "This is going to be the contents for title 2.")
    diary.add(DiaryEntry1)
    diary.add(DiaryEntry2)
    assert diary.reading_time(1) == 16
    assert diary.reading_time(2) == 8

def test_best_entry_for_reading_time():
    diary = Diary()
    DiaryEntry1 = DiaryEntry("Title1", "This will be title 1 content.")
    DiaryEntry2 = DiaryEntry("Title two", "This is going to be the contents for title 2.")
    DiaryEntry3 = DiaryEntry("Title three", "This is going to be the contents for title 3 and This is going to be the contents for title 3")
    diary.add(DiaryEntry1)
    diary.add(DiaryEntry2)
    diary.add(DiaryEntry3)
    assert diary.find_best_entry_for_reading_time(1, 6) == DiaryEntry1
    assert diary.find_best_entry_for_reading_time(1, 10) == DiaryEntry2
    assert diary.find_best_entry_for_reading_time(1, 21) == DiaryEntry3