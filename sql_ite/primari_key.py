import sqlite3

connexion = sqlite3.connect("ejemplo.db")
cursor = connexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
    dni VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(100),
    edad INTEGER,
    email VARCHAR(100)
    )
""")
# usuarios = [
#     ('A65456465','mario',51,'marios@example.com'),
#     ('ss65456465','mercedes',45,'mercedez@ejemplo.com'),
#     ('65456bh465','juan',19,'juan@ejemplo.com'),
#     ('65d456465','hector',33,'hector@examople.com')
# ]
# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)",usuarios)

cursor.execute("INSERT INTO usuarios VALUES ('A654256465','mario',51,'marios@example.com')")

connexion.commit()
connexion.close()