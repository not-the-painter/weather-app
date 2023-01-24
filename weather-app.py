from tkinter import *

import weather

root = Tk()
root.geometry("400x250")
root.title('Simple Weather App')

global show_lbl
show_lbl = Label(root, text="", justify='left')


def get_user_input(event=None):
    global show_lbl
    show_weather = weather.get_current_weather(city_input.get())
    city_input.delete("0", END)
    show_lbl.config(text=show_weather)
    show_lbl.grid(row=2, column=0, columnspan=5)


def reset():
    global show_lbl
    show_lbl.destroy()


city_lbl = Label(root, text='Enter the city: ')
city_lbl.grid(row=0, column=0)

city_input = Entry(root)
city_input.grid(row=0, column=1, columnspan=4)
city_input.focus()

city_input.bind('<Return>', get_user_input)

get_city_btn = Button(root, text="Submit", command=get_user_input)
get_city_btn.grid(row=1, column=1)

quit_btn = Button(root, text="Quit", width=6, command=quit)
quit_btn.grid(row=1, column=2)

reset_btn = Button(root, text="Reset", width=6,
                   command=reset)
reset_btn.grid(row=1, column=3)

root.mainloop()
