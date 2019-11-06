# JUSTIN GLUSKA
# ECS102 FINAL PROJECT
# ROULETTE GAME

from graphics import *
import math
wheel = GraphWin("Roulette Wheel", 1000, 1000)
wheel.setBackground("lightblue")
otherWin = GraphWin("Bet Controls", 600, 300)
wheel.setCoords(-90, -90, 90, 90)
aCircle = Circle(Point(0,0), 90)
aCircle.draw(wheel)
for x in range(38):
    temp = (math.pi*x)/180
    aLine = Line(Point(0,0), Point(90*math.cos(temp*9.4736842105),90*math.sin(temp*9.4736842105)))
    if x%2 == 0:
        aLine.setFill("red")
    elif x%2 == 1:
        aLine.setFill("black")
    aLine.draw(wheel)
