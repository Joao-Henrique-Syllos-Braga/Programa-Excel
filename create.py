
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font

inf = False

def create_excel(data, fileName, inf):
    # Creating a new workbook
    wb = Workbook()

    # Accessing the active sheet
    sheet = wb.active
    sheet.title = "Listão"

    # Defining the background color and font color styles
    fill = PatternFill(start_color="1f1f1f", end_color="1f1f1f", fill_type="solid")
    font = Font(color="ffffff")

    # Adding the first row with styles
    first_row = data[0]  # First row of data
    sheet.append(first_row)  # Adding the data to the sheet
    for cell in sheet[1]:  # For each cell in the first row
        cell.fill = fill  # Applying the background color
        cell.font = font   # Applying the font color

    # Adding the rest of the data rows
    for row in data[1:]:  # Iterating over the remaining data
        if row == " ":  # Check for empty rows
            sheet.append("######")
        else:
            sheet.append(row)

    # Saving the file
    if inf == True:
        wb.save(fileName)