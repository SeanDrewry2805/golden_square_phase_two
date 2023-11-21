from lib.ChallengeDiary import *
from lib.ChallengeEntry import *
import pytest

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
#Test inputs with phone numbers and run function to check for valid phone numbers - returns all numbers
#Test reading diary entry with wpm and reading time values - return best matching diary entry
#Test with invalid inputs (reading time function with incorrect values

# def test_initial_integration():
#     entry = Entry("Hello this is my diary entry. :)")
#     diary = Diary()
#     result = diary.add_entry(entry)
#     assert result == "Hello this is my diary entry. :)"

def test_type_of_entry_insert_todo():
    diary = Diary()
    entry = Entry("TODO: pick up clothes")
    typeEntry = entry.entry_type()
    diary.add_entry(entry)
    assert diary.all(typeEntry) == [entry]
    
def test_type_of_entry_insert():
    diary = Diary()
    entry = Entry("Entry: I picked up clothes")
    typeEntry = entry.entry_type()
    diary.add_entry(entry)
    assert diary.all(typeEntry) == [entry]
    
def test_finding_phone_numbers():
    diary = Diary()
    entry = Entry("Entry: I picked up clothes and called 07876345654")
    diary.add_entry(entry)
    result = diary.find_numbers()
    assert result == ["07876345654"]

def test_finding_multiple_phone_numbers():
    diary = Diary()
    entry = Entry("Entry: I picked up clothes and called 07876345654")
    entry2 = Entry("Entry: I picked up clothes and called 01234123423")
    diary.add_entry(entry)
    diary.add_entry(entry2)
    result = diary.find_numbers()
    assert result == ["07876345654", "01234123423"]

def test_reading_best_entry():
    diary = Diary()
    entry = Entry("Entry: I picked up clothes and called 07876345654") #8
    entry2 = Entry("Entry: I picked up clothes and called my friend 01234123423") #10
    diary.add_entry(entry)
    diary.add_entry(entry2)
    result = diary.reading_best_entry(1, 10)
    assert result == entry2

def test_reading_3_entries():
    diary = Diary()
    entry = Entry("Entry: I picked up clothes and called 07876345654") #8
    entry2 = Entry("Entry: I picked up clothes and called my friend 01234123423") #10
    entry3 = Entry("Entry: I picked up clothes and called my friend 01234123423 and we went shopping happilly") #15
    diary.add_entry(entry)
    diary.add_entry(entry2)
    diary.add_entry(entry3)
    result = diary.reading_best_entry(1, 10)
    assert result == entry2

def test_reading_3_entries_invalid_parameters():
    diary = Diary()
    entry = Entry("Entry: I picked up clothes and called 07876345654") #8
    entry2 = Entry("Entry: I picked up clothes and called my friend 01234123423") #10
    entry3 = Entry("Entry: I picked up clothes and called my friend 01234123423 and we went shopping happilly") #15
    diary.add_entry(entry)
    diary.add_entry(entry2)
    diary.add_entry(entry3)
    with pytest.raises(Exception) as e:
        result = diary.reading_best_entry(0, 10)
    assert str(e.value) == "Invalid numbers"