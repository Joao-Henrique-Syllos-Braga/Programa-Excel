import tkinter as tk

def Fornecedor(window, labelText):
    containerFornecedor = tk.Frame(window, bg="lightgray")
    containerFornecedor.pack(fill="x", padx=10, pady=5)

    labelFornecedor = tk.Label(containerFornecedor, text=labelText, width=20, anchor="w")
    labelFornecedor.pack(side="left", padx=5)

    inputFornecedor = tk.Entry(containerFornecedor, width=40)
    inputFornecedor.pack(side="left", padx=5)
