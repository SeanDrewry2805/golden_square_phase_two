'''
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.
'''

import pytest # type: ignore
from lib.TaskTracker import *

def test_list_of_tasks_add_task():
    # will check the class has a public variable for holding tasks in a list
    tracker = TaskTracker()
    tracker.add_task('Water the plants')
    assert tracker.show_tasks() == 'Water the plants'

def test_show_tasks_format():
    # will return a list of tasks in the correct format
    tracker = TaskTracker()
    tracker.tasks = []
    tracker.add_task('Mow the lawn')
    tracker.add_task('Make lasagna')
    assert tracker.show_tasks() == 'Mow the lawn, Make lasagna'


def test_remove_task(monkeypatch):
    # will initlaise a tracker and add some items to the list
    # will remove a task from the list and reutnr the list to prove it has gone
    monkeypatch.setattr('builtins.input', lambda _ :"Mow the lawn")
    tracker = TaskTracker()
    tracker.tasks = []
    tracker.add_task('Mow the lawn')
    tracker.add_task('Make lasagna')
    complete_task = tracker.complete_task()
    assert complete_task == 'Make lasagna'


def test_remove_task_from_longer_list(monkeypatch):
    # will initlaise a tracker and add some items to the list
    # will remove a task from the list and reutnr the list to prove it has gone
    monkeypatch.setattr('builtins.input', lambda _ :"Mow the lawn")
    tracker = TaskTracker()
    tracker.tasks = []
    tracker.add_task('Mow the lawn')
    tracker.add_task('Make lasagna')
    tracker.add_task('Do the laundry')
    tracker.add_task('Take out the recycling')
    complete_task = tracker.complete_task()
    assert complete_task == 'Make lasagna, Do the laundry, Take out the recycling'