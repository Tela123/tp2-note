from abc import ABC, abstractmethod

class Affichable(ABC):
    @abstractmethod
    def afficher_details(self):
        pass

# Livre et Personne implémentent l'interface Affichable
Livre.afficher_details = Livre.afficher_details
Personne.afficher_details = Personne.afficher_details