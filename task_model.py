import random
import quantumrandom

class Task_Model:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_size(self):
        return len(self.tasks)

    def randomly_select_task(self):
        try:
            index = quantumrandom.randint(0,len(self.tasks))
        except:
            index = random.randint(0,len(self.tasks)-1)
        return self.tasks[index]

    def remove_task(self, task):
        if (task.isdigit()):
            del self.tasks[int(task)]
        else:
            self.tasks.remove(task)


    def get_all_tasks(self):
        return self.tasks


