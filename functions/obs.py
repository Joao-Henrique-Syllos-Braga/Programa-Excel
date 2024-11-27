import tkinter as tk

def Obs(window, labelText, inputs_dict):
    containerObs = tk.Frame(window, bg="lightgray")
    containerObs.pack(fill="x", padx=10, pady=5)

    labelObs = tk.Label(containerObs, text=labelText, width=20, anchor="w")
    labelObs.pack(side="left", padx=5)

    inputObs = tk.Entry(containerObs, width=40)
    inputObs.pack(side="left", padx=5)

    inputs_dict[labelText] = inputObs
