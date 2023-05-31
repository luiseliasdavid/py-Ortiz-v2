import sqlite3

connexion = sqlite3.connect("ejemplo.db")

cursor = connexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100)
    )
""")

cursor.execute("""INSERT INTO usuarios VALUES
     (
     'hector',
     27,
     'hector@ejemplo.com'
     )
""")

#cursor.execute("SELECT * FROM usuarios")
#usuario = cursor.fetchone()
#print(usuario)

usuarios= [
    ('Marios',51,'mario@ejemplo.com')
]



connexion.commit()

connexion.close()