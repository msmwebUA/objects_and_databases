import sqlite3 as db
from pathlib import Path

DB_FILEPATH = Path('./dev.db')

DB_CONN = db.connect(DB_FILEPATH)
DB_CONN.row_factory = db.Row