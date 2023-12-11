#coding: utf-8


#Partie A

def init(n):
    """Recoit en argument un entier n (le nombre de disques), et qui renvoie la liste représentant la configuration initiale du plateau"""
    discs = []
    for i in range (n, 0, -1):
        discs.append(i)

    return [discs, [], []]


def nbDisques(plateau, numtour):
    """Renvoie le nombre de disques sur la tour indiquée"""
    if 0 < numtour > 2:
        return f"ERROR : Numtour must be between 0 and 2"
    return len(plateau[numtour])


def disqueSup(plateau, numtour):
    """Renvoie le numéro du disque au sommet de la tour indiquée"""
    if not plateau[numtour] or len(plateau[numtour]) == 0:
        return -1
    return plateau[numtour][len(plateau[numtour]) - 1]


def posDisque(plateau, numdisque):
    """Renvoie le numéro de la tour sur laquelle se trouve un disque"""
    if numdisque in plateau[0]:
        return 0
    elif numdisque in plateau[1]:
        return 1
    elif numdisque in plateau[2]:
        return 2
    else:
        return -1


def posDisque_edited(plateau, numdisque):
    """Renvoie la position du disque dans le plateau (n-tour, n-position dans la tour)."""
    for i in plateau:
        for x in i:
            if numdisque == x:
                return plateau.index(i), i.index(x)    #retourne d'abord la n-tour, et ensuite la n-position dans la tour

def verifDepl(plateau, nt1, nt2):
    """Vérifie si le déplacement entre les tours nt1 et nt2 est valide."""
    taille=plateau[nt1-1][len(plateau[nt1-1])-1]
    if plateau[nt2-1]==[]:
        return True
    elif plateau[nt2-1][len(plateau[nt2-1])-1]>taille:
        return True
    else:
        return False

def verifVictoire(plateau,n):
    """Vérifie si la configuration actuelle du plateau est une victoire."""
    return plateau[2]==[i for i in range(n,0,-1)]




#Partie 2
import turtle
    
# Fonction pour dessiner le plateau avec trois tours
def dessinePlateau(n):
    """Dessine le plateau avec trois tours."""
    largeur_plateau = 40+30*n        
    hauteur_plateau = 20
    hauteur_tour = 20*n+30

    # Dessiner le plateau
   
    turtle.fillcolor("gray")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(largeur_plateau)
        turtle.left(90)
        turtle.forward(hauteur_plateau)
        turtle.left(90)
    turtle.end_fill()

    # Dessiner les tours
    for i in range(3):
        turtle.penup()
        x_tour = (largeur_plateau / 6) + i * (largeur_plateau / 3)
        y_tour = hauteur_plateau 
        turtle.goto(x_tour , y_tour)
        turtle.pendown()
        for i in range(2):
            turtle.forward(0)
            turtle.left(90)
            turtle.forward(hauteur_tour)
            turtle.left(90)

    turtle.hideturtle()



def dessineDisque(nd, plateau, n):
    """Trace un disque sur le plateau."""
    #Dimension plateau
    largeur_plateau = 40+30*n
    hauteur_plateau = 20
    hauteur_tour = 20*n+30
    #trouver emplacement du disque dans la liste
    PosD=[0,0]
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j]==nd:
                PosD=[i,j]
    #Tracer un disque
    longueur_disque = nd*10
    hauteur_disque = 20
    xdisque = (largeur_plateau / 6) + PosD[0] * (largeur_plateau / 3)
    ydisque = hauteur_plateau+hauteur_plateau*PosD[1]
    turtle.penup()
    turtle.goto(xdisque,ydisque)
    turtle.forward(longueur_disque/2)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(hauteur_disque)
    turtle.left(90)
    turtle.forward(longueur_disque)
    turtle.left(90)
    turtle.forward(hauteur_disque)
    turtle.left(90)

def effaceDisque(nd,plateau,n):
    """Efface un disque du plateau."""
    #Dimension plateau
    largeur_plateau = 40+30*n
    hauteur_plateau = 20
    hauteur_tour = 20*n+30
    #trouver emplacement du disque dans la liste
    PosD=[0,0]
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if plateau[i][j]==nd:
                PosD=[i,j]
    #Tracer un disque
    longueur_disque = nd*10
    hauteur_disque = 20
    xdisque = (largeur_plateau / 6) + PosD[0] * (largeur_plateau / 3)
    ydisque = hauteur_plateau+hauteur_plateau*PosD[1]
    
    turtle.pencolor("white")
    turtle.penup()
    turtle.goto(xdisque,ydisque+1)
    turtle.forward(longueur_disque/2)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(hauteur_disque-1)
    turtle.left(90)
    turtle.forward(longueur_disque)
    turtle.left(90)
    turtle.forward(hauteur_disque)
    turtle.left(90)
    turtle.pencolor("black")
    turtle.penup()
    turtle.goto(xdisque,ydisque)
    turtle.pendown()
    turtle.goto(xdisque,ydisque+22)


def dessineConfig(plateau,n):
    """Dessine la configuration actuelle du plateau."""
    for i in range(n):
        dessineDisque(i+1,plateau,n)

def effaceTout(plateau,n):
    """Efface tous les disques du plateau."""
    for i in range(n):
        effaceDisque(i+1,plateau,n)


  
#Partie C
import time
#Fonction qui initialise l'emplacement des disques de départs et d'arrivé
def lireCoords(plateau):
    """Lit les coordonnées (tour de départ, tour d'arrivée) fournies par l'utilisateur."""
    while True:
        # Demande le numéro de la tour de départ
        tour_depart = -3
        while tour_depart not in [-1,1,2,3] or len(plateau[tour_depart - 1]) == 0:
            tour_depart = int(input("Entrez le numéro de la tour de départ (1, 2, 3) : "))
            if tour_depart==-1:
                print("Vous avez choisis d'abandonner.")
                tour_arrivee=None
                tour_depart=None
                break
            elif tour_depart==-2:
                print("Vous avez annuler le dernier coup.")
                tour_arrivee=-2
                break
            elif tour_depart not in [1,2,3]:
                print("Le numéro de la tour doit être entre 1 et 3.")
            elif len(plateau[tour_depart - 1]) == 0:
                print("La tour de départ est vide. Choisissez une autre tour.")
        
        # Demande le numéro de la tour d'arrivée
        if tour_depart!=None and tour_depart!=-2:
            tour_arrivee = int()
            flag=True
            while flag:
                tour_arrivee = int(input("Entrez le numéro de la tour d'arrivée (1, 2, 3) : "))
                if tour_arrivee not in [1,2,3]:
                    print("Le numéro de la tour doit être entre 1 et 3.")
                elif len(plateau[tour_arrivee - 1]) > 0 and plateau[tour_arrivee - 1][-1] < plateau[tour_depart - 1][-1]:
                    print("Le disque sélectionné ne peut pas être placé sur cette tour. Choisissez une autre tour.")
                else:
                    if plateau[tour_arrivee-1]==[]:
                        flag = False
                    elif plateau[tour_arrivee - 1][-1] < plateau[tour_depart - 1][-1]:
                        flag = True
                    elif tour_arrivee in [1,2,3]:
                        flag = False
            tour_depart=tour_depart-1
            tour_arrivee=tour_arrivee-1
        return tour_depart , tour_arrivee


def jouerUnCoup(plateau,n):
    """Joue un coup en déplaçant un disque d'une tour à une autre."""
    tour_depart,tour_arrivee=lireCoords(plateau)
    if tour_depart ==None:
        plateau.clear()
    elif tour_depart==-2:
        return 1
    else:
        effaceDisque(plateau[tour_depart][-1],plateau,n)
        
        
        liste_temporaire=plateau[tour_arrivee][:]
        liste_temporaire.append(plateau[tour_depart][-1])
        plateau[tour_arrivee]=liste_temporaire[:]
        
        liste_temporaire.clear()
        
        liste_temporaire=plateau[tour_depart][:]
        liste_temporaire.pop()
        plateau[tour_depart]=liste_temporaire[:]
        dessineDisque(plateau[tour_arrivee][-1], plateau, n)
    
    return plateau


def boucleJeu(plateau,n,score):
    """Boucle principale du jeu."""
    temps_jeu=0
    start=time.time()
    nb_coup=0
    dessinePlateau(n)
    dessineConfig(plateau,n)
    flag=True
    continuer=True
    dico={}
    dico[0]=plateau[:]
    while flag and not verifVictoire(plateau,n) :
        coup=jouerUnCoup(plateau,n)
        if plateau==[]:
            flag=False
            print(f"Vous avez abandonner après {nb_coup} coups")
        elif coup==1:
            nb_coup=nb_coup-1
            tour_depart,tour_arrivee=dernierCoup(dico)
            
            
            effaceDisque(plateau[tour_arrivee][-1],plateau,n)
        
        
            liste_temporaire=plateau[tour_depart][:]
            liste_temporaire.append(plateau[tour_arrivee][-1])
            plateau[tour_depart]=liste_temporaire[:]
            
            liste_temporaire.clear()
            
            liste_temporaire=plateau[tour_arrivee][:]
            liste_temporaire.pop()
            plateau[tour_arrivee]=liste_temporaire[:]
            dessineDisque(plateau[tour_depart][-1], plateau, n)
            
            
            
        else:
            dico[nb_coup+1]=coup[:]
            nb_coup+=1
    if flag:
        print(f"Victoire en {nb_coup} coups")
        end=time.time()
        temps_jeu=end-start
        if input("Voullez vous enregistrer vôtre score? (o/n)")=="o":
            score=sauvScore(n,nb_coup,score,temps_jeu)



##Partie D

def dernierCoup(dico):
    """Renvoie les tours de départ et d'arrivée du dernier coup effectué."""
    clé=list(dico.keys())
    valeur=list(dico.values())
    coup1=dico[clé[-1]]
    coup2=dico[clé[len(clé)-2]]
    changement=[]
    for i in range(len(coup1)):
        if len(coup1[i])<len(coup2[i]):
            tour_depart=i
        elif len(coup1[i])>len(coup2[i]):
            tour_arrivee=i
    return tour_depart, tour_arrivee

def annulerDernierCoup(dico):
    """Annule le dernier coup en retirant la configuration correspondante du dictionnaire."""
    clé=dico.keys()
    dico.pop(clé[-1])
    
##Partie E


def sauvScore(nb_disques,nb_coups,score,temps):
    """Enregistre le score d'une partie."""
    nom_joueur=str(input("Quelle est vôtre nom? "))
    clé=list(score.keys())
    score[len(clé)]=[nom_joueur,nb_coups,nb_disques,temps]
    return score


def afficheScores(score):
    """Affiche les scores en fonction du classement choisi."""
    cle=list(score.keys())
    valeur=list(score.values())
    liste=[]
    liste_temps=[]
    for elt in cle:
        liste.append([score[elt][1],elt])
        liste_temps.append(score[elt][1])

    liste_temps.sort()
    for i in range(len(liste_temps)):
        for j in range(len(liste)):
            if liste[j][0]==liste_temps[i]:
                print(cle[i]+1,valeur[i][0],valeur[i][1])
                
                
def afficheChronos(score):
    """Affiche les scores en fonction du classement choisi."""
    cle=list(score.keys())
    valeur=list(score.values())
    liste=[]
    liste_temps=[]
    for elt in cle:
        liste.append([score[elt][3],elt])
        liste_temps.append(score[elt][3])

    liste_temps.sort()
    for i in range(len(liste_temps)):
        for j in range(len(liste)):
            if liste[j][0]==liste_temps[i]:
                print(cle[i]+1,valeur[i][0],round(float(valeur[i][3]),2))



def reflexionMoy(score,nom_joueur):
    """Calcule la moyenne des chronos d'un joueur."""
    valeur=list(score.values())
    liste_joueur=[]
    for elt in valeur:
        if elt[0]==nom_joueur:
            liste_joueur.append([elt[1],elt[3]])
    
    moy=0
    for elt in liste_joueur:
        moy+=elt[1]/elt[0]
    moy=moy/len(liste_joueur)
    
    return moy

def afficheTPC(score):
    """Affiche le classement par rapidité."""
    valeur=list(score.values())
    liste_moy=[]
    for elt in valeur:
        a=[elt[0],round(reflexionMoy(score,elt[0]),2)]
        if  a not in liste_moy:
            liste_moy.append(a)
    
    
    liste_temps=[liste_moy[i][1] for i in range(len(liste_moy))]
    liste_temps.sort()
    for i in range(len(liste_temps)):
        print(i+1,liste_moy[i][0],liste_temps[i])
    
def hanoi(n, source, cible, auxiliaire, mouvements):
    """Implémente l'algorithme de résolution du problème des tours de Hanoi."""
    if n > 0:
        # Déplacer n - 1 disques de la source à l'auxiliaire en utilisant la cible comme tampon
        hanoi(n - 1, source, auxiliaire, cible, mouvements)
        
        # Déplacer le disque restant de la source vers la cible
        mouvements.append((source, cible))
        
        # Déplacer les n - 1 disques de l'auxiliaire vers la cible en utilisant la source comme tampon
        hanoi(n - 1, auxiliaire, cible, source, mouvements)
        

def anime(mouvements,n):
    """Anime la résolution des tours de Hanoi."""
    turtle.speed(50)
    turtle.reset()
    plat=init(n)
    dessinePlateau(n)
    dessineConfig(plat,n)
    for elt in mouvements:
        effaceDisque(plat[elt[0]-1][-1],plat,n)
        
        
        liste_temporaire=plat[elt[1]-1][:]
        liste_temporaire.append(plat[elt[0]-1][-1])
        plat[elt[1]-1]=liste_temporaire[:]
        
        liste_temporaire.clear()
        
        liste_temporaire=plat[elt[0]-1][:]
        liste_temporaire.pop()
        plat[elt[0]-1]=liste_temporaire[:]
        dessineDisque(plat[elt[1]-1][-1], plat, n)
    turtle.speed(100)


def main():
    """Fonction principale du programme."""
    continuer=True
    score={}
    print("Bienvenue dans les Tour d'Hanoi")
    print("Voici les règles:")
    print("Les tours de Hanoi sont un jeu de réflexion consistant à déplacer des disques de différents diamétres, d'une tour de départ à une tour d'arrivée, en passant par une tour intermédiaire, en un minimum de coups, avec ces contraintes :\n  On ne peut déplacer qu'un seul disque à la fois \n  On ne peut pas placer un disque sur un disque plus petit que lui")
    while continuer:
        print("1.Jouer\n2.Afficher score\n3.Voir théorie\n4.Quitter")
        entree=input("Que voulez-vous faire?(1/2/3/4)")
        if entree=='1':
            turtle.reset()
            turtle.speed(100)
            n=int(input("Combien de disque souhaitez-vous?"))
            print("Entrer -1 pour valeur de la tour de départ si vous voulez abandonner et -2 si vous voulez revenir 1 coup en arrière")
            plateau=init(n)
            boucleJeu(plateau,n,score)

        elif entree=='2':
            oui=True
            while oui:
                if score!={}:
                    print("1.Classement par score\n2.Classement par chronos\n3.Classement par rapidité")
                
                    entree2=input("Quel classement voulez-vous affichez? ")
                    if entree2=="1":
                        afficheScores(score)
                    elif entree2=="2":
                        afficheChronos(score)
                    elif entree2=="3":
                        afficheTPC(score)
                    else:
                        print("Veuillez entrer 1 2 ou 3 comme valeur")
                    oui=input("Voulez vous continuer à regarder les scores? (o/n)")=="o"
                else:
                    print("Désolé aucune partie n'à encore était enregistrer")
                    oui=False
        elif entree=="3":
            n=int(input("Combien de disque voulez-vous ?"))
            mouvements=[]
            hanoi(n,1,3,2,mouvements)
            print(mouvements)
            anime(mouvements,n)
        elif entree=="4":
            print("Au revoir")
            continuer=False
            
# Exécution du programme
main()
