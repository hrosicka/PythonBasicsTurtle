# nakreslí vesnici pomocí knihovny turtle
  
from turtle import exitonclick, bgcolor, screensize, title
import turtle
from random import randint, randrange
import math
import tkinter

def domecek(t, rozmer, fasada):

    t.pencolor(fasada)
    t.fillcolor(fasada)
    t.begin_fill()
    for _ in range(4):
        t.forward(8*rozmer)
        t.right(90)
    t.end_fill()

    t.penup()
    t.backward(rozmer)
    t.pendown()

    t.pencolor("darkred")
    t.fillcolor("red")
    t.begin_fill()
    for _ in range(3):
        t.forward(10*rozmer)
        t.left(120)
    t.end_fill()

    t.penup()
    t.forward(3*rozmer)
    t.right(90)
    t.forward(2*rozmer)

    t.pendown()

    t.pencolor("blue")
    t.fillcolor("lightblue")
    t.begin_fill()
    for _ in range(4):
        t.forward(4*rozmer)
        t.left(90)
    t.end_fill()

    t.right(-90)

    # želva se otiskne do rohu okna
    t.stamp()

def main(): 

    # barva pozadí okna
    bgcolor("black")
    # velikost okna
    screensize(250,250)
    # název okna
    title("Levitating village")

    img = tkinter.Image("photo", file="turtle_ico.png")
    turtle._Screen._root.iconphoto(True, img)

    # Vytvoříme novou želvu
    t = turtle.Turtle()

    # tvarem želvy je želva
    t.shape("turtle")
    # nejrychlejší želva = velmi rychlé kreslení
    t.speed(0)
    # velikost pera = slabý obrys
    t.pensize(2)


    # vesnice má 100 domečků
    for _ in range(100):

        # náhodně určená poloha domku z intervalu
        x = randint(-300, 300)
        y = randint(-300, 300)
        # tužka nahoru
        t.penup()
        # přesun na pozici
        t.goto(x, y)
        # tužka dolů
        t.pendown()

        # náhodně vygenerovaná barva fasády
        barva = randrange(0,10)/10, randrange(0,10)/10, randrange(0,10)/10

        # domky blíže k centru mohou být větší, na periferii menší
        if math.sqrt(pow(x,2) + pow(y,2)) < 200:
            velikost = randint(8,12)
        else:
            velikost = randint(4,8)

        # zavoláme funkci na vykreslení domečku
        domecek(t, velikost, barva)
    
    # zavření okna
    exitonclick()

if __name__ == "__main__":
    main()