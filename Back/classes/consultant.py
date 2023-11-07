import sqlite3
import openpyxl
data_list = ["Código", "Nome", "Contatos", "Nível", "Situação", "Débito", "Oportunidade", "Total de Pontos no Período"]
def criar_consultores(worksheet):
    for row in worksheet.iter_rows():
        if row[0].value is None:
            break
        consultant = Consultant(row)
class Consultant:
    consultants = []
    rewards = []
    LEVELS = [5500,2200,900,300]
    LEVEL_TITLES = {}
    LEVEL_TITLES[5500]="Diamante"
    LEVEL_TITLES[2200]="Ouro"
    LEVEL_TITLES[900]="Prata"
    LEVEL_TITLES[300]="Bronze"
    #def reward(self,LEVELS=LEVELS,rewarded=rewarded,LEVEL_TITLES=LEVEL_TITLES):
    
    def __init__(self, row):
        self.code = row[0].value
        self.name = row[1].value
        self.phone = row[2].value
        self.level = row[3].value
        self.status = row[4].value #current situation of the consultant
        self.debit_status = row[5].value
        self.perks =  row[6].value
        self.points = row[7].value
        Consultant.consultants.append(self)
    def upgradable(self,LEVELS=LEVELS):
        for goal in LEVELS:
            if self.points >= goal:
                self.level = goal
                return True
        return False
        

import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("database/consultants.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the table schema
create_table_query = """
CREATE TABLE IF NOT EXISTS history (
    code INTEGER,
    name TEXT,
    phone INTEGER,
    level TEXT,
    status TEXT,
    debit_status REAL,
    perks TEXT,
    points INTEGER
);
"""

# Execute the table creation query
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()









