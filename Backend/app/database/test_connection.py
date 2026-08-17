from app.database.connection import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM symptom_aliases
LIMIT 20
""")

rows = cursor.fetchall()

for row in rows:
    print(dict(row))

conn.close()