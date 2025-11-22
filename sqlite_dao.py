# sqlite_dao.py
import sqlite3
from models import Produit, Client

def get_connexion():
    return sqlite3.connect("boutique.db")

# PRODUIT
def ajouter_produit(produit):
    conn = get_connexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produit (nom, prix) VALUES (?, ?)", (produit.nom, produit.prix))
    conn.commit()
    conn.close()
    print("Produit ajouté avec succès.")

def lister_produits():
    conn = get_connexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, prix FROM produit")
    produits = [Produit(row[0], row[1], row[2]) for row in cursor.fetchall()]
    conn.close()
    return produits

def modifier_prix_produit(produit_id, nouveau_prix):
    conn = get_connexion()
    cursor = conn.cursor()
    cursor.execute("UPDATE produit SET prix=? WHERE id=?", (nouveau_prix, produit_id))
    conn.commit()
    conn.close()
    print("Prix du produit mis à jour.")

# CLIENT
def ajouter_client(client):
    conn = get_connexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO client (nom, email) VALUES (?, ?)", (client.nom, client.email))
    conn.commit()
    conn.close()
    print("Client ajouté avec succès.")

def lister_clients():
    conn = get_connexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, email FROM client")
    clients = [Client(row[0], row[1], row[2]) for row in cursor.fetchall()]
    conn.close()
    return clients

def rechercher_client_par_email(email):
    conn = get_connexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nom, email FROM client WHERE email=?", (email,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Client(row[0], row[1], row[2])
    return None
