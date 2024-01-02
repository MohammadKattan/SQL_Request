from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run(debug=True,port=8080)

