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
###
createWheel()
#############################################
### CREATE BET CONTROL & COMMAND WINDOW
#############################################
otherWin = GraphWin("Bet Controls", 750, 750)
otherWin.setBackground("Teal")
otherWin.setCoords(0,0,1000,1000)
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
        while k+20 >= 38:
            k = k - 38
    ball.setFill("Light Gray")
    slot0.setText(numberList[k+20])
    #ball.undraw()
#############################################
##### MAKE BETTING WHEEL
#############################################
splitter = Line(Point(0,500), Point(1000,500))
splitter.draw(otherWin)
#for i in range(13):
#    line = Line(Point(i*76.9,1000), Point(i*76.9,500))
#    line.draw(otherWin)
#for i in range(5):
#    line = Line(Point(0,500+(i*100)), Point(1000,500+(i*100)))
#    line.draw(otherWin)
a12 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 100]
b12 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 100]
c12 = []
for i in range(13):
    aRectangle = Rectangle(Point(i*76.9,1000), Point((i+1)*76.9,900))
    aRectangle.draw(otherWin)
    if a12[i] == 3 or a12[i] == 9 or a12[i] == 12 or a12[i] == 18 or a12[i] == 21 or a12[i] == 27 or a12[i] == 30 or a12[i] == 36:
        aRectangle.setFill("red")
    elif a12[i] == 6 or a12[i] == 15 or a12[i] == 24 or a12[i] == 33:
        aRectangle.setFill("black")
for i in range(13):
    aRectangle = Rectangle(Point(i*76.9,900), Point((i+1)*76.9,800))
    aRectangle.draw(otherWin)
    if b12[i] == 2 or b12[i] == 8 or b12[i] == 11 or b12[i] == 17 or b12[i] == 20 or b12[i] == 26 or b12[i] == 29 or b12[i] == 35:
        aRectangle.setFill("black")
for i in range(13):
    aRectangle = Rectangle(Point(i*76.9,800), Point((i+1)*76.9,700))
    aRectangle.draw(otherWin)
aLine = Line(Point(923.076,700), Point(923.076,500))
aLine.draw(otherWin)
for i in range(1,4):
    aLine = Line(Point(307.692*i, 700), Point(307.692*i, 600))
    aLine.draw(otherWin)
for i in range(1,9):
    aLine = Line(Point(115.3845*i,600), Point(115.3845*i, 500))
    aLine.draw(otherWin)
aLine = Line(Point(0,600), Point(1000,600))
aLine.draw(otherWin)
#def drawBettingColors:
def drawBettingNumbers:
    for i in a12:
        message = Text(Point((50+25*i)-77.5,950), i)
        message.setFill("white")
        message.setStyle("bold")
        message.setSize(18)
        message.draw(otherWin)
#def drawBettingMisc:
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