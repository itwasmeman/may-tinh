import tkinter as tk
from tkinter import ttk
import tkinter.ttk as tkk

root = tk.Tk()
root.title("máy tính")

result_var = tk.StringVar()
result_entry = tkk.Entry(root, textvariable=result_var, font=("Sleepy Moody", 24), justify="right")
result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

def nutxuly(nutduocbam):
    nuthientai = result_var.get()
    if nutduocbam == "=":
        try:
            expression = nuthientai.replace("÷", "/").replace("×", "*")
            result = eval(expression)
            # kiem tra thu xem la so co tron ko
            if int(result) == result:
                result = int(result)
            result_var.set(result)
        except:
            result_var.set("Error")
    elif nutduocbam == "C":
        result_var.set("")
    else:
        result_var.set(nuthientai + nutduocbam)

buttons_text = [
    '7', '8', '9', '÷',
    '4', '5', '6', '×',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

for i, buttons_text in enumerate(buttons_text):
    row = i // 4 + 1
    col = i % 4
    colspan = 1
    buttons = tkk.Button(root, text=buttons_text, command=lambda text=buttons_text: nutxuly(text), style="TButton")
    buttons.grid(row=row, column=col, columnspan=colspan, sticky="nsew", ipadx=10, ipady=4, padx=5, pady=5)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

width = 600
height = 900
root.resizable(False, False)
root.bind("<Return>", lambda event: nutxuly("="))
root.bind("<BackSpace>", lambda event: nutxuly("C"))
root.mainloop()