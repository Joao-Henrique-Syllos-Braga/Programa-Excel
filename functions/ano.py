import tkinter as tk

def Ano(window, labelText, inputs_dict):
    containerAno = tk.Frame(window, bg="lightgray")
    containerAno.pack(fill="x", padx=10, pady=5)

    labelAno = tk.Label(containerAno, text=labelText, width=20, anchor="w")
    labelAno.pack(side="left", padx=5)

    inputAno = tk.Entry(containerAno, width=40)
    inputAno.pack(side="left", padx=5)

    inputs_dict[labelText] = inputAno