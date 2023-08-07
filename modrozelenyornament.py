# nakreslí vesnici pomocí knihovny turtle
  
from turtle import exitonclick, bgcolor, screensize, title, colormode
import turtle
from random import randint
import math

def cara(t, strana, barva):

    t.pencolor(barva)
    t.forward(strana)
    t.left(90)

def main(): 

    # barva pozadí okna
    bgcolor("lightblue3")
 
    # název okna
    title("Modrozeleny ornament")

    # format barev
    colormode(255)

    # Vytvoříme novou želvu
    t = turtle.Turtle()

    # Želva má tvar želvy
    t.shape("turtle")

    
    # nejrychlejší želva = velmi rychlé kreslení
    t.speed(0)
    # velikost pera = silný obrys
    t.pensize(5)

    # délka strany čtverce
    strana = 8

    for _ in range(100):
        # náhodné odstíny modrozelené
        barva = (randint(0, 55), randint(0, 155), randint(55, 255))
        cara(t, strana, barva)
        strana = strana + 8

    # zavření okna
    exitonclick()

if __name__ == "__main__":
    main()