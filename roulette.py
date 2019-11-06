# JUSTIN GLUSKA
# ECS102 FINAL PROJECT
# ROULETTE GAME

from graphics import *

win = GraphWin("Roulette Wheel", 1000, 1000)
win.setCoords(-90, -90, 90, 90)
aCircle = Circle(Point(0,0), 90)
aCircle.draw(win)
aLine = Line(Point(0,180), Point(0,-180))
aLine.draw(win)
aLine = Line(Point(9.47,180-9.47), Point(-9.47*2,-180+(9.47*2)))
aLine.draw(win)