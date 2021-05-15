import tkinter as tk
import requests

URL = "http://127.0.0.1:9000"

root = tk.Tk()
root.geometry("500x500")
root.title("Just Login with user details")

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
    dictionary = {}
    dictionary['name'] = name
    dictionary['number'] = number
    result = requests.post(URL+"/login",data=dictionary)
    print(result.text)

submit_button = tk.Button(root, textvariable="Login", width=10, height=5, command=get_input).pack()

root.mainloop()