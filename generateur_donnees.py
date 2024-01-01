import sqlite3
from faker import Faker
import random


def generateur():
    connexion = sqlite3.connect('OnlineStore.db')
    cursor = connexion.cursor()
    fake = Faker()
    # Générer 20 clients aléatoires
    for _ in range(20): 
        nom = fake.name()
        email = fake.email()
        adresse = fake.address()
        cursor.execute("INSERT INTO clients (nom,email,adresse)VALUES(?,?,?)",(nom,email,adresse))
    # Générer 20 commandes fictives avec des clients aléatoires
    for _ in range(30):  
        id_client = random.randint(1, 20)
        date_commande = fake.date_time_this_year()
        montant_total = round(random.uniform(10, 1000), 2)
        cursor.execute("INSERT INTO commandes (id_client, date_commande, montant_total) VALUES (?, ?, ?)",
                        (id_client, date_commande, montant_total))
        

    donnees_produits = [
        ("Chaussures de sport", 59.99, 100),
        ("Smartphone", 499.99, 50),
        ("Sac à dos", 39.95, 75),
        ("Casque audio", 129.50, 30),
        ("Montre connectée", 199.00, 60),
        ("Laptop", 899.00, 25),
        ("Bouteille d'eau", 1.99, 200),
        ("Livre", 19.99, 80),
        ("Téléviseur 4K", 1499.99, 15),
        ("Cafetière", 79.50, 40),
        ("Enceinte Bluetooth", 69.99, 55),
        ("Souris sans fil", 29.95, 90),
        ("Clavier mécanique", 89.00, 70),
        ("Imprimante", 249.50, 20),
        ("Tapis de yoga", 29.99, 120),
        ("Parapluie", 14.50, 150),
        ("Jeux de société", 35.00, 45),
        ("Batterie externe", 49.99, 65),
        ("Plantes d'intérieur", 9.99, 180),
        ("Chargeur USB", 12.95, 100)
    ]
    for produit in donnees_produits:
        cursor.execute("INSERT INTO produits (nom_produit, prix, stock) VALUES (?, ?, ?)", produit)

    for _ in range(15): 
        id_commande = random.randint(1,29)
        id_produit = random.randint(1,20)
        quantite = random.randint(1,5)
        cursor.execute("INSERT INTO commandes_prodiuts(id_commande,id_produit,quantite)VALUES(?,?,?)",(id_commande,id_produit,quantite))
    connexion.commit()
    connexion.close()