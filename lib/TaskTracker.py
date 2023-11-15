class TaskTracker():
    # list of tasks
    tasks = []

    def __init__(self):
        pass

    def add_task(self, task):
        # take the string as an argumment for a task
        # add that to the list of tasks
        self.tasks.append(task)
        self.show_tasks()

    def show_tasks(self):
        # returns a list of outstanding tasks
        text = ', '.join(self.tasks)
        print(text)
        return text

    def complete_task(self):
        # remove a completed taks from the list
        # takes a name as an argument
        task = input("What task have you finished?")
        sorted = list(filter(lambda i: task not in i, self.tasks))
        text = ', '.join(sorted)
        self.tasks = sorted
        self.show_tasks()
        return text
    
tracker=TaskTracker()

tracker.add_task('Mow the lawn')
tracker.add_task('Make lasagna')
tracker.add_task('Do the laundry')
tracker.add_task('Take out the recycling')

tracker.show_tasks()

tracker.complete_task()