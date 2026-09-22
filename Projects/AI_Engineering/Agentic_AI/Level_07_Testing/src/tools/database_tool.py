from langchain_core.tools import tool 
from database.connection import get_connection

@tool
def get_documents() -> list:
    """
    Get a list of documents from the database.
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM documents")
    documents= cursor.fetchall()
    cursor.close()
    connection.close()
    return documents
    
