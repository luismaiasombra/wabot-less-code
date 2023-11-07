import sqlite3
data_list = ["Código", "Nome", "Contatos", "Nível", "Situação", "Débito", "Oportunidade", "Total de Pontos no Período"]

import sqlite3
#Este aqui é o histórico
# Connect to the SQLite database (or create it if it doesn't exist)
def create_history():
    conn = sqlite3.connect("database/history.db")

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
        points INTEGER,
        event_type TEXT
    );
    """

    # Execute the table creation query
    cursor.execute(create_table_query)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    return 'Success'


