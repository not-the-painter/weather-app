# Weather app using tkinter
import tkinter as tk
from tkinter import ttk

import weather


def getweather():
    root = tk.Tk()
    root.title("Weather App")

    tk.Label(root, text="Enter a city or region:").pack(anchor="w", padx=8, pady=(8, 0))
    entry = tk.Entry(root, width=40)
    entry.pack(fill="x", padx=8, pady=(0, 4))

    out = tk.Text(root, height=5, width=40, wrap="word")
    out.pack(fill="x", padx=8, pady=(0, 4))

    btn_frame = tk.Frame(root)
    btn_frame.pack(fill="x", padx=8, pady=(0, 8))

    def on_submit(event=None):
        city = entry.get()
        entry.delete(0, tk.END)
        try:
            result = weather.get_current_weather(city)
            out.delete("1.0", tk.END)
            out.insert("1.0", result)
        except KeyError:
            out.delete("1.0", tk.END)
            out.insert("1.0", "Please enter a valid city.")

    def on_reset():
        entry.delete(0, tk.END)
        out.delete("1.0", tk.END)

    def on_exit():
        root.destroy()

    ttk.Button(btn_frame, text="Submit", command=on_submit).pack(side="left", padx=(0, 4))
    ttk.Button(btn_frame, text="Reset", command=on_reset).pack(side="left", padx=(0, 4))
    ttk.Button(btn_frame, text="Exit", command=on_exit).pack(side="left")

    def on_return(_event=None):
        on_submit()
        return "break"

    entry.bind("<Return>", on_return)
    root.protocol("WM_DELETE_WINDOW", on_exit)

    entry.focus_set()
    root.mainloop()


def main() -> None:
    getweather()


if __name__ == "__main__":
    main()
