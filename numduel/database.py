import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="numduel",
        user="postgres",
        password="1234",
        port="5432"
    )

def get_cursor():
    connection = get_connection()
    cursor = connection.cursor()

    return connection, cursor