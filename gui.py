from modules import functions
import PySimpleGUI as sg
#instead of typing the long name again we give it an alias with as

label = sg.Text('Type in a task')
input = sg.InputText(tooltip="Enter Task", key='todo')
add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
list_box = sg.Listbox(values=functions.get_todos('todos.txt'), key='todos',enable_events=True, size=[45, 10])
window = sg.Window('My Task App', layout=[[label,input],[list_box,edit_button,complete_button],[add_button]], font=('Helvetica',15))
# everything contained in one list in the big list argument will be displayed as one row
while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos('todos.txt')
            to_be_added = values['todo']+ '\n'
            todos.append(to_be_added)
            functions.write_todos('todos.txt',todos)
            window['todos'].update(values=todos)
        case "Edit":
            chosen_task = values['todos'][0]
            todos = functions.get_todos('todos.txt')
            index_chosen = todos.index(chosen_task)
            new_task = values['todo']
            todos[index_chosen]=new_task
            functions.write_todos('todos.txt',todos)
            print(todos)
            window['todos'].update(values=todos)

        case 'Complete':
            chosen_task = values['todos'][0]
            todos = functions.get_todos('todos.txt')
            index_chosen = todos.index(chosen_task)
            todos.pop(index_chosen)
            functions.write_todos('todos.txt',todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case sg.WIN_CLOSED:
            break
            # if we use exit() program quits without executing window.close()
        case todos:
            window['todo'].update(value=values['todos'][0])
window.close()






