import PySimpleGUI as sg
import pandas as ps

label = sg.Text("Paste Indexes.")
index_input = sg.Input("", key='input')
goods_get_input = sg.Button("G00DS", key='goods')
sql_get_input = sg.Button("SQL", key='sql')
exit_button = sg.Button("Exit", key='exit')

layout = [[label],
          [index_input],
          [goods_get_input, sql_get_input, exit_button]]

window = sg.Window("goods-separator-powered by Cr4v3n182",
                   layout=layout, size=(400,100),
                   font=('Helvetica', 10))

while True:
    event, values = window.read()
    match event:
        case 'goods':
            with open("goods_sep.csv", "w") as file:
                index = values['input'].replace("\n", ",")
                file.write(index)
                sg.popup("Goods convertion completed")
        case 'sql':
            with open("sql_synt.csv", "w") as file:
                sql_values = values['input'].replace("\n", ", ")
                sql_req = sql_values.split(", ")
                sql_req = sql_req[:-1]
                sql_req = tuple(map(str, sql_values.split(", ")))
                file.write(str(sql_req))
                sg.popup("SQL convertion completed")
        case 'exit':
            break
        case sg.WIN_CLOSED:
            break
window.close()

