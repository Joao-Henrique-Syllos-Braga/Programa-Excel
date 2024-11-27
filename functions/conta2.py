import tkinter as tk

def Conta2(window, labelText):
    containerConta2 = tk.Frame(window, bg="lightgray")
    containerConta2.pack(fill="x", padx=10, pady=5)

    labelConta2 = tk.Label(containerConta2, text=labelText, width=20, anchor="w")
    labelConta2.pack(side="left", padx=5)

    inputConta2 = tk.Entry(containerConta2, width=40)
    inputConta2.pack(side="left", padx=5)
