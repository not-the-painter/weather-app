from tkinter import *

import weather


def get_user_input():
    pass


root = Tk()
# root.minsize(500, 350)
root.title('Simple Weather App')

city_lbl = Label(root, text='City: ', justify='left')
city_lbl.grid(row=0, column=0)
city_input = Entry(root)
city_input.grid(row=0, column=1)
get_city_btn = Button(root, command=get_user_input)

show_weather = weather.get_current_weather('Ottawa')

show_lbl = Label(root, padx=25, pady=10, text=show_weather, justify='left')
show_lbl.grid(row=1, column=0)

root.mainloop()
