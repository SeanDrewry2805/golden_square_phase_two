from lib.todo import *

'''
Given I initialise Todo with a task
The Todo object has assigned a task and a complete property
'''
def test_todo_title():
    task = Todo('Wash the dog')
    assert task.task == 'Wash the dog'

def test_todo_complete_property():
    task = Todo('Wash the dog')
    assert task.complete == False

'''
Given I mark a Todo as completed
The completed property toggles to True
'''
def test_complete_todo():
    task = Todo('Wash the dog')
    task.mark_complete()
    assert task.complete == True