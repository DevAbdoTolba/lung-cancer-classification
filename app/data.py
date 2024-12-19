# In app.py or a separate database module
import sqlite3

def init_db():
    conn = sqlite3.connect('data/logs.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            emotion TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_interaction(emotion):
    conn = sqlite3.connect('data/logs.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO interactions (emotion) VALUES (?)', (emotion,))
    conn.commit()
    conn.close()