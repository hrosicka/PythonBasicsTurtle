# barevná (random) pavučina pomocí knihovny turtle
import turtle
from turtle import bgcolor, exitonclick, title
from random import randrange
import tkinter

title("Spider Web")

img = tkinter.Image("photo", file="turtle_ico.png")
turtle._Screen._root.iconphoto(True, img)

# Vytvoříme novou želvu
t = turtle.Turtle()

bgcolor("black")
t.pensize(3)
t.speed(10)

# uzel se skládá ze 3 smyček
for uzel in range (100):
    # smyčka uzlu se skládá ze 4 hran
    for smycka in range (3):
        # pro každý uzel je náhodně vygenerována barva
        t.pencolor(randrange(0,10)/10, randrange(0,10)/10, randrange(0,10)/10)
        for hrana in range (4):
            t.forward(20)
            t.left(90)
        t.left(20)

    t.forward(20 + 5*uzel)

exitonclick()