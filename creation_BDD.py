import sqlite3
def creation():
    connexion = sqlite3.connect('OnlineStore2.db') 

    cursor = connexion.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS clients(
            id_client INTEGER PRIMARY KEY AUTOINCREMENT, 
            nom TEXT,
            email TEXT, 
            adresse TEXT
        )
    ''')
    cursor.execute(''' CREATE TABLE IF NOT EXISTS commandes(
            id_commande INTEGER PRIMARY KEY AUTOINCREMENT,
            id_client INTEGER,
            date_commande DATE,
            montant_total FLOAT,
            FOREIGN KEY (id_client) REFERENCES clients(id_client)
        )
    ''')
    cursor.execute (''' CREATE TABLE IF NOT EXISTS produits(
            id_produit INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_produit text,
            prix FLOAT,
            stock INTEGER
        )
    ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS commandes_produits(
            id_commande INTEGER,
            id_produit INTEGER,
            quantite INTEGER,
            FOREIGN KEY(id_commande)REFERENCES commandes(id_commande),
            FOREIGN KEY(id_produit) REFERENCES produits(id_produit)
        )
    ''')

    connexion.commit()
    connexion.close()

