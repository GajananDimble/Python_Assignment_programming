""" 2: Find the Largest Number
Develop a Tkinter application that accepts three numbers from the user. Provide a Find Maximum button to
determine and display the largest number.
"""

import tkinter as tk

root = tk.Tk()

root.title("Find The Largest Number")
root.geometry("400x300")

tk.Label(root, text="Jay Ganesh",
         font=("Arial", 15, "bold")).pack(padx=10)

tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Enter Third Number").pack()
entry3 = tk.Entry(root)
entry3.pack()

def LargestNum():
    no1 = int(entry1.get())
    no2 = int(entry2.get())
    no3 = int(entry3.get())

    Maximum = max(no1,no2,no3)

    labelResult.config(text="Largest Number is :"+str(Maximum))

tk.Button(root, text="Find Maximum", command=LargestNum).pack(pady=15)

labelResult = tk.Label(root, text="", font=("Arial", 15))
labelResult.pack()

root.mainloop()