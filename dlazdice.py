# nakreslí vesnici pomocí knihovny turtle
  
from turtle import exitonclick, bgcolor, screensize, title, colormode
import turtle
from random import randint, randrange
import math

def dlazdice(t, strana, barva):

    t.pencolor("black")
    t.fillcolor(barva)
    t.begin_fill()
    t.left(60)
    for _ in range(6):
        t.forward(strana)
        t.right(60)
    t.end_fill()

    t.penup()
    t.backward(0)
    t.pendown()

def main(): 

    # barva pozadí okna
    bgcolor("black")
    # velikost okna
    # název okna
    title("Dlazdice")

    # format barev
    colormode(255)

    # Vytvoříme novou želvu
    t = turtle.Turtle()

    t.shape("turtle")

    
    # nejrychlejší želva = velmi rychlé kreslení
    t.speed(0)
    # velikost pera = slabý obrys
    t.pensize(2)

    strana = 30
    t.forward(strana)
    t.left(60)
    t.forward(strana)
    t.right(120)

    for _ in range(6):
        for _ in range(6):
            # nahodne odstiny ruzove
            barva = (randint(155, 255), randint(0, 55), randint(55, 155))
            dlazdice(t, strana, barva)
            t.penup()
            t.right(60)
            t.forward(2*strana)
            t.pendown()
            t.right(60)
        t.left(60)
        t.forward(strana)

    # zavření okna
    exitonclick()

'''
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
  '''  
    

if __name__ == "__main__":
    main()