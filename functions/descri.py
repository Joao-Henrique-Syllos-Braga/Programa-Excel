import tkinter as tk

def Descri(window, labelText):
    containerDescri = tk.Frame(window, bg="lightgray")
    containerDescri.pack(fill="x", padx=10, pady=5)

    labelDescri = tk.Label(containerDescri, text=labelText, width=20, anchor="w")
    labelDescri.pack(side="left", padx=5)

    inputDescri = tk.Entry(containerDescri, width=40)
    inputDescri.pack(side="left", padx=5)
