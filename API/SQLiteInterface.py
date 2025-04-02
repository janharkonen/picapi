import os

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, '..', 'Database', 'PicMetadata.db')
import sqlite3

class SQLiteInterface:
    def __init__(self):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS PIC_METADATA (
                uuid TEXT PRIMARY KEY,
                filename TEXT NOT NULL,
                upload_date DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            '''
        )
        self.conn.commit()
    
    def save(self, uuid: str, filename: str):
        self.cursor.execute(
            '''
            INSERT INTO PIC_METADATA (uuid, filename)
            VALUES (?, ?)
            ''',
            (uuid, filename)
        )
        self.conn.commit()