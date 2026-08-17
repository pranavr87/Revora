import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]
DATABASE_PATH = BASE_DIR / "database" / "vehicle_fault_FINAL.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn