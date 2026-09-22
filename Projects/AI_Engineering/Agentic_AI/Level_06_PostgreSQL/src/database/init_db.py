import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS documents (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT NOT NULL
    )
    """
)   
connection.commit()
cursor.close()
connection.close()
print("table document created successfully!")