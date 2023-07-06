from modules import functions
import PySimpleGUI as sg
#instead of typing the long name again we give it an alias with as

label = sg.Text('Type in a task')
input = sg.InputText(tooltip="Enter Task", key='todo')
add_button = sg.Button('Add')
window = sg.Window('My Task App', layout=[[label,input],[add_button]], font=('Helvetica',15))
# everything contained in one list in the big list argument will be displayed as one row
while True:
    event,values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos('todos.txt')
            to_be_added = values['todo']+ '\n'
            todos.append(to_be_added)
            functions.write_todos('todos.txt',todos)
        case sg.WIN_CLOSED:
            break
window.close()






