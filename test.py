import sqlite3

connexion = sqlite3.connect('OnlineStore2.db')
cursor = connexion.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    print(f"Contenu de la table '{table_name}':")
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print()


# Afficher les résultats
connexion.close()
