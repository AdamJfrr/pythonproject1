import PySimpleGUI as sg
from modules import converter
label1= sg.Text('Enter feet:')
input1 = sg.Input(tooltip='Enter feet', key='feet')
label2 = sg.Text('Enter inches:')
input2 = sg.Input(tooltip='Enter inches', key='inches')
convert_button = sg.Button('Convert')
output = sg.Text(key='message')
window = sg.Window('Convertor',layout=[[label1,input1],[label2,input2],[convert_button,output]],font=('Helvetica',15))
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Convert':
            feet_value = values['feet']
            inches_value = values['inches']
            result= converter.converter(float(feet_value),float(inches_value))
            window['message'].update(value=result)
        case sg.WIN_CLOSED:
            break
window.close()