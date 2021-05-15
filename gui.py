import tkinter as tk
from typing import Text

root = tk.Tk()
root.geometry("500x500")
root.title("Just Login")

tk.Label(root, text = "Enter Login Details").pack()
tk.Label(root, text="").pack()

user_name = tk.StringVar()
name_entry = tk.Entry(root, textvariable=user_name).pack()
tk.Label(root, text="").pack()

phone_number = tk.StringVar()
number_entry = tk.Entry(root, textvariable=phone_number).pack()
tk.Label(root, text="").pack()

def get_input():
    name = user_name.get()
    number = phone_number.get()
    print(name, number)

submit_button = tk.Button(root, textvariable="Login", width=10, height=5, command=get_input).pack()

root.mainloop()