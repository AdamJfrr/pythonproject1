import PySimpleGUI as sg

label1 = sg.Text('Select files to compress')
input1 = sg.InputText(tooltip="Select file")
add_button1 = sg.FilesBrowse('Choose')
label2 = sg.Text('Select destination folder')
input2 = sg.InputText(tooltip="Select destination folder")
add_button2 = sg.FolderBrowse('Choose')
compress_button = sg.Button('Compress')
window = sg.Window('File Compressor', layout=[[label1,input1,add_button1],[label2,input2,add_button2],[compress_button]])
window.read()
window.close()