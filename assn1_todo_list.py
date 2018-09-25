# To Do list - Initially prompts to create a user.  It then prompts user to add tasks.

class Task:
    def __init__(self, task_name):
        self.task_name = task_name
        self.priority = "priority: none"


class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task_object(self, task_name):
        self.tasks.append(Task(task_name))

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


def create_user():
    continue_prompt = True

    while continue_prompt:
        user = input("Create a user: ")

        if user.isalpha():
            continue_prompt = False
            return User(user)


def task_commands(user):
    while True:
        prompt = input("Enter task command (a-add v-view r-remove p-setpriority q-exit): ")

        if (prompt == "a"):
            task_name = input("Enter task name: ")
            user.add_task_object(task_name)

        elif (prompt == "v"):
            user.view_tasks()

        elif (prompt == "p"):
            task_name_prompt = input("Enter existing task name to set priority: ")
            priority_value_prompt = input("Enter priority for the task: ")
            user.set_task_priority(task_name_prompt, priority_value_prompt)

        elif (prompt == "r"):
            task_name_prompt = input("Enter existing task name to remove: ")
            user.remove_task(task_name_prompt)

        elif (prompt == "q"):
            break

        else:
            print("Invalid task command")


continue_app = True
print("# To Do List App Started #")
while continue_app:

    user = create_user()

    task_commands(user)

    print("# To Do List App Ended #")
    continue_app = False

