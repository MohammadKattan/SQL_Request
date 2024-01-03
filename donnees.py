import sqlite3

# Établir la connexion à la base de données
def donnees() : 
    connexion = sqlite3.connect('OnlineStore2.db')
    cursor = connexion.cursor()

    # Insérer des données dans la table 'clients'
    clients_data = [
        ('Client A', 'clientA@example.com', 'Adresse A'),
        ('Client B', 'clientB@example.com', 'Adresse B'),
        ('Client C', 'clientC@example.com', 'Adresse C'),
        ('Client D', 'clientD@example.com', 'Adresse D'),
        ('Client E', 'clientE@example.com', 'Adresse E'),
        ('Client F', 'clientF@example.com', 'Adresse F')
    ]
    cursor.executemany("INSERT INTO clients (nom, email, adresse) VALUES ( ?, ?, ?)", clients_data)

    # Insérer des données dans la table 'commandes'
    commandes_data = [
        ( 1, '2023-10-15', 50.00),
        ( 2, '2023-11-20', 75.50),
        ( 1, '2023-12-05', 30.25),
        ( 3, '2023-12-10', 100.00),
        ( 4, '2024-01-03', 75.50),
        ( 5, '2024-01-03', 30.25),
        ( 1, '2024-01-03', 100.00)
    ]
    cursor.executemany("INSERT INTO commandes (id_client, date_commande, montant_total)VALUES ( ?, ?, ?)", commandes_data)

    # Insérer des données dans la table 'produits'
    produits_data = [
        ( 'Produit 1', 10.00, 50),
        ( 'Produit 2', 15.50, 30),
        ( 'Produit 3', 5.75, 75),
        ( 'Produit 4', 20.00, 20)
    ]
    cursor.executemany("INSERT INTO produits (nom_produit, prix, stock) VALUES ( ?, ?, ?)", produits_data)

    # Insérer des données dans la table 'commandes_produits'
    commandes_produits_data = [
        (1, 1, 2),
        (1, 3, 1),
        (2, 2, 3),
        (3, 4, 2),
        (4, 1, 4),
        (5, 3, 1),
        (5, 2, 3),
        (6, 4, 2),
        (6, 1, 4),
        (7, 3, 1)
    ]
    cursor.executemany("INSERT INTO commandes_produits (id_commande, id_produit, quantite)VALUES (?, ?, ?)", commandes_produits_data)

    # Valider les modifications et fermer la connexion à la base de données
    connexion.commit()
    connexion.close()
