""" 4: Voting Eligibility Checker
Develop a Tkinter application that accepts a person's name and age. Provide a Check Eligibility button to
determine whether the person is eligible to vote based on the minimum age of 18 years.
"""


import tkinter as tk

root = tk.Tk()

root.title("Voting Eligibility Checker")
root.geometry("400x300")

tk.Label(root, text="Jay Ganesh",
         font=("Arial", 15, "bold")).pack(padx=10)

tk.Label(root, text="Enter Person Name:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Age:").pack()
entry2 = tk.Entry(root)
entry2.pack()

def CheckEligibility():
    Name = entry1.get()
    Age = int(entry2.get())

    if Age >= 18:
        labelResult.config(text=Name + " is Eligible to Vote")
    else:
        labelResult.config(text=Name + " is Not Eligible to Vote")

tk.Button(root, text="Check Eligibility",
          command=CheckEligibility).pack(pady=15)

labelResult = tk.Label(root, text="", font=("Arial", 12))
labelResult.pack()

root.mainloop()