import PySimpleGUI as sg
from zipcreator import compress

label1 = sg.Text('Select files to compress')
input1 = sg.InputText(tooltip="Select file")
add_button1 = sg.FilesBrowse('Choose', key='file')
label2 = sg.Text('Select destination folder')
input2 = sg.InputText(tooltip="Select destination folder")
add_button2 = sg.FolderBrowse('Choose', key='folder')
compress_button = sg.Button('Compress')
message = sg.Text(key='FinalMessage')
window = sg.Window('File Compressor', layout=[[label1,input1,add_button1],[label2,input2,add_button2],[compress_button,message]])

while True:
    event,values= window.read()
    print(event,values)
    files = values['file'].split(';')
    folder = values['folder']
    compress(files,folder)
    window['FinalMessage'].update(value='compresion conmplete!')
window.close()