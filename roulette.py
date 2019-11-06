# JUSTIN GLUSKA
# ECS102 FINAL PROJECT
# ROULETTE GAME

### IMPORT GRAPHICS AND MATH
from graphics import *
import math
### SET WHEEL WINDOW CONDITIONS
wheel = GraphWin("Roulette Wheel", 650, 650)
wheel.setCoords(-90, -90, 90, 90)
wheel.setBackground("lightblue")
#################################
### CREATE ROULETTE WHEEL
rouletteCircle = Circle(Point(0,0), 90)
rouletteCircle.draw(wheel)
for x in range(38):
    temp = (math.pi*x)/180
    temp2 = (math.pi*(x+1))/180
    aLine = Polygon(Point(0,0), Point(90*math.cos(temp*9.4736842105),90*math.sin(temp*9.4736842105)), Point(90*math.cos(temp2*9.4736842105),90*math.sin(temp2*9.4736842105)))
    if x%2 == 0:
        aLine.setFill("red")
    elif x%2 == 1:
        aLine.setFill("black")
    aLine.draw(wheel)
### CREATE CONTROL WINDOW
otherWin = GraphWin("Bet Controls", 600, 300)
otherWin.setBackground("grey")
