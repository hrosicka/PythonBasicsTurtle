# nakreslí vesnici pomocí knihovny turtle
  
from turtle import exitonclick, bgcolor, title, colormode
import turtle
from random import randint
# ze souboru vesnice je potřeba funkce domecek
from vesnice import *

def posun(t, strana):

    t.penup()
    t.forward(strana)
    t.left(60)
    t.pendown()

def main(): 

    # barva pozadí okna
    bgcolor("black")
    # velikost okna
    # název okna
    title("Crazy village")

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

    dilek = 50
    red = 255
    green = 0
    velikostDomecku = 3


    for _ in range(20):

        barva = (red, green, 0)
        posun(t, dilek)
        dilek = dilek + 20
        green = green + 12
        red = red - 12
        velikostDomecku = velikostDomecku + 1
        domecek(t, velikostDomecku, barva)

    # zavření okna
    exitonclick()

if __name__ == "__main__":
    main()