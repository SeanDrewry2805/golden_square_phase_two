from lib.todo_list import *

'''
When I initialise a TodoList
It contains an empty list parameter
'''
def test_todo_list():
    list = TodoList()
    assert list.todos == []