# mysql_dao.py
import mysql.connector
from mysql.connector import Error
from models import Produit, Client

# Fonction pour obtenir la connexion
def get_connexion():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=3307,                # port de ton MySQL
            user="root",
            password="",  # remplace par ton vrai mot de passe
            database="boutique"
        )
        return conn
    except Error as err:
        print("Erreur de connexion :", err)
        return None

# ------------------ PRODUIT ------------------

def ajouter_produit(produit):
    conn = get_connexion()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO produit (nom, prix) VALUES (%s, %s)",
            (produit.nom, produit.prix)
        )
        conn.commit()
        print("Produit ajouté avec succès.")
    except Error as err:
        print("Erreur lors de l'ajout du produit :", err)
    finally:
        conn.close()

def lister_produits():
    conn = get_connexion()
    if not conn:
        return []
    produits = []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nom, prix FROM produit")
        rows = cursor.fetchall()
        for row in rows:
            produits.append(Produit(row[0], row[1], row[2]))
    except Error as err:
        print("Erreur lors de la lecture des produits :", err)
    finally:
        conn.close()
    return produits


def modifier_prix_produit(produit_id, nouveau_prix):
    conn = get_connexion()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE produit SET prix=%s WHERE id=%s",
            (nouveau_prix, produit_id)
        )
        conn.commit()
        print("Prix du produit mis à jour.")
    except Error as err:
        print("Erreur lors de la modification du produit :", err)
    finally:
        conn.close()

# ------------------ CLIENT ------------------

def ajouter_client(client):
    conn = get_connexion()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO client (nom, email) VALUES (%s, %s)",
            (client.nom, client.email)
        )
        conn.commit()
        print("Client ajouté avec succès.")
    except Error as err:
        print("Erreur lors de l'ajout du client :", err)
    finally:
        conn.close()

def lister_clients():
    conn = get_connexion()
    if not conn:
        return []
    clients = []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nom, email FROM client")
        rows = cursor.fetchall()
        for row in rows:
            clients.append(Client(row[0], row[1], row[2]))
    except Error as err:
        print("Erreur lors de la lecture des clients :", err)
    finally:
        conn.close()
    return clients

def rechercher_client_par_email(email):
    conn = get_connexion()
    if not conn:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nom, email FROM client WHERE email=%s", (email,))
        row = cursor.fetchone()
        if row:
            return Client(row[0], row[1], row[2])
    except Error as err:
        print("Erreur lors de la recherche du client :", err)
    finally:
        conn.close()
    return None

