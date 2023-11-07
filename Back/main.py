import openpyxl
from classes.system import realizar_disparos
from database.create_history import create_history
from classes.consultant import Consultant,criar_consultores
from database.history import in_history,add_to_history
from classes.consultant import Consultant as Consultant
from database.create_history import create_history

from classes.sheet import load_excel_sheet

workbook=openpyxl.load_workbook('CAMPOS UTILIZADOS.xlsx')
worksheet = workbook['CAMPOS']
create_history()
criar_consultores(worksheet)
realizar_disparos()






 



