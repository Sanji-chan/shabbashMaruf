from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys, math
import numpy as np

import random

# utility functions
def addvertex(x, y):
    glVertex2f(x, y)


def addcolour(hex_code):
    red = hex_code[:2]
    green = hex_code[2:4]
    blue = hex_code[4:]

    r = int(red, 16)
    g = int(green, 16)
    b = int(blue, 16)

    glColor3f(r / 255, g / 255, b / 255)


def drawPixel(x, y):
    glBegin(GL_POINTS)
    addvertex(x, y)
    glEnd()

def drawLine(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    n_x = -1
    if x0 < x1 :
        n_x=1
    n_y = -1
    if y0 < y1:
        n_y=1
    d = dx - dy
    while True:
        drawPixel(x0, y0)
        if x0 == x1 and y0 == y1:
            break
        incr = 2 * d
        if incr > -dy:
            d -= dy
            x0 += n_x
        if incr < dx:
            d += dx
            y0 += n_y
def draw8way(x,y,c_x,c_y):
    drawPixel( x+c_x , y+c_y)
    drawPixel(-x+c_x, y+c_y)
    drawPixel( y+c_x , x+c_y)
    drawPixel(-y+c_x,-x+c_y)
    drawLine(-x+c_x, y+c_y, x+c_x, y+c_y)
    drawLine(-y+c_x, x+c_y, y+c_x, x+c_y)
    drawLine(-x+c_x,-y+c_y, x+c_x,-y+c_y)
    drawLine(-y+c_x,-x+c_y, y+c_x,-x+c_y)



def drawCircle(r, c_x, c_y):
    x = r
    y = 0
    d = 5 - (4 * r)

    red = 252/255
    green = 215/255
    blue = 64/255

    while (y <= x):

        glColor3f(red, green, blue)

        draw8way(x, y, c_x, c_y)
        if (d < 0):
            d += 4 * ((2 * y) + 3)

        else:
            d += 4 * ((-2 * x) + (2 * y) + 5)
            x -= 1

        y += 1



# numbers
def zero(x, y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()


def one(x, y):
    glBegin(GL_LINES)
    addvertex(x + 25, y)  # right
    addvertex(x + 25, y - 50)
    glEnd()


def two(x, y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y - 25)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 25)
    glEnd()


def three(x, y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()


def four(x, y):
    glBegin(GL_LINES)
    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y)  # left bar
    addvertex(x, y - 25)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()


def five(x, y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 25)

    addvertex(x + 25, y - 25)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()


def six(x, y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y - 25)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()


def seven(x, y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()


def eight(x, y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()


def nine(x, y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 25)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()


def display_score(text):
    current_x = -270
    current_y = 410
    space = 40
    addcolour("383838")

    for i in text:
        if i == "0":
            zero(current_x, current_y)
            current_x += space
        elif i == "1":
            current_x -= 25
            one(current_x, current_y)
            current_x += space
        elif i == "2":
            two(current_x, current_y)
            current_x += space
        elif i == "3":
            three(current_x, current_y)
            current_x += space
        elif i == "4":
            four(current_x, current_y)
            current_x += space
        elif i == "5":
            five(current_x, current_y)
            current_x += space
        elif i == "6":
            six(current_x, current_y)
            current_x += space
        elif i == "7":
            seven(current_x, current_y)
            current_x += space
        elif i == "8":
            eight(current_x, current_y)
            current_x += space
        elif i == "9":
            nine(current_x, current_y)
            current_x += space

# characters
def a(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()

def b(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 23, y)

    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 23, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()
def c(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)
    glEnd()

def d(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 23, y)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 23, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()

def e(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)
    glEnd()

def f(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)
    glEnd()

def g(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x + 25, y-25)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()

def h(x,y):
    glBegin(GL_LINES)
    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()

def I(x,y):
    glBegin(GL_LINES)
    addvertex(x + 25, y)  # right
    addvertex(x + 25, y - 50)
    glEnd()

def j(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y-40)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()


def k(x,y):
    glBegin(GL_LINES)
    addvertex(x, y-25)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 25)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)
    glEnd()


def l(x,y):
    glBegin(GL_LINES)
    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)
    glEnd()

def m(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 12.5, y-25)

    addvertex(x+12.5, y - 25)  # mid bar
    addvertex(x + 25, y)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()

def n(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y-50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()

def o(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()

def p(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 25)
    glEnd()

def q(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x+15, y - 30)  # mid bar
    addvertex(x + 30, y - 50)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()

def r(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 25)

    addvertex(x + 15.5, y-25)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()

def s(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x, y - 25)  # mid bar
    addvertex(x + 25, y - 25)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 25)

    addvertex(x + 25, y-25)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()

def t(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x + 12.5, y)  # right bar
    addvertex(x + 12.5, y - 50)
    glEnd()

def u(x,y):
    glBegin(GL_LINES)
    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)

    addvertex(x, y)  # left bar
    addvertex(x, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 25, y - 50)
    glEnd()

def v(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # left bar
    addvertex(x+12.5, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 12.5, y - 50)
    glEnd()

def w(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # left bar
    addvertex(x+6.25, y - 50)

    addvertex(x + 12.5, y)  # right bar
    addvertex(x + 6.25, y - 50)

    addvertex(x+12.5, y)  # left bar
    addvertex(x+18.75, y - 50)

    addvertex(x + 25, y)  # right bar
    addvertex(x + 18.75, y - 50)

    glEnd()

def x(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)
    addvertex(x+25, y - 50)

    addvertex(x + 25, y)
    addvertex(x, y - 50)
    glEnd()


def y(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # left bar
    addvertex(x+12.5, y - 25)

    addvertex(x + 25, y)  # right bar
    addvertex(x+12.5, y - 25)

    addvertex(x + 12.5, y-25)  # right bar
    addvertex(x + 12.5, y - 50)
    glEnd()


def z(x,y):
    glBegin(GL_LINES)
    addvertex(x, y)  # top bar
    addvertex(x + 25, y)

    addvertex(x + 25, y)
    addvertex(x, y - 50)

    addvertex(x, y - 50)  # bottom bar
    addvertex(x + 25, y - 50)
    glEnd()

def co(x, y):
    glPointSize(4)
    glBegin(GL_POINTS)
    addvertex(x+25, y-10)
    addvertex(x+25, y-40)
    glEnd()
    glPointSize(1)


def display_name(name, x, y):
    current_x = x
    current_y = y
    space = 40
    addcolour("383838")

    for i in name.upper():
        if i == "A":
            a(current_x, current_y)
            current_x += space
        elif i == "B":
            b(current_x, current_y)
            current_x += space
        elif i == "C":
            c(current_x, current_y)
            current_x += space
        elif i == "D":
            d(current_x, current_y)
            current_x += space
        elif i == "E":
            e(current_x, current_y)
            current_x += space
        elif i == "F":
            f(current_x, current_y)
            current_x += space
        elif i == "G":
            g(current_x, current_y)
            current_x += space
        elif i == "H":
            h(current_x, current_y)
            current_x += space
        elif i == "I":
            current_x -= 25
            I(current_x, current_y)
            current_x += space
        elif i == "J":
            j(current_x, current_y)
            current_x += space
        elif i == "K":
            k(current_x, current_y)
            current_x += space
        elif i == "L":
            l(current_x, current_y)
            current_x += space
        elif i == "M":
            m(current_x, current_y)
            current_x += space
        elif i == "N":
            n(current_x, current_y)
            current_x += space
        elif i == "O":
            o(current_x, current_y)
            current_x += space
        elif i == "P":
            p(current_x, current_y)
            current_x += space
        elif i == "Q":
            q(current_x, current_y)
            current_x += space
        elif i == "R":
            r(current_x, current_y)
            current_x += space
        elif i == "S":
            s(current_x, current_y)
            current_x += space
        elif i == "T":
            t(current_x, current_y)
            current_x += space
        elif i == "U":
            u(current_x, current_y)
            current_x += space
        elif i == "V":
            v(current_x, current_y)
            current_x += space
        elif i == "W":
            w(current_x, current_y)
            current_x += space
        elif i == "X":
            x(current_x, current_y)
            current_x += space
        elif i == "Y":
            y(current_x, current_y)
            current_x += space
        elif i == "Z":
            z(current_x, current_y)
            current_x += space
        elif i == ":":
            current_x -= 25
            co(current_x, current_y)
            current_x += space

class BG():
    def __init__(self):
        self.coin_coordinates = []
        self.n = 0

    def sky(self):
        glBegin(GL_QUADS)
        addcolour("09E9FE") # darker left top colour
        glVertex3f(-600, 800, 0)
        addcolour("8DE1EA") # whiter sky near ground
        glVertex3f(-600, -300, 0)
        glVertex3f(600, -300, 0)
        addcolour("EFEA80")  # yellower sky near sun
        glVertex3f(600, 800, 0)
        glEnd()

    def ground(self):
        glBegin(GL_QUADS)
        addcolour("2E8C16")
        glVertex3f(-600, -300, 0)
        addcolour("54C424")
        glVertex3f(-600, -600, 0)
        glVertex3f(600, -600, 0)
        glVertex3f(600, -300, 0)
        glEnd()

    def mountain(self):
        glBegin(GL_TRIANGLES)
        addcolour("3C1C0A") # mountain no. 1
        glVertex3f(-470, -550, 0)
        addcolour("B68E61")
        glVertex3f(-200, 300, 0)
        addcolour("914500")
        glVertex3f(200, -500, 0)

        glColor3f(0, 0.1, 0.4)    # mountain no. 2
        glVertex3f(-200, -550, 0)
        addcolour("008100")
        glVertex3f(30, 200, 0.4)
        glColor3f(0, 0.7, 0)
        glVertex3f(300, -500, 0)
        glEnd()

    # sun
    def sun(self, r, c_x, c_y):
        r = int(r)
        c_x = int(c_x)
        c_y = int(c_y)
        angle = 0
        r2 = r / 2

        glPointSize(3)

        drawCircle(r, c_x, c_y)

        k = 0

        for i in range(0):
            x = r2 * math.cos(angle)
            y = r2 * math.sin(angle)

            drawCircle(r2, x + c_x, y + c_y)
            angle += k

    def drawRay(self, r, c_x, c_y):  # ADD AFTER drawCircle
        red = 252 / 255
        green = 215 / 255
        blue = 64 / 255

        glColor3f(red, green, blue)
        drawLine(c_x - r, c_y, c_x + r, c_y)
        drawLine(c_x, c_y - r, c_x, c_y + r)
        drawLine(c_x - r, c_y - r, c_x + r, c_y + r)
        drawLine(c_x - r, c_y + r, c_x + r, c_y - r)
        drawLine(c_x - r // 2, c_y - r // 2, c_x + r // 2, c_y + r // 2)
        drawLine(c_x - r // 2, c_y + r // 2, c_x + r // 2, c_y - r // 2)

    def display_bg(self):
        self.sky()
        self.mountain()
        self.ground()
        self.sun(50, 500, 400)
        self.drawRay(50 + 10, 500, 400)

    def generate_coins(self):
        if self.n < 6:
            a = random.randrange(-500, 500, 100)
            b = random.randrange(-250, 40, 50)
            if [a, b] not in self.coin_coordinates:
                self.coin_coordinates.append([a,b])
            self.n +=1

    def show_coins(self):
        glPointSize(40)
        addcolour("EEC401")
        if len(self.coin_coordinates)!= 0:
            for item in self.coin_coordinates:
                if item != None:
                    drawPixel(item[0], item[1])
        glPointSize(1)

    def remove_coin(self, r_list):
        temp = []
        for c in range(len(self.coin_coordinates)):
            if c not in r_list:
                temp.append(self.coin_coordinates[c])
        self.n -= len(r_list)
        self.coin_coordinates = temp

class player():
    def __init__(self):
        self.score = 0
        self.top_left = [-575, -130]
        self.bottom_right = [-530, -300]

    def display_player(self):
        genji = np.array([[-580, -250], [-580, -200], [-530, -200], [-530, -250]])

        body = np.array([[-570, -210], [-570, -200], [-540, -200], [-540, -210],  # neck
                         [-600, -250], [-600, -200], [-580, -200], [-580, -250],  # left arm
                         [-530, -250], [-530, -200], [-510, -200], [-510, -250],  # right arm
                         [-575, -200], [-575, -150], [-535, -150], [-535, -200],  # head
                         [-535, -175], [-535, -165], [-530, -165], [-530, -175]])  # nose

        lungi = np.array([[-580, -300], [-580, -250], [-530, -250], [-530, -300]])

        hat = np.array([[-575, -150], [-575, -130], [-535, -130], [-535, -150],  # main hat
                        [-535, -150], [-535, -145], [-525, -145], [-525, -150]])  # front bit

        t = np.array([x, y])

        if (-600 + t[0]) < -600:
            t[0] = 0
        if (-510 + t[0]) > 600:
            t[0] = 1110

        glBegin(GL_QUADS)

        for i in range(4):
            addcolour("e2e5de")
            g = np.add(genji[i], t)
            addvertex(g[0], g[1])

        for i in range(20):
            addcolour("a67556")
            b = np.add(body[i], t)
            addvertex(b[0], b[1])

        for i in range(4):
            addcolour("0008a3")
            l = np.add(lungi[i], t)
            if i == 3:
                self.bottom_right = l
            addvertex(l[0], l[1])

        for i in range(8):
            addcolour("b90e0a")
            h = np.add(hat[i], t)
            if i == 1:
                self.top_left = h
            addvertex(h[0], h[1])

        glEnd()

    def update_score(self,n):
        self.score += 10*n
def catch_coin(tl, br, coin_c):
    remove = []

    for i, item in enumerate(coin_c):
        for item_xRange in range(item[0]-20, item[0]+20):
            if item_xRange >= tl[0] and item_xRange <= br[0]:
                for item_yRange in range(item[1] - 20, item[1] + 20):
                    if item_yRange <= tl[1] and item_yRange >= br[1]:
                        if i not in remove:
                            remove.append(i)
    return remove


# initialization
WIDTH = 1200  # display size
HEIGHT = 1000

name = input("Enter name: ")
if len(name) > 5:
    name = "Name:" + name[0:5]
else:
    name = "Name:" + name

x = 0
y = 0
velocity = 10  # change to alter horizontal (left to right) movement
height = 170  # change to alter max jumping height

bg = BG()
p = player()

def initialize():
    glClearColor(1, 1, 1, 0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-WIDTH / 2, WIDTH / 2, -HEIGHT / 2, HEIGHT / 2)

def key(k, a, b):
    global x, velocity
    glutSetKeyRepeat(GLUT_KEY_REPEAT_ON)
    if k == GLUT_KEY_LEFT:
        x -= velocity
        glutPostRedisplay()

    elif k == GLUT_KEY_RIGHT:
        x += velocity
        glutPostRedisplay()
def jump(k, a, b):
    global y, height
    glutSetKeyRepeat(GLUT_KEY_REPEAT_OFF)
    if k == b" ":
        y += height
        glutPostRedisplay()

def jump_down(k, a, b):
    global y, height
    glutSetKeyRepeat(GLUT_KEY_REPEAT_OFF)
    if k == b" ":
        y -= height
        glutPostRedisplay()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT)

    bg.display_bg() # show background
    # sun(50, 500, 400)

    if (random.randint(0, 250) < 30): # generate coins for game at random
        bg.generate_coins()

    bg.show_coins() # show coins
    p.display_player()  # show player position

    remove_list = catch_coin(p.top_left, p.bottom_right, bg.coin_coordinates) #check to see, if player catches the coin

    if len(remove_list) != 0: # remove all caught coins and update score
        bg.remove_coin(remove_list)
        p.update_score(len(remove_list))
        print("Your score is: ", p.score)

    display_name(name, -500, 480)
    display_name("score:", -500, 410)
    display_score(str(p.score)) #show score

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WIDTH, HEIGHT)  # window size
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Shabbash Maruf")  # window name

    # initialization
    initialize()

    glutDisplayFunc(showScreen)
    glutKeyboardFunc(jump)
    glutKeyboardUpFunc(jump_down)
    glutSpecialFunc(key)
    glutMainLoop()

if __name__ == "__main__":
    main()
