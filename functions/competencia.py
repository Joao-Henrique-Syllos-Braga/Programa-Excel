import tkinter as tk

def Competencia(window, labelText, inputs_dict):
    containerCompetencia = tk.Frame(window, bg="lightgray")
    containerCompetencia.pack(fill="x", padx=10, pady=5)

    labelCompetencia = tk.Label(containerCompetencia, text=labelText, width=20, anchor="w")
    labelCompetencia.pack(side="left", padx=5)

    inputCompetencia = tk.Entry(containerCompetencia, width=40)
    inputCompetencia.pack(side="left", padx=5)

    inputs_dict[labelText] = inputCompetencia