import unittest
from task_model import Task_Model 
from splinter import Browser

test_browser = True

class Test_Task_Model(unittest.TestCase):
    def setUp(self):
        self.task_model = Task_Model()

    def test_add_tasks(self):
        tasks = ["Mop floor", "Write task", "Run Game"]
        for task in tasks:
            self.task_model.add_task(task)
        assert self.task_model.get_size() == 3

    def test_add_tasks_web(self):
        if(test_browser):
            with Browser() as browser:
                url = "http://127.0.0.1:5000/"
                browser.visit(url)
                browser.fill('task', 'Write test')
                button = browser.find_by_name('task_submit')
                button.click()
                browser.visit(url)
                browser.fill('task', 'Test test')
                button = browser.find_by_name('task_submit')
                button.click()
                assert browser.is_text_present('Test test')
                assert browser.is_text_present('Write test')
                assert browser.is_text_present('Tasks')

    def test_randomly_select(self):
        tasks = ["Write test", "Pass Test", "Revise"] 
        for task in tasks:
            self.task_model.add_task(task)
        for i in range(3):
            rand = self.task_model.randomly_select_task()
            assert rand in tasks

    def test_select_tasks_web(self):
        tasks = ['Drink tea', 'Listen to know-it-all', 'Be humble']
        if(test_browser):
            with Browser() as browser:
                url = "http://127.0.0.1:5000/"
                browser.visit(url)
                for task in tasks:
                    browser.fill('task', task)
                    button = browser.find_by_name('task_submit')
                    button.click()
                button = browser.find_by_name('task_select')
                button.click()
                task =  browser.find_by_name('selected_task').value
                assert task in tasks, task + " is not in tasks"

    def test_remove_tasks(self):
        tasks = ['Sit here thinking', 'Write some code', 'Destress']
        for task in tasks:
            self.task_model.add_task(task)
        rtasks = self.task_model.get_all_tasks()
        assert rtasks == tasks
        self.task_model.remove_task(tasks[0])
        rtasks = self.task_model.get_all_tasks()
        assert tasks[0] not in rtasks

    def test_remove_tasks_web(self):
        tasks = ['Drink tea', 'Listen to know-it-all', 'Be humble']
        if(test_browser):
            with Browser() as browser:
                url = "http://127.0.0.1:5000/"
                browser.visit(url)
                for task in tasks:
                    browser.fill('task', task)
                    button = browser.find_by_name('task_submit')
                    button.click()
                button = browser.find_by_name('0_delete')
                button.click()
                assert browser.is_text_present("Listen to know-it-all")
                assert browser.is_text_present("Be humble")
                assert browser.is_text_not_present("Drink tea")
        
        
        


                

    
    def tearDown(self):
        pass
    


    
if (__name__ == "__main__"):
    unittest.main()

