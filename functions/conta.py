import tkinter as tk

def Conta(window, labelText):
    containerConta = tk.Frame(window, bg="lightgray")
    containerConta.pack(fill="x", padx=10, pady=5)

    labelConta = tk.Label(containerConta, text=labelText, width=20, anchor="w")
    labelConta.pack(side="left", padx=5)

    inputConta = tk.Entry(containerConta, width=40)
    inputConta.pack(side="left", padx=5)
