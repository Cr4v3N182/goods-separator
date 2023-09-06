import PySimpleGUI as sg
import pandas as ps

label = sg.Text("Paste Indexes.")
index_input = sg.Input("", key='input')
get_input = sg.Button("GET", key='get')
exit_button = sg.Button("Exit", key='exit')

layout = [[label],[index_input],[get_input, exit_button]]

window = sg.Window("goods-separator", layout=layout, size=(400,100))

while True:
    event, values = window.read()
    match event:
        case 'get':
            with open("goods_sep.csv", "w") as file:
                index = values['input'].replace("\n", ",")
                file.write(index)
                sg.popup("File has been created")
        case 'exit':
            break
        case sg.WIN_CLOSED:
            break
window.close()

