# main.py
from models import Produit, Client
import mysql_dao as dao  # utilise sqlite_dao si tu veux SQLite

def menu():
    print("\nMenu:")
    print("1. Ajouter produit")
    print("2. Lister produits")
    print("3. Modifier prix d'un produit")
    print("4. Ajouter client")
    print("5. Lister clients")
    print("6. Rechercher client par email")
    print("0. Quitter")

def main():
    while True:
        menu()
        choix = input("Votre choix: ")

        if choix == "1":
            nom = input("Nom du produit: ")
            try:
                prix = float(input("Prix: "))
            except ValueError:
                print("Prix invalide.")
                continue
            dao.ajouter_produit(Produit(None, nom, prix))

        elif choix == "2":
            produits = dao.lister_produits()
            if not produits:
                print("Aucun produit trouvé.")
            for p in produits:
                print(p)

        elif choix == "3":
            try:
                produit_id = int(input("ID du produit à modifier: "))
                nouveau_prix = float(input("Nouveau prix: "))
            except ValueError:
                print("Valeurs invalides.")
                continue
            dao.modifier_prix_produit(produit_id, nouveau_prix)

        elif choix == "4":
            nom = input("Nom du client: ")
            email = input("Email du client: ")
            dao.ajouter_client(Client(None, nom, email))

        elif choix == "5":
            clients = dao.lister_clients()
            if not clients:
                print("Aucun client trouvé.")
            for c in clients:
                print(c)

        elif choix == "6":
            email = input("Email du client à rechercher: ")
            client = dao.rechercher_client_par_email(email)
            if client:
                print(client)
            else:
                print("Client non trouvé.")

        elif choix == "0":
            print("Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
