from database import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute("SELECT * FROM leaderboard")

rows = cursor.fetchall()

print(rows)

cursor.close()
connection.close()