import tkinter as tk
from tkinter import ttk


# functions
def calculate():
    pass

#colors
BACKGROUND_COLOR = "#F0F0F0"
BUTTON_COLOR = "#F4F9E9"

#window
window = tk.Tk()
window.geometry("400x500")
window.title("Calculator")

#display Output
output_frame = tk.Frame(master= window, background=BACKGROUND_COLOR, height=100)
output_frame.pack(fill="x")
output_frame.pack_propagate(False)

outputInt = tk.StringVar()
outputInt.set('0')

calculator_output = ttk.Label(
    master=output_frame, 
    textvariable=outputInt, 
    font=("Times New Roman", 50),
    anchor="e",
    background=BACKGROUND_COLOR,
    )
calculator_output.pack(fill="x", expand=True, padx=20)

#input buttons
input_frame = tk.Frame(master=window, background=BUTTON_COLOR)
input_frame.pack(fill="both", expand=True)
input_frame.pack_propagate(False)

for a in range(4):
    input_frame.rowconfigure(a, weight=1)
for b in range(4):
    input_frame.columnconfigure(b, weight=1)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

button_widgets = {}


for r, row in enumerate(buttons):       
    for c, label in enumerate(row):     
        btn = ttk.Button(input_frame, text=label, command=calculate)
        btn.grid(row=r, column=c, sticky="nsew", padx=1, pady=1)
        button_widgets[label] = btn
    



#loop
window.mainloop()