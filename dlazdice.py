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

if __name__ == "__main__":
    main()