import sqlite3

connexion = sqlite3.connect("ejemplo.db")
cursor = connexion.cursor()


connexion.commit()
connexion.close()