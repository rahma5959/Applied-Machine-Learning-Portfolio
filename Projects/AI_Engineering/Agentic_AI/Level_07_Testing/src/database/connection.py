import psycopg


def get_connection():
    connection = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="ai_agent",
        user="postgres",
        password="rahma"
    )

    return connection

