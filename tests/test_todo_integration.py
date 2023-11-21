from lib.todo import *
from lib.todo_list import *

'''
Given I add a Todoo to my list
The results are saved in a list parameter of the TodoList
'''
def test_add_todo_to_list():
    task = Todo('Water the plants')
    list = TodoList()
    list.add(task)
    assert list.incomplete() == 'Tasks:\nWater the plants'

'''
Given I have added to my list and call incomplete
I will see a list of unfinished todos
'''
def test_show_incomplete():
    list = TodoList()
    task_one = Todo('Water the plants')
    task_two = Todo('Bake some bread rolls')
    list.add(task_one)
    list.add(task_two)
    assert list.incomplete() == f'Tasks:\nWater the plants\nBake some bread rolls'

'''
Given I have added to my list
I can mark an item as completed
'''
def test_mark_completed_adds_to_completed(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Bake some bread rolls')
    list = TodoList()
    task_one = Todo('Play squash')
    task_two = Todo('Bake some bread rolls')
    task_three = Todo('Water the plants')
    list.add(task_one)
    list.add(task_two)
    list.add(task_three)
    list.mark_complete()
    assert list.complete() == 'Completed Tasks:\nBake some bread rolls'

def test_mark_completed_removes_from_incomplete(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Bake some bread rolls')
    list = TodoList()
    task_one = Todo('Play squash')
    task_two = Todo('Bake some bread rolls')
    task_three = Todo('Water the plants')
    list.add(task_one)
    list.add(task_two)
    list.add(task_three)
    list.mark_complete()
    assert list.incomplete() == 'Tasks:\nPlay squash\nWater the plants'

'''
Given I have added to my list, completed a task and call complete
I will see a list of finished todos
'''

'''
Given I have added to my list and call give_up
I will make all my todos as complete
'''
def test_giving_up():
    list = TodoList()
    task_one = Todo('Play squash')
    task_two = Todo('Go for a walk at lunch')
    list.add(task_one)
    list.add(task_two)
    list.give_up()
    assert list.incomplete() == 'Tasks:\n'