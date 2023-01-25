# remake weather app using PySimpleGUI
import PySimpleGUI as sg

import weather

layout = [
    [sg.Text("Enter a city and :")],
    [sg.Input(key="-IN-")],
    [sg.Text(size=(30, 5), key="-OUT-")],
    [sg.Button("Submit", bind_return_key=True),
     sg.Button("Reset"), sg.Button("Exit")],
]

window = sg.Window("Weather App", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == "Exit":
        break

    window["-IN-"].update("")

    if event == "Submit":
        try:
            window["-OUT-"].update(weather.get_current_weather(values['-IN-']))
        except KeyError:
            window["-OUT-"].update("Please enter a valid city.")
    else:
        window["-OUT-"].update("")


window.close()
