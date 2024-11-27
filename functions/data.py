import tkinter as tk

def Data(window, labelText):
    containerData = tk.Frame(window, bg="lightgray")
    containerData.pack(fill="x", padx=10, pady=5)

    labelData = tk.Label(containerData, text=labelText, width=20, anchor="w")
    labelData.pack(side="left", padx=5)

    inputData = tk.Entry(containerData, width=40)
    inputData.pack(side="left", padx=5)
