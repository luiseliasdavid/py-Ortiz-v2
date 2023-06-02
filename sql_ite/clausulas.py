import sqlite3

connexion = sqlite3.connect("ejemplo.db")
cursor = connexion.cursor()

cursor.execute("DELETE FROM usuarios WHERE dni='65d456465'")


connexion.commit()
connexion.close()