import os

import sqlite3

class SQLiteInterface:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_dir = os.path.join('/app', 'app', 'storage', 'storage')
        os.makedirs(db_dir, exist_ok=True)
        self.db_path = os.path.join(db_dir, 'PicMetadata.db')
        
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS PIC_METADATA (
                uuid TEXT PRIMARY KEY,
                original_filename TEXT NOT NULL,
                upload_date DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            '''
        )
        self.conn.commit()
        self.conn.close()
    
    def save(self, unique_filename: str, original_filename: str):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''
            INSERT INTO PIC_METADATA (uuid, original_filename)
            VALUES (?, ?)
            ''',
            (unique_filename, original_filename)
        )
        self.conn.commit()
        self.conn.close()
    
    def delete(self, uuid: str):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''
            DELETE FROM PIC_METADATA
            WHERE uuid = ?
            ''',
            (uuid,)
        )
        self.conn.commit()
        self.conn.close()

    def get_metadata(self) -> list[dict]:
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''
            SELECT uuid, original_filename
            FROM PIC_METADATA
            '''
        )
        rows = self.cursor.fetchall()
        self.conn.close()
        
        metadata = [
            {
                'uuid': row[0],
                'original_filename': row[1],
            }
            for row in rows
        ]
        metadata.reverse()

        return metadata