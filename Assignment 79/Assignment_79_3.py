""" 3: Area of Circle
Develop a Tkinter application that accepts the radius of a circle. Provide a Calculate Area button to calculate
and display the area of the circle.
"""

import tkinter as tk
import math

root = tk.Tk()

root.title("Area of Circle")
root.geometry("400x300")

tk.Label(root, text="Jay Ganesh",
         font=("Arial", 15, "bold")).pack(padx=10)

tk.Label(root, text="Enter Radius of Circle:").pack()
entry1 = tk.Entry(root)
entry1.pack()

def CalculateArea():
    Radius = float(entry1.get())

    Area = math.pi * Radius * Radius

    labelResult.config(text="Area of Circle: " + str(round(Area, 2)))

tk.Button(root, text="Calculate Area",
          command=CalculateArea).pack(pady=15)

labelResult = tk.Label(root, text="", font=("Arial", 14))
labelResult.pack()

root.mainloop()