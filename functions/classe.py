import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_value = combo.get()  # Get the selected option
    print(f"Selected: {selected_value}")

def Classe(window, labelText, inputs_dict):
    containerClasse = tk.Frame(window, bg="lightgray")
    containerClasse.pack(fill="x", padx=10, pady=5)

    labelClasse = tk.Label(containerClasse, text=labelText, width=20, anchor="w")
    labelClasse.pack(side="left", padx=5)

    # Create a Combobox with a list of options
    options = [1.1, 1.2, 2.01, 2.02, 2.03, 2.04, 2.05, 2.06, 2.07, 2.08, 2.09, 2.20, 2.30, 2.50, 2.51, 2.60]
    combo = ttk.Combobox(containerClasse, values=options)
    combo.pack(pady=10)

    # Bind the combobox to an event (when the selection changes)
    combo.bind("<<ComboboxSelected>>", on_select)

    inputs_dict[labelText] = combo
