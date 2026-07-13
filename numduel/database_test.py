import psycopg2


#connect python to PostgreSQL database 
connection = psycopg2.connect(
    host = "localhost",
    database = "numduel",
    user = "postgres",
    password = "1234",
    port = "5432"
)

#create cursor 
cursor = connection.cursor()

# Execute SQL query
cursor.execute("SELECT * FROM leaderboard")

#Fetch result 
rows = cursor.fetchall()

print(rows)

#Cleanup
cursor.close()
connection.close()