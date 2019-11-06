# JUSTIN GLUSKA
# ECS102 FINAL PROJECT
# ROULETTE GAME

from graphics import *
import math
win = GraphWin("Roulette Wheel", 1000, 1000)
win.setCoords(-90, -90, 90, 90)
aCircle = Circle(Point(0,0), 90)
aCircle.draw(win)
#aLine = Line(Point(0,0), Point(90*math.cos(0),90*math.sin(0)))
#aLine.draw(win)
#aLine = Line(Point(0,0), Point(90*math.cos(0.523599),90*math.sin(0.523599)))
#aLine.draw(win)
for x in range(38):
    temp = (math.pi*x)/180
    aLine = Line(Point(0,0), Point(90*math.cos(temp),90*math.sin(temp)))
    aLine.draw(win)