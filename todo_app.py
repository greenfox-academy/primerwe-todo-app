import sys

class Controller():
    def __init__(self):
        self.list_argv = []
        self.arg_reader()
        self.controller()
    
    def arg_reader(self):
        
    
    def controller(self)

class Model()
    def __init__(self):
        self.txt = ''
        self.open_read()

    def open_read(self):
        todos = open('todo_list.txt', 'r')
        self.txt = todos.readlines()
        todos.close()

    def open_write(self):
        todos = open('todo_list.txt', 'w')
        todos.writelines(self.txt)
        todos.close()
        
    def add_todo(self, text):
        self.txt.append('[ ] ' + text + '\n')
        self.open_write()
    
    def remove_todo(self, item):
        self.txt.remove[item]
        self.open_write()

    def complete_todo(self, item):
        self.txt[item].replace('[ ]', '[X]', 1)
        self.open_write()
     
    
        
class View():
    
    def __init__(self):
        self.commands = [
            {'argument': '-l', 'description' : 'Lists all the tasks'},
            {'argument': '-a', 'description' : 'Adds a new task'},
            {'argument': '-r', 'description' : 'Removes a task'},
            {'argument': '-c', 'description' : 'Completes a task'}
        ]
        
    def print_commands(self):
        print('Command Line Todo application\n' + '=============================\n' + 'Command line arguments:\n\n')
        for i in self.commands:
            print(i['argument'] + ' ' + i['description'])
    
    
    
model = Model()
view = View()
control = Controller()