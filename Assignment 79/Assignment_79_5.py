""" 5: Basic Login Form
Develop a Tkinter application that accepts a username and password using Entry widgets. Provide a Login
button to validate the entered credentials against predefined values and display an appropriate success or failure
message.
"""

import tkinter as tk

root = tk.Tk()

root.title("Login Form")
root.geometry("300x200")

tk.Label(root, text="Jay Ganesh",
         font=("Arial", 15, "bold")).pack(padx=10)

tk.Label(root, text="Enter Username :").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Password").pack()
entry2 = tk.Entry(root)
entry2.pack()

def login():
    Username = entry1.get()
    Password = entry2.get()

    if Username == "admin" and Password == "1234":
        labelResult.config(text="Login Successful")
    else:
        labelResult.config(text="Invalid Username or Password")

tk.Button(root, text="Login", command=login).pack(pady=15)

labelResult = tk.Label(root, text="", font=("Arial", 12))
labelResult.pack()

root.mainloop()