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

# Function to call all input functions
def inputs():
    Classe(window, "Classe:")
    Conta(window, "Conta:")
    Fc(window, "FC:")
    Descri(window, "Descrição:")
    Fornecedor(window, "Fornecedor:")
    Data(window, "Data:")
    Competencia(window, "Competência:")
    Valor(window, "Valor:")
    Ano(window, "Ano:")
    Conta2(window, "Conta2:")
    Obs(window, "Observação:")

# Call the input function
inputs()

# Run the application
window.mainloop()
