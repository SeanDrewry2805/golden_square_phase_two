from lib.Todo import *
from lib.TodoList import *

def test_initial_functionality():
    ToDo1 = Todo("Clean up the house before my parents get home.")
    assert ToDo1.dict == {"task": "Clean up the house before my parents get home.", "status": False}