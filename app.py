import tkinter as tk
from tkinter import ttk


# functions
def display(value):
    symbols = {"+", "-", "x", "/", "."}
    
    current_text = outputInt.get()
    if current_text == '0' or current_text =="Error" and value not in ['=', 'C', 'AC']:
        if value not in symbols:
            outputInt.set(value) 

    elif value == '=':
        calculate(current_text)
    elif value == 'AC':
        outputInt.set('0')
    elif value == 'C':
        new_text = current_text[:-1]
        outputInt.set(new_text if new_text else '0')

    else:
        if not (value in symbols and current_text[-1] in symbols):
            outputInt.set(current_text + value)


def calculate(value):
    equation = value.replace('x', '*')
    try:
        outputInt.set((eval(equation)))
    except Exception:
        outputInt.set('Error')
        

#colors
BACKGROUND_COLOR = "#E8F6FC"
BUTTON_COLOR = "#E6FAFD"

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
input_frame = tk.Frame(master=window, background=BACKGROUND_COLOR)
input_frame.pack(fill="both", expand=True)
input_frame.pack_propagate(False)

for a in range(4):
    input_frame.rowconfigure(a, weight=1)
for b in range(4):
    input_frame.columnconfigure(b, weight=1)

buttons = [
    ["", "", "C", "AC",],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "x"],
    ["1", "2", "3", "-"],
    [".", "0", "=", "+"],
]

button_widgets = {}


for r, row in enumerate(buttons):       
    for c, label in enumerate(row):     
        btn = tk.Button(
            input_frame, 
            text=label, 
            font=("Times", 20), 
            background=BUTTON_COLOR,
             width=5,height=2,
            command=
            lambda l=label: display(l)
            )
        btn.grid(row=r, column=c, sticky="nsew", padx=1, pady=1)
        button_widgets[label] = btn
    
arian_label = tk.Label(
    input_frame,
    text="made by arian",
    font=("Times", 14),
    background=BACKGROUND_COLOR,
    anchor="center",
    border=1,
    relief="solid",
    foreground="#000000"
)
arian_label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=1, pady=1)



#loop
window.mainloop()