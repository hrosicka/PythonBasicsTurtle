# nakreslí květinu pomocí knihovny turtle
  
from turtle import exitonclick, bgcolor, title
import turtle
import tkinter



# jedny okvětní lísky na květině
def okvetniListky(t, s, count, col1, col2):

    # nastaví barvu okvětních lístků - barva výplně a barva obrysu
    t.fillcolor(col1)
    t.pencolor(col2)
    
    # začátek toho, co se bude vyplňovat barvou
    t.begin_fill()
    
    # nakreslí vrstvu okvětních lístků
    for _ in range(count):
        t.circle(s)
        t.right(360/count)

    # vyplní vše od begin_fill
    t.end_fill()


# funkce vykreslí 1 květinu
def kvetina(t, s, col1, col2, col3, col4):

    # nastaví barvu vnějších okvětních lístků
    okvetniListky(t, s, 12, col1, col4)

    # nakreslí první vnitřní okvětní lístky
    okvetniListky(t, 2*s/3, 9, col2, col3)

    # nakreslí druhé vnitřní okvětní lístky
    okvetniListky(t, s/3, 6, col3, col2)

    # nakreslí střed květiny
    okvetniListky(t, s/6, 8, col4, col4)


def main():    
    # barva pozadí okna
    bgcolor("black")

    title("Flower")

    img = tkinter.Image("photo", file="turtle_ico.png")
    turtle._Screen._root.iconphoto(True, img)   

    # Vytvoříme novou želvu
    t = turtle.Turtle()

    # nejrychlejší želva = velmi rychlé kreslení
    t.speed(0)
    # velikost pera = slabý obrys
    t.pensize(1)
    
    print("Flower")
    print("------")
    # poloměr jednoho květu
    s = int(input("Zadej poloměr jednoho květu, ze kterých se bude skládat kytice: "))

    col1 = input("Zadej barvu vnějších lístků květiny(název nebo hex(# RRGGBB)): ")
    col2 = input("Zadej alternativní barvu vnějších lístků květiny(název nebo hex(# RRGGBB)): ")
    col3 = input("Zadej barvu středních lístků květiny(název nebo hex(# RRGGBB)): ")
    col4 = input("Zadej alternativní barvu středních lístků květiny(název nebo hex(# RRGGBB)): ")
    col5 = input("Zadej barvu středu květiny(název nebo hex(# RRGGBB)): ")

    # první květina do kytice
    t.penup()
    t.setpos(8*s/3 , 5*s/3)
    t.pendown()
    kvetina(t,s, col2, col4, col3, col5)

    # druhá květina do kytice
    t.penup()
    t.setpos(-7*s/3, -9*s/3)
    t.pendown()
    kvetina(t,s, col1, col4, col3, col5)

    # třetí květina do kytice
    t.penup()
    t.setpos(6*s/3, -8*s/3)
    t.pendown()
    kvetina(t,s, col1, col3, col4, col5)

    # čtvrtá květina do kytice
    t.penup()
    t.setpos(-8*s/3, 6*s/3)
    t.pendown()
    kvetina(t,s, col2, col3, col4, col5)

    # pátá květina do kytice
    t.penup()
    t.setpos(11*s/3, 0)
    t.pendown()
    kvetina(t,s, col2, col3, col4, col5)

    # šestá květina do kytice
    t.penup()
    t.setpos(0, 11*s/3)
    t.pendown()
    kvetina(t,s, col2, col4, col3, col5)

    # sedmá květina do kytice
    t.penup()
    t.setpos(-11*s/3, 0)
    t.pendown()
    kvetina(t,s, col1, col4, col3, col5)

    # osmá květina do kytice
    t.penup()
    t.setpos(0, -12*s/3)
    t.pendown()
    kvetina(t,s, col2, col4, col3, col5)

    # devátá květina do kytice
    t.penup()
    t.setpos(0, 0)
    t.pendown()
    kvetina(t,s, col1, col3, col4, col5)

    # zavření okna
    exitonclick()


if __name__ == "__main__":
    main()