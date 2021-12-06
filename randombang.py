import random
from startbang import *
from caractere import *


carte = ["Hors-la-loi", "Renégat", "Shérif", "Hors-la-loi"]

1
def main():
    debutgame(carte)
    randoms(debutgame)
    perso()
    
   

def randoms(debutgame):

    random.shuffle(carte) # Mélange les cartes
    
    print("\n")
    print("Les rôles qui pourrez-vous être attribué :")
    print(carte) # Affiche la liste mélanger
    print("\n")

    SelectRole = carte.pop() # Récupère et supprime le dernier élément de la liste
    print('Voici ton rôle :', SelectRole)

    desc(SelectRole)
    

def desc(SelectRole):


    # Aide pour connaître les rôles
    if SelectRole == "Hors-la-loi":
        print("Les Hors-la-loi gagnent la partie dès qu'ils ont éliminé le Shérif. En fonction du nombre de joueurs, il y a 2 ou 3 Hors-la-loi.\n")
    
    if SelectRole == "Shérif":
        print("Tu incarne le shérif est tu es le seul à dire ton rôle. Ton objectif est d'éliminer le(s) renégat(s) et les Hors-la-loi.\n")

    if SelectRole == "Renégat":
        print("Le Renégat doit supprimer les Hors-la-loi et Adjoint(s), et ensuite le Shérif, mais seulement en dernier, sinon ce sont les Hors-la-loi qui gagnent.\n")

    if SelectRole == "Adjoint":
        print("Les joueurs jouant les Adjoints gardent leur rôle secret mais doivent néanmoins veiller à ce que le Shérif survive. En fonction du nombre de joueurs, il y a 0, 1 ou 2 Adjoints.\n")

     
# def caractere(perso):
   # print("Maintenant que tout les rôles sont donner voici 4 personnages choisi en 1 :\n")

main()