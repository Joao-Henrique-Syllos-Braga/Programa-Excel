import tkinter as tk

def Fc(window, labelText):
    containerFc = tk.Frame(window, bg="lightgray")
    containerFc.pack(fill="x", padx=10, pady=5)

    labelFc = tk.Label(containerFc, text=labelText, width=20, anchor="w")
    labelFc.pack(side="left", padx=5)

    inputFc = tk.Entry(containerFc, width=40)
    inputFc.pack(side="left", padx=5)