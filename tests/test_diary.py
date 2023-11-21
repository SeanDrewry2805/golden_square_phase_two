from lib.diary import *

'''
When I initialise a new dairy
diary contains an empty list of entries
'''
def test_initialise_diary():
    diary = Diary()
    assert diary.entries == []