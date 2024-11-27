import tkinter as tk
from functions.classe import Classe
from functions.conta import Conta
from functions.fc import Fc
from functions.descri import Descri
from functions.fornecedor import Fornecedor
from functions.data import Data
from functions.competencia import Competencia
from functions.valor import Valor
from functions.ano import Ano
from functions.conta2 import Conta2
from functions.obs import Obs

# Create the main window
window = tk.Tk()
window.title("Excel Create")
window.geometry("600x800")

# Initialize input fields dictionary to store all inputs
inputs_dict = {}

# Function to call all input functions
def inputs():
    global inputs_dict  # Reference the global dictionary
    Classe(window, "Classe:", inputs_dict)
    Conta(window, "Conta:", inputs_dict)
    Fc(window, "FC:", inputs_dict)
    Descri(window, "Descrição:", inputs_dict)
    Fornecedor(window, "Fornecedor:", inputs_dict)
    Data(window, "Data:", inputs_dict)
    Competencia(window, "Competência:", inputs_dict)
    Valor(window, "Valor:", inputs_dict)
    Ano(window, "Ano:", inputs_dict)
    Conta2(window, "Conta2:", inputs_dict)
    Obs(window, "Observação:", inputs_dict)



# Function to retrieve values from the input fields
def get_values():
    # Retrieve values from the global dictionary
    for key, entry in inputs_dict.items():
        print(f"{key}: {entry.get()}")

# Function to submit the values when button is pressed
def Submit():
    get_values()

# Add submit button
submit_button = tk.Button(window, text="Enviar", command=Submit)
submit_button.pack(pady=20)

# Call the input functions to create all the fields
inputs()

# Run the application
window.mainloop()
