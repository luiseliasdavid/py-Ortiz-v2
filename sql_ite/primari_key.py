import sqlite3

connexion = sqlite3.connect("ejemplo.db")
cursor = connexion.cursor()

#EL ID SERA INCREMENTAL
# EL DNI NO PODRA REPETIRSE
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dni VARCHAR(9) UNIQUE, 
    nombre VARCHAR(100),
    edad INTEGER,
    email VARCHAR(100)
    )
""")
usuarios = [
     ('A65456465','mario',51,'marios@example.com'),
     ('ss65456465','mercedes',45,'mercedez@ejemplo.com'),
     ('65456bh465','juan',19,'juan@ejemplo.com'),
     ('65d456465','hector',33,'hector@examople.com')
 ]

#AL CULOCAR NULL LA COLUMNA ID SE ASIGNARA AUTOMATICAMENTE UN ID UNICO
cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?,?)",usuarios)

# cursor.execute("INSERT INTO usuarios VALUES ('A654256465','mario',51,'marios@example.com')")
connexion.commit()

cursor.execute("SELECT * FROM usuarios")
all_usuarios= cursor.fetchall()
print(all_usuarios)

connexion.close()