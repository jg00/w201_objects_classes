


class Task:
    def __init__(self, task_name):
        self.task_name = task_name
        self.priority = "priority: none"   #default

class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(task_name)

    def view_tasks(self):
        print(self.name + "\'s tasks:")
        for task in self.tasks:
            print(task.task_name + " (" + task.priority + ")")

    def set_task_priority(self, task_name, priority_value):
        for index in range(len(self.tasks)):
            if self.tasks[index].task_name == task_name:
                self.tasks[index].priority = priority_value
    
    def remove_task(self, task_name):
        for index in range(len(self.tasks)):
            if self.tasks[index].task_name == task_name:
                del self.tasks[index]


jack = User('Jack')

mow = Task('mow')
laundry = Task('laundry')
groceries = Task('groceries')

jack.add_task(laundry)
jack.add_task(groceries)
jack.add_task(mow)

jack.set_task_priority('groceries', 'high')

jack.view_tasks()

jack.remove_task('mow')

jack.view_tasks()