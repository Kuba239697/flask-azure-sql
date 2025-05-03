from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Konfigurace připojení k Azure SQL databázi
server = 'server239697.database.windows.net'
database = 'Databaze_2'
username = 'skola@239697@server239697'
password = 'adnim_239697'
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'

def get_db_connection():
    conn = pyodbc.connect(connection_string)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM your_table')
    rows = cursor.fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

if __name__ == '__main__':
    app.run(debug=True)
