from lib.Todo_checker import *

"""
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.
"""

#test with a string containing the tag "#TODO"
#test with a string that has no tag
#test with a string with part of the tag ie "TODO" (no hashtag)

#def test_todo_checker():
#    result = todo_checker("Hello world!")
#    assert result == None

def test_todo_checker_correct():
    result = todo_checker("Empty the dishwasher #TODO")
    assert result == True

def test_todo_checker_incorrect():
    result = todo_checker("Dont empty the dishwasher")
    assert result == False

def test_todo_checker_partially_incorrect():
    result = todo_checker("Dont empty the dishwasher TODO")
    assert result == False