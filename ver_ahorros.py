import sqlite3


conn = sqlite3.connect("ahorros.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM ahorros")

datos = cursor.fetchall()

print("\n📊 HISTORIAL DE AHORROS\n")

for ahorro in datos:
    print(ahorro)

conn.close()