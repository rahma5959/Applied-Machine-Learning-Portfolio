import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.connection import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute("SELECT * FROM documents")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()
