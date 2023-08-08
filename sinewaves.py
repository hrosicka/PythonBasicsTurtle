# nakreslí vesnici pomocí knihovny turtle
  
from turtle import exitonclick, bgcolor, title, colormode
import turtle
from random import randint
import math
import turtle
 
bgcolor("lightblue")
title("Sine waves")

# 4 turtles ~ 4 waves 
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()

t1.speed(0)
t2.speed(0)
t3.speed(0)
t4.speed(0)
 
t1.penup()
t2.penup()
t3.penup()
t4.penup()

t1.goto(-360, 0)
t2.goto(-300, -20)
t3.goto(-240, +10)
t4.goto(-180, +20)

t1.pendown()
t2.pendown()
t3.pendown()
t4.pendown()

t1.pencolor("lightseagreen")
t2.pencolor("lightskyblue")
t3.pencolor("deepskyblue")
t4.pencolor("cyan3")

t1.pensize(20)
t2.pensize(10)
t3.pensize(15)
t4.pensize(25)


for x in range(-360,360):
    y = 100*math.sin(math.radians(x))
    t1.goto(x, y)
    t2.goto(x+60, y-20)
    t3.goto(x+120, y+10)
    t4.goto(x+180, y+20)

# zavření okna
exitonclick()

