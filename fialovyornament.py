# nakreslí vesnici pomocí knihovny turtle
  
from turtle import exitonclick, bgcolor, screensize, title, colormode
import turtle
from random import randint

def cara(t, strana, barva):

    t.pencolor(barva)
    t.forward(strana)
    t.left(10)

def main(): 

    # barva pozadí okna
    bgcolor("plum")
    # velikost okna
    # název okna
    title("Fialovy spiralovy ornament")

    # formát barev
    colormode(255)

    # Vytvoříme novou želvu
    t = turtle.Turtle()

    # Želva vypadá jako želva
    t.shape("turtle")

    # nejrychlejší želva = velmi rychlé kreslení
    t.speed(0)
    # velikost pera = silný obrys
    t.pensize(18)

    dilek = 1


    for _ in range(500):
        # nahodné odstíny fialové
        barva = (randint(55, 155), randint(0, 55), randint(155, 255))
        cara(t, dilek, barva)
        dilek = dilek + 0.1

    # zavření okna
    exitonclick()

if __name__ == "__main__":
    main()