# nakreslí vesnici pomocí knihovny turtle
  
from turtle import exitonclick, bgcolor, title, colormode
import turtle
from random import randint

def cara(t, strana, barva):

    t.pencolor(barva)
    t.forward(strana)
    t.left(60)

def main(): 

    # barva pozadí okna
    bgcolor("aqua")
    # velikost okna
    # název okna
    title("Barevný šestihran ornament")

    # formát barev
    colormode(255)

    # Vytvoříme novou želvu
    t = turtle.Turtle()

    # Želva vypadá jako želva
    t.shape("turtle")

    # nejrychlejší želva = velmi rychlé kreslení
    t.speed(0)
    # velikost pera = silný obrys
    t.pensize(5)

    dilek = 5
    green = 255
    blue = 0


    for _ in range(255):
        # nahodné odstíny fialové
        barva = (0, green, blue)
        cara(t, dilek, barva)
        dilek = dilek + 2
        green = green - 1
        blue = blue + 1

    # zavření okna
    exitonclick()

if __name__ == "__main__":
    main()