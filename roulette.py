# JUSTIN GLUSKA
# ECS102 FINAL PROJECT
# ROULETTE GAME

### IMPORT GRAPHICS AND MATH
from graphics import *
import math
import time
import random
### SET WHEEL WINDOW CONDITIONS
wheel = GraphWin("Roulette Wheel", 750, 750)
wheel.setCoords(-90, -90, 90, 90)
wheel.setBackground("NavyBlue")
#################################
### CREATE ROULETTE WHEEL
def createWheel():
    rouletteCircle = Circle(Point(0,0), 90)
    rouletteCircle.draw(wheel)
    for x in range(38):
        temp = (math.pi*x)/180
        temp2 = (math.pi*(x+1))/180
        aLine = Polygon(Point(0,0), Point(90*math.cos(temp*9.4736842105),90*math.sin(temp*9.4736842105)), Point(90*math.cos(temp2*9.4736842105),90*math.sin(temp2*9.4736842105)))
        if x == 9:
            aLine.setFill("green")
        elif x == 28:
            aLine.setFill("green")
        elif x%2 == 0:
            aLine.setFill("black")
        elif x%2 == 1:
            aLine.setFill("red")
        aLine.draw(wheel)
    bigBlockCircle = Circle(Point(0,0), 55)
    bigBlockCircle.draw(wheel)
    bigBlockCircle.setFill("Dark Slate Gray")
    blockCircle = Circle(Point(0,0), 50)
    blockCircle.draw(wheel)
    blockCircle.setFill("maroon")
createWheel()
#############################################
### CREATE CONTROL WINDOW
#############################################
otherWin = GraphWin("Bet Controls", 800, 400)
otherWin.setBackground("grey")

#############################################
### DRAW POINTS ON WHEEL
#############################################
numberList = ["21","6","18","31","19","8","12","29","25","10","27","00","1","13","36","24","3","15","34","22","5","17","32","20","7","11","30","26","9","28","0","2","14","35","23","4","16","23"]
def createLabels():
    for x in range(38):
        temp = ((math.pi*x)/180)-5
        text = Text(Point((83*(math.cos(temp*9.4736842105))),(83*math.sin(temp*9.4736842105))), numberList[x])
        text.setSize(18)
        text.setTextColor("white")
        text.draw(wheel)
#############################################
##### CREATE BALL ON GREEN 0
#############################################
def spinBall():
    ball = Circle(Point(63.4,5.5), 3)
    ball.setFill("orange")
    ball.draw(wheel)
    spinCount = random.randrange(38,190)
    print(spinCount)
    k = 0
    final = 0
    for i in range(1,spinCount):
        time.sleep(.05)
        ball.move(-1*math.sin(0.165346981767014*i)*10.5,math.cos(0.165346981767014*i)*10.5)
    if spinCount+20 > 38:
        k = spinCount
        while k+20 > 38:
            k = k - 38
    slot0.setText(numberList[k+20])
    ball.undraw()
#############################################    
##### PROGRAM RUN #####
#############################################
createWheel()
createLabels()

slot0 = Text(Point(0,0), "make sure to eat your vegetables")
slot0.setSize(22)
slot0.setTextColor("orange")
slot0.draw(wheel)
while True:
    click = otherWin.getMouse()
    spinBall()