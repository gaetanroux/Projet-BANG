
        
def debutgame(carte):


    pseudo = []
    
    start = input("Combien de joueur êtes vous :")

    if int(start) < 4:
        print("Vous n'êtes pas assez pour lancer une partie (4 minimum).") 
        exit()



    if int(start) == 4:

        print("Vous êtes pile le nombre pour lancer une partie !\n")

        a = input('Entrez le prénom ou le surnom du joueur 1 :\n').split()
        pseudo = pseudo + a

        b = input("Entrez le prénom ou le surnom du joueur 2 :\n").split()
        pseudo = pseudo + b

        c = input("Entrez le prénom ou le surnom du joueur 3 :\n").split()
        pseudo = pseudo + c

        d = input("Entrez le prénom ou le surnom du joueur 4 :\n").split()
        pseudo = pseudo + d


    if int(start) == 5:
        carte.append("Adjoint")
        print("Vous pouvez lancer une partie, une carte supplémentaire s'ajoute.\n")
        a = input("Entrez le prénom ou le surnom du joueur 1 :\n").split()
        pseudo = pseudo + a

        b = input("Entrez le prénom ou le surnom du joueur 2 :\n").split()
        pseudo = pseudo + b

        c = input("Entrez le prénom ou le surnom du joueur 3 :\n").split()
        pseudo = pseudo + c

        d = input("Entrez le prénom ou le surnom du joueur 4 :\n").split()
        pseudo = pseudo + d

        e = input("Entrez le prénom ou le surnom du joueur 5 :\n").split()
        pseudo = pseudo + e

    if int(start) == 6:
        carte.append("Hors-la-loi")
        carte.append("Adjoint")
        print("Vous pouvez lancer une partie, deux cartes supplémentaires s'ajoute.\n")
        a = input("Entrez le prénom ou le surnom du joueur 1 :\n").split()
        pseudo = pseudo + a

        b = input("Entrez le prénom ou le surnom du joueur 2 :\n").split()
        pseudo = pseudo + b

        c = input("Entrez le prénom ou le surnom du joueur 3 :\n").split()
        pseudo = pseudo + c

        d = input("Entrez le prénom ou le surnom du joueur 4 :\n").split()
        pseudo = pseudo + d

        e = input("Entrez le prénom ou le surnom du joueur 5 :\n").split()
        pseudo = pseudo + e

        f = input("Entrez le prénom ou le surnom du joueur 6 :\n").split()
        pseudo = pseudo + f

    if int(start) == 7:
        carte.append("Adjoint")
        carte.append("Hors-la-loi")
        carte.append("Adjoint")
        print("Vous pouvez lancer une partie, trois cartes supplémentaires s'ajoute.\n")
      
        a = input("Entrez le prénom ou le surnom du joueur 1 :\n").split()
        pseudo = pseudo + a

        b = input("Entrez le prénom ou le surnom du joueur 2 :\n").split()
        pseudo = pseudo + b

        c = input("Entrez le prénom ou le surnom du joueur 3 :\n").split()
        pseudo = pseudo + c

        d = input("Entrez le prénom ou le surnom du joueur 4 :\n").split()
        pseudo = pseudo + d

        e = input("Entrez le prénom ou le surnom du joueur 5 :\n").split()
        pseudo = pseudo + e

        f = input("Entrez le prénom ou le surnom du joueur 6 :\n").split()
        pseudo = pseudo + f

        g = input("Entrez le prénom ou le surnom du joueur 7 :\n").split()
        pseudo = pseudo + g

print("La partie commence...\n")
