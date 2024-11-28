import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="delta_metadata",
        user="admin",
        password="admin123",
        host="postgres-service",
        port=5432
    )
