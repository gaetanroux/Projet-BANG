from random import *
import random

finalcaract = []

caract = ["Bart Cassidy pv:4 -- chaque fois qu’il perd un point de vie, il pioche immédiatement une carte ",
"Kit Carlson pv:4 -- durant la phase 1 de son tour, il regarde les trois premières cartes de la pioche, en choisit 2 qu’il garde et repose la troisième sur la pioche, face cachée.",
"Black Jack pv:4 -- durant la phase 1 de son tour, il doit montrer la seconde carte qu’il a piochée. Si c’est un Cœur ou un Carreau (comme dans le cas d’un « dégaine ! »), il tire une carte supplémentaire (sans la révéler).", 
"Lucky Duke pv:4 -- chaque fois qu’il doit « dégainer », il retourne les deux premières cartes de la pioche et choisit le résultat qu’il préfère. Il défausse ensuite les deux cartes.", 
"Calamity Janet pv:4 -- elle peut utiliser les cartes BANG ! comme des cartes Raté ! et vice-versa. Si elle joue un Raté ! à la place d’un BANG !, elle ne peut pas jouer d’autre carte BANG ! durant son tour (à moins d’avoir un Volcanic en jeu).",
"Paul Regret pv:3 -- on considère qu’il a un Mustang en jeu à tout moment : tous les autres joueurs doivent ajouter 1 à la distance qui les sépare de lui. S’il a un autre Mustang réel en jeu, il peut utiliser les deux, ce qui augmente la distance de 2 en tout.",
"El Gringo pv:3 -- chaque fois qu’il perd un point de vie à cause d’une carte jouée par un autre joueur, il tire une carte au hasard dans la main de ce dernier (une carte par point de vie). Si ce joueur n’a plus de cartes, dommage, il ne peut pas lui en prendre ! N’oubliez pas que les points vie perdus à cause de la dynamite ne sont pas considérés comme étant causés par un joueur",
"Pedro Ramirez pv:4 -- durant la phase 1 de son tour, il peut choisir de piocher la première carte de la défausse au lieu de la prendre dans la pioche. Il pioche sa seconde carte normalement, dans la pioche.",
"Jesse Jones pv:4 -- durant la phase 1 de son tour, il peut choisir soit de piocher la première carte de la pioche, soit de prendre 1 carte au hasard dans la main d’un autre joueur. Il pioche ensuite sa deuxième carte dans la pioche.", 
"Rose Doolan pv:4 -- on considère qu’elle a une Lunette en jeu à tout moment : la distance de tous les autres joueurs est réduite de 1 pour elle. Si elle a une autre Lunette réelle en jeu, elle peut utiliser les deux, ce qui réduit la distance de tous les autres joueurs de 2 en tout.",
"Jourdonnais pv:4 -- on considère qu’il a une Planque en jeu à tout moment. Il peut « dégainer ! » quand il est la cible d’un BANG !, et s’il tire un cœur, le tir l’a raté. S’il a une autre vraie carte Planque en jeu, il peut l’utiliser également, ce qui lui donne deux chances d’annuler un BANG ! avant d’avoir à jouer un Raté !",
"Sid Ketchum pv:4 --  à tout moment, il peut défausser 2 cartes de sa main pour regagner 1 point de vie. S’il le désire et si c’est possible, il peut utiliser cette caractéristique plusieurs fois d’affi lée. Mais souvenez-vous : il ne peut à aucun moment avoir plus de 4 points de vie.",
"Slab le flingueur pv:4 --  quand il joue une carte BANG ! contre un joueur, celui-ci doit dépenser 2 cartes Raté ! au lieu d’une pour l’annuler. L’effet de la Planque ne compte que pour une carte Raté !",
"Sam le vautour pv:4 -- dès qu’un personnage est éliminé de la partie, Sam prend toutes les cartes que ce joueur avait en main et en jeu, et il les ajoute à sa propre main.",
"Suzy Lafayette pv:4 -- dès qu’elle n’a plus aucune carte en main, elle prend une carte dans la pioche.",
"Willy le Kid pv:4-- il peut jouer autant de cartes BANG ! qu’il le désire pendant son tour.",]



def perso():

    random.shuffle(caract)

    # We ask that as long as there are more than 12 elements in the array you copy and delete one element and then put it in a second array.
    while (len(caract) > 12):
        selectrole = caract.pop()
        finalcaract.append(selectrole)
        
    print("Maintenant que tout les rôles sont donner voici 4 personnages choisi en 1 :\n")
    
    print(finalcaract)    

    startcaract = input(" Joueur 1 : Quel carte choissez-vous ?")
    selectrole = caract.pop() # Récupère et supprime le dernier élément de la liste

    random.shuffle(caract)

    while (len(caract) > 12):
        selectrole = caract.pop()
        finalcaract.append(selectrole)
    print("Maintenant que tout les rôles sont donner voici 4 personnages choisi en 1 :\n")
    print(finalcaract)
    startcaract = input(" Joueur 2 : Quel carte choissez-vous ?")
    selectrole = caract.pop() # Récupère et supprime le dernier élément de la liste
    
        
    print("Voici ton rôle :")

    if startcaract == "1":
        print(finalcaract[0])
    if startcaract == "2":
        print(finalcaract[1])
    if startcaract == "3":
        print(finalcaract[2])
    elif startcaract == "4":
        print(finalcaract[3])
    
    print("\n")
    print("La partie peut maintenant commencer")


