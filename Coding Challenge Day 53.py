import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
heading = tk.Label(
    text="Welcome to Scribble Zone",
    fg="white",
    bg="orange",
    width=50,
    height=25
    ).pack()

window.mainloop()

button = tk.Button(
    text="URGENT-CLICK TO VIEW",
    width=20,
    height=5,
    bg="orange",
    fg="red",
    ).pack()

label = tk.Label(text="SSN*").pack()
entry = tk.Entry(fg="white", bg="black", width=50).pack()



