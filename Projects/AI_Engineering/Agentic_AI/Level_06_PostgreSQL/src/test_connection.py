from database.connection import get_connection

connection=get_connection()

print("connexion with database is succeful!")

connection.close()