from flask import Flask, render_template
from datetime import datetime, timedelta
import sqlite3

app = Flask(__name__)

# Fonction pour obtenir les noms des tables
def obtenir_noms_tables():
    conn = sqlite3.connect('OnlineStore2.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return tables

# Fonction pour récupérer les données des tables
def obtenir_donnees(table_name):
    conn = sqlite3.connect('OnlineStore2.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/')
def afficher_tables():
    tables = obtenir_noms_tables()
    return render_template('tables.html', tables=tables)

# Route pour afficher les clients
@app.route('/table/clients')
def afficher_clients():
    donnees_clients = obtenir_donnees('clients')
    return render_template('clients.html', titre='Clients', donnees=donnees_clients)

# Route pour afficher les commandes
@app.route('/table/commandes')
def afficher_commandes():
    donnees_commandes = obtenir_donnees('commandes')
    return render_template('commandes.html', titre='Commandes', donnees=donnees_commandes)

# Route pour afficher les produits
@app.route('/table/produits')
def afficher_produits():
    donnees_produits = obtenir_donnees('produits')
    return render_template('produits.html', titre='Produits', donnees=donnees_produits)

# Route pour afficher les commandes
@app.route('/table/commandes_produits')
def afficher_commandes_produits():
    donnees_commandes_produits = obtenir_donnees('commandes_produits')
    return render_template('commandes_produits.html', titre='Commandes_produits', donnees=donnees_commandes_produits)


@app.route('/commandes/<int:id_client>', methods=['GET'])
def afficher_commandes_client(id_client):
    connexion = sqlite3.connect('Onlinestore2.db')
    cursor = connexion.cursor()
    # Récupérer les commandes du client spécifique depuis la base de données
    cursor.execute("""
    SELECT c.id_commande, c.id_client, c.date_commande, c.montant_total, cl.nom
    FROM commandes AS c
    INNER JOIN clients AS cl ON c.id_client = cl.id_client
    WHERE c.id_client = ?
""", (id_client,))

    commandes = cursor.fetchall()

    connexion.close()

    return render_template('commandes_client.html', titre="Commandes du Client", donnees=commandes)


@app.route('/produits_commandes/<int:id_client>', methods=['GET'])
def afficher_produits_commandes(id_client):
    connexion = sqlite3.connect('OnlineStore2.db')
    cursor = connexion.cursor()
    # Récupérer les détails des produits commandés par le client spécifique
    cursor.execute("""
        SELECT p.id_produit, p.nom_produit, p.prix, cp.quantite
        FROM produits AS p
        JOIN commandes_produits AS cp ON p.id_produit = cp.id_produit
        JOIN commandes AS c ON cp.id_commande = c.id_commande
        WHERE c.id_client = ?
    """, (id_client,))
    produits_commandes = cursor.fetchall()
    connexion.close()
    return render_template('produits_commandes.html', titre="Produits commandés", produits_commandes=produits_commandes)

@app.route('/commandes_ce_jour/')
def commande_ce_jour():
    connexion = sqlite3.connect('OnlineStore2.db')
    cursor = connexion.cursor()
    date_24h_avant = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    cursor.execute("""
        SELECT c.id_client, c.nom, SUM(p.prix * cp.quantite) AS montant_total_achats
        FROM clients AS c
        JOIN commandes AS cmd ON c.id_client = cmd.id_client
        JOIN commandes_produits AS cp ON cmd.id_commande = cp.id_commande
        JOIN produits AS p ON cp.id_produit = p.id_produit
        WHERE cmd.date_commande >= ?
        GROUP BY c.id_client, c.nom
    """, (date_24h_avant,))
    commandes_ce_jour = cursor.fetchall()
    connexion.close()
    return render_template('commandes_ce_jour.html', titre="Commandes du Jour", donnees=commandes_ce_jour)

@app.route('/client_depense/<int:id_client>', methods=['GET'])
def client_depense(id_client):
    connexion = sqlite3.connect('OnlineStore2.db')
    cursor = connexion.cursor()
    cursor.execute("""
        SELECT c.id_client, c.nom, SUM(p.prix * cp.quantite) AS montant_total_depense
        FROM clients AS c
        JOIN commandes AS cmd ON c.id_client = cmd.id_client
        JOIN commandes_produits AS cp ON cmd.id_commande = cp.id_commande
        JOIN produits AS p ON cp.id_produit = p.id_produit
        WHERE c.id_client = ?
        GROUP BY c.id_client, c.nom;
    """, (id_client,))
    client_depense = cursor.fetchall()
    print(len(client_depense))
    connexion.close()
    return render_template('commandes_ce_jour.html', titre="Montant total dépensé", donnees=client_depense)


if __name__ == '__main__':
    app.run(debug=True,port=8080)

