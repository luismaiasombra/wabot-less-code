import openpyxl
data_list = ["Código", "Nome", "Contatos", "Nível", "Situação", "Débito", "Oportunidade", "Total de Pontos no Período"]



def load_excel_sheet(file_name):
    try:
        # Open the Excel file
        workbook = openpyxl.load_workbook(file_name)

        # Select the first worksheet
        sheet = workbook['CAMPOS UTILIZADOS']

        # Initialize a list to store the data
        data = []

        # Start reading the sheet from the second row (index 2)
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(list(row))

        return data

    except Exception as e:
        print(f"Error loading the Excel sheet: {str(e)}")
        return None

# Example usage

