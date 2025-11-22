

class Produit:
    def __init__(self, id, nom, prix):
        self.id = id
        self.nom = nom
        self.prix = prix

    def __str__(self):
        return f"Produit[{self.id}]: {self.nom}, Prix: {self.prix}€"


class Client:
    def __init__(self, id, nom, email):
        self.id = id
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"Client[{self.id}]: {self.nom}, Email: {self.email}"
