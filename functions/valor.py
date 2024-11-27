import tkinter as tk

def Valor(window, labelText):
    containerValor = tk.Frame(window, bg="lightgray")
    containerValor.pack(fill="x", padx=10, pady=5)

    labelValor = tk.Label(containerValor, text=labelText, width=20, anchor="w")
    labelValor.pack(side="left", padx=5)

    inputValor = tk.Entry(containerValor, width=40)
    inputValor.pack(side="left", padx=5)
