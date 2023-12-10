

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
    for i in plateau:
        for x in i:
            if numdisque == x:
                return plateau.index(i), i.index(x)    #retourne d'abord la n-tour, et ensuite la n-position dans la tour

def verifDepl(plateau, nt1, nt2):
    taille=plateau[nt1-1][len(plateau[nt1-1])-1]
    if plateau[nt2-1]==[]:
        return True
    elif plateau[nt2-1][len(plateau[nt2-1])-1]>taille:
        return True
    else:
        return False

def verifVictoire(plateau,n):
    return plateau[2]==[i for i in range(n,0,-1)]




#Partie 2
import turtle
    
# Fonction pour dessiner le plateau avec trois tours
def dessinePlateau(n):              #J'en ai une autre qui fait des tours plus larges mais c'est plus chiant pour les tracer et pour la suite
    largeur_plateau = 40+30*n        #Mais demandes moi si tu la veux
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

# Sous fonction pour obtenir l'emplacement du disque dans la liste

#Fonction pour tracer le disque (ça marche pas à partir de turtle)


#fonction auxilière pour tracer/effacer les disques
def dessineDisque(nd, plateau, n):
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
  #Les autre choses demandées dans la partie 2 dépendent de la fonction qui marche pas donc j'ai pas pus faire

def effaceDisque(nd,plateau,n):
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
    for i in range(n):
        dessineDisque(i+1,plateau,n)

def effaceTout(plateau,n):
    for i in range(n):
        effaceDisque(i+1,plateau,n)


  
#Partie C
import time
#Fonction qui initialise l'emplacement des disques de départs et d'arrivé (j'ai pas pus tester pck j'arrive pas à tracer les disques
def lireCoords(plateau):
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
                if plateau[tour_arrivee-1]==[]:
                    flag = False
                elif plateau[tour_arrivee - 1][-1] < plateau[tour_depart - 1][-1]:
                    flag = True
                elif tour_arrivee in [1,2,3]:
                    flag = False
                if tour_arrivee not in [1,2,3]:
                    print("Le numéro de la tour doit être entre 1 et 3.")
                elif len(plateau[tour_arrivee - 1]) > 0 and plateau[tour_arrivee - 1][-1] < plateau[tour_depart - 1][-1]:
                    print("Le disque sélectionné ne peut pas être placé sur cette tour. Choisissez une autre tour.")
            tour_depart=tour_depart-1
            tour_arrivee=tour_arrivee-1
        return tour_depart , tour_arrivee


def jouerUnCoup(plateau,n):
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
            print(1)
            print(score)
            score=sauvScore(n,nb_coup,score,temps_jeu)
            print(score)



def main():
    continuer=True
    score={}
    while continuer:
        turtle.reset()
        turtle.speed(100)
        n=int(input("Combien de disque souhaitez-vous?"))
        plateau=init(n)
        boucleJeu(plateau,n,score)
        continuer=(input("Voullez-vous rejouer?(o/n)")=="o")
    


##Partie D

def dernierCoup(dico):
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
    clé=dico.keys()
    dico.pop(clé[-1])
    
##Partie E


def sauvScore(nb_disques,nb_coups,score,temps):
    nom_joueur=str(input("Quelle est vôtre nom? "))
    clé=list(score.keys())
    print("clé",clé)
    score[len(clé)]=[nom_joueur,nb_coups,nb_disques,temps]
    return score


def afficheScores(score):
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
        
score={0: ['Louis', 7, 3, 7.907096862792969], 1: ['dz', 8, 3, 16.681009769439697]}
afficheChronos(score)

##main()
turtle.mainloop()