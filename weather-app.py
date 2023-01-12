from tkinter import *

import weather


def get_user_input(event=None):
    show_weather = weather.get_current_weather(city_input.get())
    city_input.delete("0", END)
    show_lbl = Label(root, text=show_weather, justify='left')
    show_lbl.grid(row=2, column=0, columnspan=2)


root = Tk()
root.geometry("350x200")
root.title('Simple Weather App')

city_lbl = Label(root, text='Enter the city: ')
city_lbl.grid(row=0, column=0)

city_input = Entry(root)
city_input.grid(row=0, column=1, columnspan=4)
city_input.focus()

city_input.bind('<Return>', get_user_input)

get_city_btn = Button(root, text="Submit", command=get_user_input)
get_city_btn.grid(row=1, column=1)

quit_btn = Button(root, text="Quit", command=quit)
quit_btn.grid(row=1, column=4)
root.mainloop()
