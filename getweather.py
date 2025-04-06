# remake weather app using PySimpleGUI
import PySimpleGUI as sg

import weather


def getweather():
    layout = [
        [sg.Text("Enter a city or region:", size=(20, 1))],
        [sg.Input(key="-IN-")],
        [sg.Text(size=(40, 5), key="-OUT-")],
        [
            sg.Button("Submit", bind_return_key=True),
            sg.Button("Reset"),
            sg.Button("Exit"),
        ],
    ]

    window = sg.Window("Weather App", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break

        window["-IN-"].update("")

        if event == "Submit":
            try:
                result = weather.get_current_weather(values["-IN-"])
                window["-OUT-"].update(result)
            except KeyError:
                window["-OUT-"].update("Please enter a valid city.")
        else:
            window["-OUT-"].update("")

    window.close()


if __name__ == "__main__":
    getweather()
