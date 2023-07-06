#from functions import get_todos,write_todos
from modules import functions
#if functions is only in a file in the same directory we write import functions only
import time
#import glob
time_current = time.strftime('%b %d %Y time: %H:%M')
print(time_current)
#filesList = glob.glob('./files/*.txt')
#for file in filesList:
    #with open(file,'w') as file:
        #file.writelines('Hello')
#print(glob.glob('./files/*.txt'))
while True:
    user_action = input('Enter add or show or exit or edit or complete').strip()
    if user_action.startswith('add'):
        #user_input = input('add task') + "\n"
        #file=open('todos.txt','r')
        #tasks = file.readlines()
        #file.close()
        task = user_action[4:] + '\n'
        #with open('todos.txt', 'r') as file:
            #tasks = file.readlines()
        tasks = functions.get_todos('todos.txt')

        tasks.append(task)
        functions.write_todos('todos.txt', tasks)
        #with open('todos.txt', 'w') as file:
            #file.writelines(tasks)
        #file = open('todos.txt','w')
        #file.writelines(tasks)
        #file.close()
    elif 'show' in user_action:
        #file = open('todos.txt', 'r')
        #tasks = file.readlines()
        #file.close()

        #new_tasks=[item.strip("\n") for item in tasks]
        #with open('todos.txt','r') as file:
            #tasks = file.readlines()
        tasks = functions.get_todos('todos.txt')
        for index, task in enumerate(tasks):
          task= task.capitalize().strip('\n')
          row = f"{index}-{task}"
          print(row)
    elif 'exit' in user_action:
        break
    elif 'complete' in user_action:
        #completed_rank = input('Enter position to be completed')
        try:
            completed_rank = user_action[9:]
            tasks = functions.get_todos('todos.txt')
            task_tobe_removed = tasks[int(completed_rank)].strip('\n')
            tasks.pop(int(completed_rank))
            with open('todos.txt','w') as file:
                file.writelines(tasks)
            message = f"Task {task_tobe_removed} has been removed!"
            print(message)
            print(message)
        except IndexError:
            print('Your index is out of range')
            continue
    elif 'edit' in user_action:

        #number = input('Please add a number')
        #number = user_action[5:]
        try:
            tobe_edited = user_action[5:]
            print(tobe_edited)
            tasks = functions.get_todos('todos.txt')
            print(tasks)
            #task_item = tasks[int(number)]
            #print(task_item)
            new_todo = input('enter new task')
            index_of_tobe_edited = tasks.index(tobe_edited.lower()+'\n')
            #tasks[int(number)]=f"{new_todo}"+'\n'
            tasks[index_of_tobe_edited] = f"{new_todo}" + '\n'
            print(tasks)
            #with open('todos.txt', 'w') as file:
                #file.writelines(tasks)
            functions.write_todos('todos.txt', tasks)
        except ValueError:
            print('Your command is not valid')
            user_action = input('Enter add or show or exit or edit or complete').strip()
    #case _:
        #print('Command not found')
    else:
        print('Command not found')
print('you have exited')


