# ========== 『 Paramètres de base 』 ========== #
from time import *
from engine import *

setup(width=1.0, height=1.0)
tracer(False)
hideturtle()
#speed(0)
#delay(0)
bgcolor("#2E3846")
pensize(5)
up()


# ========== 『 Décor 』 ========== #
palette = []
for couleurQuille in range(0,15):
    nouvelleCouleur = (choice(["#78E463", "#FF6CAF", "#7B48FF", "#3350B5", "#FD8727", "#FFF548", "#FD504B"]))
    palette.append(nouvelleCouleur)
    
consignes(400,-145,"debout", palette)

security(-300, 180, 740, 370)
fenetre(-650, 105, 300, 395, "Logs.txt")

bouton(-632, -105, 50, 50, "1")
bouton(-557, -105, 50, 50, "2")
bouton(-482, -105, 50, 50, "3")
bouton(-407, -105, 50, 50, "4")

bouton(-630, -180, 70, 50, "G")
bouton(-530, -180, 70, 50, "M")
bouton(-430, -180, 70, 50, "D")

consignes(-430, 250, "tombée", palette)

nomDossiers = ["orteils", "Photos", "Downloads", "26/01/20", "Aubin", "darina"]
for colonne1 in range (0,4):
    fichier(555, 350 - colonne1 * 100, nomDossiers[colonne1])
for colonne2 in range (0,2):
    fichier(440, 350 - colonne2 * 100, nomDossiers[(colonne2)+4])


# ========== 『 Moteur du jeu 』 ========== #
nInit = 15#(randint(3, 15))
quille = list([[0,nInit-1]])
nombreQuille(quille, nInit, palette)
tour = 1

continuer = True
joueurGagne = True
while continuer:                    # Tant qu'il n'y a pas de gagnant
    goto(75, -270)
    choix = joueurJoue(quille)
    security(-300, 180, 740, 370)
    nombreQuille(jouer(choix, quille), nInit, palette)
    ligne = len(quille)
    updateQuille(ligne, tour)
    if ligne == 0:                  # Cas où le joueur gagne
        sleep(1)
        zoneOrdi(palette)
        write("Bien joué, t'as gagné !", align="left", font=("arial", 17, "normal"))
        zoneJoueur()
        write(":)", align="right", font=("arial", 17, "normal"))
        continuer = False
        joueurGagne = True
    else:                           # Cas où la partie continue
        tour = tour + 1
        sleep(1)
        choix = ordiJoue(quille, palette)
        security(-300, 180, 740, 370)
        nombreQuille(jouer(choix, quille), nInit, palette)
        ligne = len(quille)
        updateQuille(ligne, tour)
        if ligne == 0:              # Cas où l'ordinateur gagne
            sleep(1)
            zoneOrdi(palette)
            write("La honte, t'as perdu", align="left", font=("arial", 17, "normal"))
            zoneJoueur()
            write(">:(", align="right", font=("arial", 17, "normal"))
            continuer = False
            joueurGagne = False


# ========== 『 Fin de la partie 』 ========== #
sleep(3)
clear(); bgcolor("black")
etoile = 0
for etoile in range(0, 100):
    x = randint(-700, 700)
    yHaut = randint(50, 400)
    yBas = randint(-400, -20)
    goto(x,yHaut)
    dot(5, "white")
    goto(x,yBas)
    dot(5, "white")
quilleFlotante(200, 10, joueurGagne)
goto(0,0); pencolor("white")
write("Fin de la partie", align="center", font=("arial", 30))
