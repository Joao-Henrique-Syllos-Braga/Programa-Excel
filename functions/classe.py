import tkinter as tk

def Classe(window, labelText):
    containerClasse = tk.Frame(window, bg="lightgray")
    containerClasse.pack(fill="x", padx=10, pady=5)

    labelClasse = tk.Label(containerClasse, text=labelText, width=20, anchor="w")
    labelClasse.pack(side="left", padx=5)

    inputClasse = tk.Entry(containerClasse, width=40)
    inputClasse.pack(side="left", padx=5)
