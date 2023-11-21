from lib.ChallengeDiary import *
from lib.ChallengeEntry import *

#Diary entry class (diary class)
#Implement todo list in diary class
#Functionality:
#A list of diary entries
#be able to add to the list and access the list
#seperate list with Todo items - be able to add to list and access it
#find phone numbers in diary entries and return a list
#return a diary entry with the most appropriate number of words for the users wpm and timeframe

#Test if the variables are being assigned - returns empty list or current state of list varaible
#Test both the entries list and the todo list variables
#Test adding values to both lists and return the lists to see if they have been added
#Test inputs with phone numbers and run function to check for valid phone numbers
#Test reading diary entry with wpm and reading time values - return best matching diary entry
#Test with invalid inputs (reading time function with incorrect values)
#Test if an entry with "TODO" is added to the right list

def test_initially_assigned_variables_entry():
    entry = Entry("Hello this is my diary entry. :)")
    assert entry.entry == "Hello this is my diary entry. :)"

def test_type_of_entry_TODO():
    entry = Entry("TODO: pick up clothes")
    typeEntry = entry.entry_type()
    assert typeEntry == False

def test_type_of_entry():
    entry = Entry("Entry: i picked up clothes")
    typeEntry = entry.entry_type()
    assert typeEntry == True

def test_returning_lists_diary_Entry():
    diary = Diary()
    result = diary.all(True)
    assert result == []

def test_returning_lists_diary_Todo():
    diary = Diary()
    result = diary.all(False)
    assert result == []

