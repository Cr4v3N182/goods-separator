import PySimpleGUI as sg

label = sg.Text("Paste Indexes.")
index_input = sg.Input("", key='input')
exit_button = sg.Button("Exit", key='exit')

layout = [[label],[index_input],[exit_button]]

window = sg.Window("goods-separator", layout=layout, size=(400,100))

while True:
    event, values = window.read()
    match event:
        case 'exit':
            break
        case sg.WIN_CLOSED:
            break
window.close()
