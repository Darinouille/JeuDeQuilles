from gui2 import *
from random import *

# ========== 『 Etude de l'état quilles 』 ========== #
def afficheQuilles(q, n):
    ligne = len(q)
    restant = ""
    for j in range(0, n):               # On travaille sur le nombre initial de quilles
        i = 0
        tombe = True
        for i in range(0, ligne):       # On étudie chaque ligne
            if q[i][0] <= j <= q[i][1]: # Quille j est dans une des lignes -> debout
                restant = restant + "|"
                tombe = False
        if tombe:                       # Quille pas dans une des lignes -> tombée
            restant = restant + "."
    return(restant)


# ========== 『 Placement des quilles 』 ========== #
def placementQuille(q, n, rangee, h, pal):
    d = 90
    if rangee % 2 == 1:                                     # Cas nombre quilles impair
        qMilieu = rangee // 2 + 1
        centre = 98
    if rangee % 2 == 0:                                     # Cas nombre quille pair
        qMilieu = rangee // 2
        centre = 58
    if h == -10 and n % 2 == 0:                             # Nombre quille initial pair
            qMilieu = qMilieu + rangee
    if h == -10 and n % 2 == 1:                             # Nombre quille initial impair
            qMilieu = qMilieu + rangee + 1
    if (afficheQuilles(q, n))[qMilieu - 1] == "|":          # Cas où la quille du centre est debout
        quilleDebout(centre, h, qMilieu, True, pal)
    else:                                                   # Cas où la quille du centre est tombée
        quilleTombee(centre, h, qMilieu, True, pal)
    gauche = qMilieu - 1
    for droite in range(qMilieu + 1, n + 1):                # On effectue le placement en partant du centre
        if (afficheQuilles(q, n))[droite - 1] == "|":       # Cas où la quille à droite est debout
            quilleDebout(centre + d, h, droite, True, pal)
        else:                                               # Cas où la quille à droite est tombée
            quilleTombee(centre + d, h, droite, True, pal)
        if gauche == 0 or (n % 2 == 1 and gauche == n // 2 + 1 and h == -10) or (n % 2 == 0 and gauche == n // 2 and h == -10):
            break           # On arrête la boucle quand on a affiché
                            # la quille qui doit être la plus à gauche
                            
        if (afficheQuilles(q, n))[gauche - 1] == "|":       # Cas où la quille à gauche est debout
            quilleDebout(centre - d, h, gauche, True, pal)
        else:                                               # Cas où la quille à gauche est tombée
            quilleTombee(centre - d, h, gauche, True, pal)
        gauche = gauche - 1
        d = d + 90


# ========== 『 Détermination du nombre de quille sur 1 rangée 』 ========== #
def nombreQuille(q, n, pal):
    if n > 8:                                                   # Cas de rangée double
        placementQuille(q, n - n // 2, n - n // 2, 100, pal)    # Rangée du haut
        placementQuille(q, n, n // 2, -10, pal)                 # Rangée du bas
    else :                                                      # Cas de rangée unique
        placementQuille(q, n, n, 50, pal)


# ========== 『 Fonction pour les actions de l'ordinateur 』 ========== #
def ordiJoue(q, pal):
    zoneOrdi(pal)
    ligne = len(q)
    i = randint(1, ligne)   # On choisit une ligne parmi les lignes disponibles
    p = choice(["G", "M", "D"])
    actionOrdi = str(i) + ":" + p
    write(("* joue " + actionOrdi +" *"), align="left", font=("arial", 17, "italic"))
    return actionOrdi


# ========== 『 Fonction pour les actions du joueur 』 ========== #
def joueurJoue(q):
    ligne = len(q)
    Erreur = True
    zoneJoueur()
    write("En attente du joueur…", align="right", font=("arial", 17, "italic"))
    while Erreur:                                                       # Tant que la valeur n'est pas correcte
        c = textinput("Choix", "Quel est votre choix ?")
        i = c[0]
        if len(c) == 3 and c[1]==":" and (i in ["1", "2", "3", "4"]):   # Notation correcte
            i = int(c[0])
            p = c[2]
            if (1 <= i <= ligne) and (p in ["G", "M", "D"]):            # Valeurs correctes
                Erreur = False
            else:                                                       # Valeurs incorrectes
                zoneJoueur()
                write("Erreur de valeurs", align="right", font=("arial", 17 ,"italic"))
        else:                                                           # Notations incorrectes
            zoneJoueur()
            write("Erreur de notation", align="right", font=("arial", 17, "italic"))
    zoneJoueur()
    write(("* joue " + c + " *"), align="right", font=("arial", 17, "italic"))
    return c


# ========== 『 Fonction milieu 』 ========== #
def jouerMilieu(c, q):
    i = int(c[0])                           # Calcul des nouvelles bornes pour les insérer dans la liste q
    borneA = q[i-1][0]
    borneB = (q[i-1][1] - q[i-1][0]+1) // 2 - 2 + borneA
    borneC = (q[i-1][1] - q[i-1][0]+1) // 2 + 1 + borneA
    borneD = q[i-1][1]
    if borneA > borneB and borneC > borneD: # Cas où la ligne disparait
        q.remove(q[i-1])
    elif borneA > borneB:                   # Cas où il reste une ligne à droite
        q.insert(i,[borneC, borneD])
        q.remove(q[i-1])
    else:                                   # Cas où la ligne est bien divisée par 2
        q.insert(i,[borneA, borneB])
        q.insert(i+1,[borneC, borneD])
        q.remove(q[i-1])
    return q


# ========== 『 Fonction coté 』 ========== #
def jouerCote(c, q):
    i = int(c[0])
    p = str(c[2])                       # On calcule les nouvelles bornes pour les insérer dans la liste q
    borneA = q[i-1][0]
    borneD = q[i-1][1]
    if p == "G" and borneA != borneD:   # Cas où la quille de gauche tombe
        borneA = borneA + 1
        q.insert(i, [borneA, borneD])
    if p == "D" and borneA != borneD:   # Cas où la quille de droite tombe
        borneD = borneD - 1
        q.insert(i, [borneA, borneD])
    q.remove(q[i-1])                    # Si la dernière quille de la ligne tombe on supprime juste la ligne
    return q


# ========== 『 Fonction qui traduit le choix 』 ========== #
def jouer(c,q):
    p = str(c[2])
    if p == "M":                        # Cas où on joue M
        return jouerMilieu(c, q)
    if p in ["G", "D"]:                 # Cas où on joue G ou D
        return jouerCote(c, q)
    

# ========== 『 Update des quilles 』 ========== #
def updateQuille(l, t):
    postIt(-50, -180, 250, 100)
    goto(75, -215)
    write("- Tour " + str(t) + " -", align="center", font=("arial", 22, "bold"))
    goto(75, -245)
    write("Il y a actuellement", align="center", font=("arial", 20, "italic", "bold"))
    goto(75, -270)
    if l == 1:
        write(str(l) + " ligne", align="center", font=("arial", 20, "italic", "bold"))
    else:
        write(str(l) + " lignes", align="center", font=("arial", 20,"italic", "bold"))
