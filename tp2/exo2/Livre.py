from datetime import datetime, timedelta

# Classe Livre
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True

    def afficher_details(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        print(f"Livre: {self.titre}, Auteur: {self.auteur}, Année: {self.annee}, Statut: {statut}")

# Classe Personne
class Personne:
    def __init__(self, nom, prenom, nummembre):
        self.nom = nom
        self.prenom = prenom
        self.nummembre = nummembre

    def afficher_details(self):
        print(f"Nom: {self.nom}, Prénom: {self.prenom}, Numéro de membre: {self.nummembre}")

# Classe dérivée Emprunt
class Emprunt:
    def __init__(self, livre, personne, date_emprunt=None, duree=14):
        self.livre = livre
        self.personne = personne
        self.date_emprunt = date_emprunt if date_emprunt else datetime.now()
        self.date_retour_prevue = self.date_emprunt + timedelta(days=duree)

from abc import ABC, abstractmethod

class Affichable(ABC):
    @abstractmethod
    def afficher_details(self):
        pass

# Livre et Personne implémentent l'interface Affichable
Livre.afficher_details = Livre.afficher_details
Personne.afficher_details = Personne.afficher_details

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.emprunts = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Livre ajouté : {livre.titre}")

    def emprunter_livre(self, titre, personne):
        for livre in self.livres:
            if livre.titre == titre and livre.disponible:
                livre.disponible = False
                emprunt = Emprunt(livre, personne)
                self.emprunts.append(emprunt)
                print(f"Livre emprunté : {titre} par {personne.nom} {personne.prenom}")
                return
        print(f"Le livre '{titre}' n'est pas disponible.")

    def retourner_livre(self, titre):
        for emprunt in self.emprunts:
            if emprunt.livre.titre == titre:
                emprunt.livre.disponible = True
                self.emprunts.remove(emprunt)
                print(f"Livre retourné : {titre}")
                return
        print(f"Le livre '{titre}' n'est pas trouvé dans les emprunts.")

    def afficher_livres_empruntes(self):
        if not self.emprunts:
            print("Aucun livre emprunté.")
        else:
            for emprunt in self.emprunts:
                print(f"Livre emprunté : {emprunt.livre.titre}, Par : {emprunt.personne.nom} {emprunt.personne.prenom}, Date retour prévue : {emprunt.date_retour_prevue.strftime('%Y-%m-%d')}")

# Test du système
if __name__ == "__main__":
    biblio = Bibliotheque()

    # Ajouter des livres
    livre1 = Livre("1984", "George Orwell", 1949)
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)

    # Ajouter une personne
    personne1 = Personne("Dupont", "Jean", 101)

    # Emprunter un livre
    biblio.emprunter_livre("1984", personne1)

    # Afficher les livres empruntés
    biblio.afficher_livres_empruntes()

    # Retourner un livre
    biblio.retourner_livre("1984")

    # Afficher les livres empruntés après le retour
    biblio.afficher_livres_empruntes()