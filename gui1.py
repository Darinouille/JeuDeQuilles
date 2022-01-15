from turtle import *

# ========== 『 Dessin d'arrondis 』 ========== #
def arrondis(sens):
    for cote in range(0, 2):
        sens(30)
        forward(4)
    sens(30)
    
# ========== 『 Dessin de quille debout 』 ========== #
def quilleDebout(x, y, nombre, numerotation, pal):
    if numerotation:
        couleur = pal[nombre - 1]
    else:
        couleur = "#78E463"
                                # Corps
    goto(x, y);
    setheading(110);
    fillcolor(couleur);
    begin_fill();
    down()
    circle(25, 160, 22)
    forward(3)
    posSac = position()
    forward(55)
    for pied in range(0, 2):
        arrondis(left)
        forward(10)
    right(90)
    forward(8)
    posJambe = position()
    arrondis(left)
    up()
    goto(posJambe);
    setheading(270);
    down()
    for pied in range(0, 2):
        forward(8)
        arrondis(left)
    forward(65)
    up()
                                # Sac à dos
    goto(posSac);
    setheading(180);
    down()
    forward(5)
    arrondis(left)
    forward(30)
    arrondis(left)
    forward(5)
    left(90)
    forward(40)
    end_fill();
    up()
                                # Vitre
    goto(x - 5, y + 2);
    setheading(180);
    fillcolor("#95C7EB");
    begin_fill();
    down()
    for cercle in range(0, 2):
        forward(14)
        circle(14, 180, 10)
    end_fill();
    up()
    goto(x - 3, y - 10);
    pensize(10);
    pencolor("white");
    down()
    forward(10)
    pencolor("black");
    pensize(5);
    up()
                                # Nombre
    if numerotation:
        goto(x - 23, y - 53)
        write(nombre, align="center", font=("arial", 23, "bold"))


# ========== 『 Dessin de quille tombée 』 ========== #
def quilleTombee(x, y, nombre, numerotation, pal):
    if numerotation:
        couleur = pal[nombre - 1]
    else:
        couleur = "#78E463"
                                # Corps
    goto(x, y);
    setheading(110);
    fillcolor(couleur)
    circle(25, 160, 22)
    forward(3)
    begin_fill(), down()
    posSac = position()
    forward(55)
    for pied in range(0, 2):
        arrondis(left)
        forward(10)
    right(90)
    forward(8)
    posJambe = position()
    arrondis(left)
    up()
    goto(posJambe);
    setheading(270);
    down()
    for pied in range(0, 2):
        forward(8)
        arrondis(left)
    forward(53)
                                # Coupure
    left(100)
    forward(5)
    right(20)
    forward(8)
    left(30)
    forward(10)
    posOs = position()
    right(20)
    forward(5)
    left(20)
    forward(8)
    right(30)
    forward(10)
    end_fill();
    up()
                                # Sac à dos
    goto(posSac);
    setheading(180);
    begin_fill();
    down()
    forward(5)
    arrondis(left)
    forward(30)
    arrondis(left)
    forward(5)
    left(90)
    forward(40)
    end_fill();
    up()
                                # Os
    goto(posOs);
    setheading(90);
    fillcolor("white");
    begin_fill();
    down()
    forward(10)
    setheading(-10)
    circle(5, 270)
    setheading(100)
    circle(5, 270)
    setheading(270)
    forward(10)
    left(90)
    forward(5)
    end_fill();
    up()
                                # Nombre
    if numerotation:
        goto(x - 23, y - 53)
        write(nombre, align="center", font=("arial", 23, "bold"))


# ========== 『 Dessin de quille tournée dans l'autre sens 』 ========== #
def quilleTournee(x, y):
    couleur = "#FF6CAF"
                                # Corps
    goto(x, y);
    setheading(70);
    fillcolor(couleur);
    begin_fill();
    down()
    circle(-25, 160, 22)
    forward(3)
    posSac = position()
    forward(55)
    for pied in range(0, 2):
        arrondis(right)
        forward(10)
    left(90)
    forward(8)
    posJambe = position()
    arrondis(right)
    up()
    goto(posJambe);
    setheading(270);
    down()
    for pied in range(0, 2):
        forward(8)
        arrondis(right)
    forward(65)
    end_fill();
    up()
                                # Sac à dos
    goto(posSac);
    setheading(0);
    begin_fill();
    down()
    forward(5)
    arrondis(right)
    forward(30)
    arrondis(right)
    forward(5)
    right(90)
    forward(40)
    end_fill();
    up()
                                # Vitre
    goto(x + 5, y + 2);
    setheading(0);
    fillcolor("#95C7EB");
    begin_fill();
    down()
    for cercle in range(0, 2):
        forward(14)
        circle(-14, 180, 10)
    end_fill();
    up()
    goto(x + 3, y - 10);
    pensize(10);
    pencolor("white");
    down()
    forward(10)
    pensize(5);
    pencolor("black");
    up()


# ========== 『 Dessin de quille Fin de la partie 』 ========== #
def quilleFlotante(x, y, joueurGagne):
    if joueurGagne:
        couleur = "#78E463"
    else:
        couleur = "#FF6CAF"
                                # Corps
    goto(x, y);
    setheading(66);
    fillcolor(couleur);
    begin_fill();
    down()
    circle(25, 160, 10)
    forward(3)
    posSac = position()
    forward(55)
    for pied in range(0, 2):
        arrondis(left)
        forward(10)
    right(90)
    forward(8)
    posJambe = position()
    arrondis(left)
    up()
    goto(posJambe);
    setheading(225);
    down()
    for pied in range(0, 2):
        forward(8)
        arrondis(left)
    forward(65)
    end_fill();
    up()
                                # Sac à dos
    goto(posSac);
    setheading(135);
    begin_fill();
    down()
    forward(5)
    arrondis(left)
    forward(30)
    arrondis(left)
    forward(5)
    left(90)
    forward(40)
    end_fill();
    up()
                                # Vitre
    goto(x - 5, y + 2);
    setheading(135);
    fillcolor("#95C7EB");
    begin_fill();
    down()
    for cercle in range(0, 2):
        forward(14)
        circle(14, 180, 13)
    end_fill();
    up()
    goto(x - 10, y - 10);
    pensize(10);
    pencolor("white");
    down()
    forward(10)
    pensize(5);
    pencolor("black");
    up()
