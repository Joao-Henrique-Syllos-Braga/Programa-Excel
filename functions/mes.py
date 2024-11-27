import tkinter as tk

def Mes(window, labelText, inputs_dict):
    containerMes = tk.Frame(window, bg="lightgray")
    containerMes.pack(fill="x", padx=10, pady=5)

    labelMes = tk.Label(containerMes, text=labelText, width=20, anchor="w")
    labelMes.pack(side="left", padx=5)

    inputMes = tk.Entry(containerMes, width=40)
    inputMes.pack(side="left", padx=5)

    inputs_dict[labelText] = inputMes