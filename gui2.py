from gui1 import *

# ========== 『 Dessin de rectangles arrondis 』 ========== #
def rectangle(x, y, longueur, hauteur, couleur, contour):
    goto(x, y)
    setheading(0)
    pencolor(contour)
    fillcolor(couleur)
    begin_fill()
    down()
    for cote in range(0, 2):
        forward(longueur)
        arrondis(right)
        forward(hauteur)
        arrondis(right)
    pencolor("black")
    end_fill()
    up()


# ========== 『 Dessin de bouton 』 ========== #
def bouton(x, y, longueur, hauteur, texte):
    rectangle(x, y, longueur, hauteur, "#70B6E4", "black")
    rectangle(x, y, longueur, hauteur - 10, "#95C7EB", "#97E3FF")
    rectangle(x, y, longueur, hauteur, "", "black")
    goto(x + longueur / 2, y - 40)
    write(texte, align="center", font=("arial", 30, "bold"))


# ========== 『 Création d'une fenêtre 』 ========== #
def fenetre(x, y, longueur, hauteur, texte):
    rectangle(x + 5, y + 45, longueur, hauteur, "#5E93CB", "black")
    # Barre latérale
    fillcolor("#576271")
    begin_fill()
    down()
    forward(longueur)
    arrondis(right)
    forward(40)
    right(90)
    forward(longueur + 10)
    right(90)
    forward(40)
    arrondis(right)
    end_fill()
    up()
    # Détails barre latérale
    goto(x + 15, y + 3)
    write("x", font=("arial", 38, "bold"))
    goto(x + longueur / 2, y + 8)
    pencolor("white")
    write(texte, align="center", font=("arial", 25, "bold"))
    pencolor("black")

    
# ========== 『 Dessin de fichiers 』 ========== #
def fichier(x, y, texte):
    goto(x, y)
    bgcolor("#2E3846")
    pensize(5)
    setheading(90)
    fillcolor("#3C61AB")
    begin_fill()
    down()
    forward(50)
    arrondis(right)
    forward(25)
    arrondis(right)
    left(90)
    forward(50)
    right(90)
    forward(55)
    right(90)
    forward(86)
    end_fill()
    fillcolor("#5E93CB")
    begin_fill()
    for cote in range(0, 2):
        right(90)
        forward(45)
        right(90)
        forward(86)
    up()
    end_fill()
    goto(x + 45, y - 30)
    pencolor("white")
    write(texte, align="center", font=("arial", 15, "normal"))
    pencolor("black")


# ========== 『 Dessin de Post It 』 ========== #
def postIt(x, y, longueur, hauteur):
    goto(x, y)
    setheading(0)
    fillcolor("#FFFD93")
    begin_fill()
    pensize(5)
    down()
    forward(longueur - 20)
    right(45)
    forward(28)
    right(45)
    forward(hauteur - 20)
    right(90)
    forward(longueur)
    right(90)
    forward(hauteur)
    end_fill()
    right(90)
    forward(longueur - 20)
    right(45)
    forward(28)
    right(135)
    forward(20)
    right(90)
    forward(20)
    up()


# ========== 『 Indication état des quilles 』 ========== #
def consignes(x, y, etat, pal):
    postIt(x, y, 120, 120)
    if etat == "debout":
        quilleTournee(x + 30, y - 35)
    if etat == "tombée":
        quilleTombee(x + 90, y - 35, 1, False, pal)
    goto(x - 15, y - 50)
    pencolor("white")
    write(("Quille " + etat), align="right", font=("arial", 20, "bold"))
    goto(x - 5, y - 100)
    write("↳", align="right", font=("arial", 50, "bold"))
    pencolor("black")

    
# ========== 『 Dessin zone Quille 』 ========== #
def security(x, y, longueur, hauteur):
    fenetre(x, y, longueur, hauteur, "Security.wav")
    rectangle(x + 25, y - 20, longueur - 40, hauteur - 85, "white", "white")
    rectangle(x + 45, y - 40, longueur - 80, hauteur - 125, "#5E93CB", "#5E93CB")
    rectangle(x + 105, y - 10, longueur - 200, hauteur - 65, "#5E93CB", "#5E93CB")
    rectangle(x + 15, y - 60, longueur - 20, hauteur - 165, "#5E93CB", "#5E93CB")
    goto(x + 640, y - 40)
    pencolor("white")
    write("REC", align="right", font=("arial", 25, "bold"))
    goto(x + 580, y - 55)
    write("•", align="right", font=("arial", 50, "bold"))
    pencolor("black")
    up()


# ========== 『 Dessin zone action ordi 』 ========== #
def zoneOrdi(pal):
    rectangle(-590, -10, 230, 60, "#EEEEEE", "black")
    quilleDebout(-575, -20, 0, False, pal)
    goto(-550, -40)
    write("Ordinateur", font=("arial", 20, "bold"))
    goto(-550, -65)


# ========== 『 Dessin zone action joueur 』 ========== #
def zoneJoueur():
    rectangle(-630, 85, 230, 60, "#EEEEEE", "black")
    quilleTournee(-415, 75)
    goto(-435, 55)
    write("Joueur", align="right", font=("arial", 20, "bold"))
    goto(-435, 30)
