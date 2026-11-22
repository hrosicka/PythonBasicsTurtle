# PythonBasicsTurtle

<div align="center">

  <a href="https://github.com/hrosicka/PythonBasicsTurtle/stargazers">
    <img src="https://img.shields.io/github/stars/hrosicka/PythonBasicsTurtle?style=for-the-badge&color=4F8EF7&logo=starship&logoColor=white" alt="Stars" />
  </a>
  <a href="https://github.com/hrosicka/PythonBasicsTurtle/network/members">
    <img src="https://img.shields.io/github/forks/hrosicka/PythonBasicsTurtle?style=for-the-badge&color=4F8EF7&logo=git&logoColor=white" alt="Forks" />
  </a>
  <a href="https://github.com/hrosicka/PythonBasicsTurtle/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/hrosicka/PythonBasicsTurtle?style=for-the-badge&color=4F8EF7&logo=github&logoColor=white" alt="Contributors" />
  </a>
  <a href="https://github.com/hrosicka/PythonBasicsTurtle/commits/main">
    <img src="https://img.shields.io/github/last-commit/hrosicka/PythonBasicsTurtle?style=for-the-badge&color=6366F1&logo=githubactions&logoColor=white" alt="Last Commit" />
  </a>
  <a href="https://github.com/hrosicka/PythonBasicsTurtle/issues">
    <img src="https://img.shields.io/github/issues/hrosicka/PythonBasicsTurtle?style=for-the-badge&color=F59E0B&logo=github&logoColor=white" alt="Issues" />
  </a>
  <br/>

  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=FFE873" alt="Python" />
  </a>
  <img src="https://img.shields.io/badge/Turtle-Powered-22C55E?style=for-the-badge&logo=python&logoColor=white" alt="Turtle Powered" />
  <img src="https://img.shields.io/badge/Graphics-Creative%20Coding-EC4899?style=for-the-badge&logo=game-developer&logoColor=white" alt="Creative Coding" />
  <img src="https://img.shields.io/badge/Fun-Guaranteed-F59E0B?style=for-the-badge&logo=sparkles&logoColor=white" alt="Fun Guaranteed" />
  <img src="https://img.shields.io/github/repo-size/hrosicka/PythonBasicsTurtle?style=for-the-badge&color=3B82F6&logo=files&logoColor=white" alt="Repo Size" />
  <br/>

  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/hrosicka/PythonBasicsTurtle?style=for-the-badge&color=10B981&logo=opensourceinitiative&logoColor=white" alt="License" />
  </a>

</div>

Dive into a collection of Python Turtle codes that bring your imagination to life on screen. From quaint villages and colorful spider webs to mesmerizing spiral ornaments and enchanting flowers.

# Table of Contents (ToC)

1. [PythonBasicsTurtle](#pythonbasicsturtle)
2. [crazyvilllage.py](#crazyvilllagepy)
    - [Application Window](#application-window)
    - [How It Works](#how-it-works)
3. [vesnice.py](#vesnicepy)
    - [Application Window](#application-window-1)
    - [How It Works](#how-it-works-1)
4. [pavucina.py](#pavucinapy)
    - [Application Window](#application-window-2)
    - [How It Works](#how-it-works-2)
5. [kytice.py](#kyticepy)
    - [Application Window](#application-window-3)
    - [How It Works](#how-it-works-3)
    - [examples](#examples)
6. [fialovyornament.py](#fialovyornamentpy)
7. [modrozelenyornament.py](#modrozelenyornamentpy)

---

- **Villages:** Build your own picturesque village with colorful houses.
- **Spider Webs:** Weave intricate and colorful webs with randomly generated patterns.
- **Spirals:** Draw mesmerizing spiral ornaments with vibrant shades of purple.
- **Flowers:** Design a bouquet of captivating flowers with customizable colors and petal shapes.

---

## crazyvilllage.py
It provides instructions on how to use the Crazy Village application, which draws a village using the Turtle graphics library.
### Application Window
The application window displays a village with houses of different sizes and colors. The background of the window is black, and the title of the window is "Crazy Village".
### How It Works
The application uses the Turtle graphics library to draw the village. The code defines a function called domecek that draws a house. The function takes three arguments:
- **t:** The Turtle object that will be used to draw the house.
- **velikostDomecku:** The size of the house.
- **barva:** The color of the house.
The code then creates a new Turtle object and sets its properties, such as shape, speed, and pen size. The code then uses a for loop to draw 20 houses. For each house, the code generates special color and size, and then calls the domecek function to draw the house. The application draws a village with 20 houses of different sizes and colors. Houses are arranged in a spiral shape

![](https://github.com/hrosicka/PythonBasicsTurtle/blob/master/doc/CrazyVillage.png)

---

## vesnice.py
It provides instructions on how to use the Levitating Village application, which draws a levitating village using the Turtle graphics library.
### Application Window
The application window displays a village with houses of different sizes and colors levitating in a black space. The title of the window is "Levitating Village".
### How It Works
The application uses the Turtle graphics library to draw the village. The code defines a function called domecek that draws a house. The function takes three arguments:
- **t:** The Turtle object that will be used to draw the house.
- **velikost:** The size of the house.
- **barva:** The color of the house.
The code then creates a new Turtle object and sets its properties, such as shape, speed, and pen size. The code then uses a for loop to draw 100 houses. For each house, the code generates a random position, color, and size, and then calls the domecek function to draw the house.

![](https://github.com/hrosicka/PythonBasicsTurtle/blob/master/doc/LevitatingVillage.png)

---

## pavucina.py
It provides instructions on how to use the Colorful Spider Web application, which draws a colorful spider web using the Turtle graphics library.
### Application Window
The application window displays a colorful spider web with intricate patterns. The background of the window is black, and the title of the window is "Spider Web".
### How It Works
The application uses the Turtle graphics library to draw the spider web. The code uses a for loop to draw 100 nodes, each of which consists of 3 loops. Each loop draws 4 edges, and the color of each edge is randomly generated. The distance between nodes increases as the web expands, creating a spiral pattern. The background of the window is black.

![](https://github.com/hrosicka/PythonBasicsTurtle/blob/master/doc/SpiderWeb.png)

---

## kytice.py
It provides instructions on how to use the Flower application, which draws a flower using the Turtle graphics library.
### Application Window
The application window displays a flower with colorful petals. The background of the window is black, and the title of the window is "Flower".
### How It Works
The application uses the Turtle graphics library to draw the flower. The code defines two functions:
- **okvetniListky(t, s, count, col1, col2):** This function draws a layer of petals. It takes five arguments:
  - **t:** The Turtle object that will be used to draw the petals.
  - **s:** The size of the petals.
  - **count:** The number of petals in the layer.
  - **col1:** The fill color of the petals.
  - **col2:** The outline color of the petals.
- **kvetina(t, s, col1, col2, col3, col4):** This function draws a flower. It takes six arguments:
  - **t:** The Turtle object that will be used to draw the flower.
  - **s:** The size of the flower.
  - **col1:** The color of the outer petals.
  - **col2:** The alternate color of the outer petals.
  - **col3:** The color of the middle petals.
  - **col4:** The color of the center of the flower.
The code then creates a new Turtle object and sets its properties, such as speed and pen size. The code then calls the kvetina function to draw the flower.

#### examples
![](https://github.com/hrosicka/PythonBasicsTurtle/blob/master/doc/Flower.png)
![](https://github.com/hrosicka/PythonBasicsTurtle/blob/master/doc/Flower2.png)
![](https://github.com/hrosicka/PythonBasicsTurtle/blob/master/doc/Flower3.png)

---

## fialovyornament.py
![](https://github.com/hrosicka/PythonBasicsTurtle/blob/master/doc/FialovyOrnament.png)

---

## modrozelenyornament.py
![](https://github.com/hrosicka/PythonBasicsTurtle/blob/master/doc/ModrozelenyOrnament.png)

---

## Author
Lovingly crafted by [Hanka Robovska](https://github.com/hrosicka) 👩‍🔬

---

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details. Free to use, modify, and distribute as needed.
