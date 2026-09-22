import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import get_connection
from langchain_core.tools import tool 

@tool
def get_document() -> list:
    """
    Get all documents from the database.
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM documents")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows