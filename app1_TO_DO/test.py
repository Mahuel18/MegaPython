import PySimpleGUI as sg
import test1

sg.theme("Black")

feet_label = sg.Text("Enter feet:")
inches_label = sg.Text("Enter inches:")

feet_input = sg.InputText(key="feet")
inches_input = sg.InputText(key="inches")

result_label = sg.Text()

convert_btn = sg.Button("Convert")
exit_btn = sg.Button("Exit")

windows = sg.Window(
    "Convertor",
    layout=[
        [feet_label, feet_input],
        [inches_label, inches_input],
        [convert_btn, exit_btn, result_label],
    ],
)

while True:
    event, values = windows.read()
    match event:
        case "Convert":
            result = test1.convert(values["feet"], values["inches"])
            result_label.update(result)

        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
windows.close()
