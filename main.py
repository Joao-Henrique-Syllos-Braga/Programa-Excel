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
from functions.mes import Mes

from create import create_excel

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
    Fc(window, "FC:", inputs_dict)
    Conta(window, "Conta:", inputs_dict)
    Descri(window, "Descrição:", inputs_dict)
    Fornecedor(window, "Fornecedor:", inputs_dict)
    Data(window, "Data:", inputs_dict)
    Competencia(window, "Competência:", inputs_dict)
    Valor(window, "Valor:", inputs_dict)
    Mes(window, "Mes:", inputs_dict)
    Ano(window, "Ano:", inputs_dict)
    Conta2(window, "Conta2:", inputs_dict)
    Obs(window, "Observação:", inputs_dict)


data = [
    ["CLASSE", "FC", "CONTA", "DESCRIÇÃO", "FORNECEDOR", "DATA", "COMPETÊNCIA", "VALOR", "MES", "ANO", "CONTA2", "OBS"]
]

# Function to retrieve values from the input fields and reset them
def get_values():
    variables = {}  # Dictionary to store variable values
    for key, entry in inputs_dict.items():
        variables[key] = entry.get()  # Get the value of each input field

    values_list = []  # Rename `list` to avoid conflict with built-in `list()` function

    # Print each variable for demonstration
    for var_name, value in variables.items():  # Get the values of inputs EX: "Class" : "information"
        # Verify if the value is ""
        if value == "":
            # Put the value ###### if the value "" -> obs, conta2
            values_list.append("######")
        elif var_name == "Competência:" or var_name == "Data:":
            print("1 passed")
            formated = value.replace("/", "")  # Remove '/' characters from the date

            # Convert the string into a list of characters
            charList = list(formated)

            # Function to format the date
            def current(charList):
                n = 0
                p = ""
                for x in charList:
                    if n == 2 or n == 4:  # Insert "/" at positions 2 and 4
                        p += "/"
                        p += x
                        n += 1
                    else:
                        p += x
                        n += 1
                return p

            formatted_date = current(charList)  # Call the function to format the date
            values_list.append(formatted_date)

        else:
            # Put the values in data at list and append on data          
            values_list.append(value)

        print(f"{var_name}: {value}")  # Print the values

    data.append(values_list)

    # Clear all input fields after retrieving the values
    for entry in inputs_dict.values():
        entry.delete(0, tk.END)  # Reset each input field

    return variables

# Call the input functions to create all the fields
inputs()

# Add submit button
submit_button = tk.Button(window, text="Enviar", command=get_values)
submit_button.pack(pady=20)

# Add create excel button
create = tk.Button(window, text="CRIAR EXCEL", command=lambda: create_excel(data=data, fileName="Listão.xlsx", inf=True))
create.pack(pady=20)

# Run the application
window.mainloop()
