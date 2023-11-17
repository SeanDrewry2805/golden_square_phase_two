from lib.todo import *

class TodoList:
    def __init__(self):
        self.todos = []
        self.completed = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todos.append(todo)

    def mark_complete(self):
        # Parameters:
        #   none
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks a specified todo as complete
        self.incomplete()
        print('\n')
        text_input = input("What task have you completed?")
        # sorted = list(filter(lambda i: text_input in i.task, self.todos))
        # sorted = [i for i in self.todos if text_input not in i.task]
        # self.completed = [i for i in self.todos if text_input in i.task]
        # self.todos = sorted
        for task in self.todos:
            if text_input in task.task:
                task.mark_complete()
        self.completed = [i for i in self.todos if i.complete == True]
        sorted = [i for i in self.todos if i.complete == False]
        self.todos = sorted
        

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        list = [todo.task for todo in self.todos]
        text = '\n'.join(list)
        print(f'Tasks:\n{text}')
        return f'Tasks:\n{text}'

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        list = [todo.task for todo in self.completed]
        text = '\n'.join(list)
        print(text)
        return f'Completed Tasks:\n{text}'

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for i in self.todos:
            i.mark_complete()
        self.completed = [i for i in self.todos if i.complete == True]
        sorted = [i for i in self.todos if i.complete == False]
        self.todos = sorted
        