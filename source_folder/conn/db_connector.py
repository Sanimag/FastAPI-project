import psycopg2

conn = psycopg2.connect(dbname = 'sales_db', user = 'san', password = 'san123', host = 'localhost')

cursor = conn.cursor()

cursor.execute("SELECT * FROM worker")

print(cursor.fetchall())

cursor.close()
conn.close()

