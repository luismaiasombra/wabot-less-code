
import sqlite3
def in_history(code, name,event_type, level):
    # Connect to your SQLite database
    conn = sqlite3.connect('database/history.db')
    cursor = conn.cursor()
    query = "SELECT * FROM history WHERE code=? AND name=? AND event_type=? AND level=?"

    cursor.execute(query, (code, name, event_type, level))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False
    conn.close()
def add_to_history(row):
    code, name, phone, level, status, debit_status, perks, points = row.code, row.name, row.phone, row.level, row.status, row.debit_status, row.perks,row.points
    event_type = 'DISPARO'
    conn = sqlite3.connect('database/history.db')
    cursor = conn.cursor()
    query = "INSERT INTO history (code, name, event_type, level) VALUES (?, ?, ?, ?)"
    # Execute the INSERT statement with the provided values
    cursor.execute(query, (code, name, event_type, level))
    conn.commit()
    conn.close()
    #code, name, event_type, level

