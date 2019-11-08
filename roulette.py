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
            aLine.setFill("Dark Green")
        elif x == 28:
            aLine.setFill("Dark Green")
        elif x%2 == 0:
            aLine.setFill("black")
        elif x%2 == 1:
            aLine.setFill("maroon")
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
    spinCount = random.randrange(38,304)
    print(spinCount)
    k = 0
    final = 0
    for i in range(1,spinCount):
        j = i/spinCount
        if j >= .90:
            time.sleep((j/3)/2)
        elif j >= .80:
            time.sleep((j/6)/2)
        elif j >= .70:
            time.sleep((j/12)/2)
        elif j < 70:
            time.sleep(.025)
        
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
c12 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 100]
for i in range(3):
    twoOne = Rectangle(Point(76.9230769231*12,700+(i*100)),Point(1000,800+(i*100)))
    twoText = Text(Point(960,750+(i*100)), "2:1")
    twoText.setFill("white")
    twoText.setStyle("bold")
    twoText.setSize(18)
    twoOne.setFill("Slate Gray")
    twoOne.draw(otherWin)
    twoText.draw(otherWin)
for i in range(13):
    aRectangle = Rectangle(Point(i*76.9,1000), Point((i+1)*76.9,900))
    aRectangle.draw(otherWin)
    if a12[i] == 3 or a12[i] == 9 or a12[i] == 12 or a12[i] == 18 or a12[i] == 21 or a12[i] == 27 or a12[i] == 30 or a12[i] == 36:
        aRectangle.setFill("maroon")
    elif a12[i] == 6 or a12[i] == 15 or a12[i] == 24 or a12[i] == 33:
        aRectangle.setFill("black")
for i in range(13):
    aRectangle = Rectangle(Point(i*76.9,900), Point((i+1)*76.9,800))
    aRectangle.draw(otherWin)
    if b12[i] == 2 or b12[i] == 8 or b12[i] == 11 or b12[i] == 17 or b12[i] == 20 or b12[i] == 26 or b12[i] == 29 or b12[i] == 35:
        aRectangle.setFill("black")
    elif b12[i] == 5 or b12[i] == 14 or b12[i] == 23 or b12[i] == 32:
        aRectangle.setFill("maroon")
for i in range(13):
    aRectangle = Rectangle(Point(i*76.9,800), Point((i+1)*76.9,700))
    aRectangle.draw(otherWin)
    if c12[i] == 1 or c12[i] == 7 or c12[i] == 16 or c12[i] == 19 or c12[i] == 25 or c12[i] == 34:
        aRectangle.setFill("maroon")
    elif c12[i] == 4 or c12[i] == 10 or c12[i] == 13 or c12[i] == 22 or c12[i] == 28 or c12[i] == 31:
        aRectangle.setFill("black")
aLine = Line(Point(923.076,700), Point(923.076,500))
aLine.draw(otherWin)
for i in range(0,3):
    aLine = Rectangle(Point(i*307.6923076924,600), Point((i+1)*307.6923076924,700))
    aLine.setFill("Slate Grey")
    aLine.draw(otherWin)
    if i == 0:
        first12a = Text(Point(153.8461538462,650), "1st 12")
        first12a.setStyle("bold")
        first12a.setSize(18)
        first12a.setFill("white")
        first12a.draw(otherWin)
    if i == 1:
        first12b = Text(Point(153.8461538462*3,650), "2nd 12")
        first12b.setStyle("bold")
        first12b.setSize(18)
        first12b.setFill("white")
        first12b.draw(otherWin)
    if i == 2:
        first12c = Text(Point(153.8461538462*5,650), "3rd 12")
        first12c.setStyle("bold")
        first12c.setSize(18)
        first12c.setFill("white")
        first12c.draw(otherWin)
### DRAW RECTANGLE OF NOTHINGNESS
nothing = Rectangle(Point(923.0769230772,500), Point(1000,700))
nothing.setFill("black")
nothing.draw(otherWin)
#########
for i in range(1,9):
    aLine = Line(Point(115.3845*i,600), Point(115.3845*i, 500))
    aLine.draw(otherWin)
aLine = Line(Point(0,600), Point(1000,600))
aLine.draw(otherWin)
#def drawBettingColors:
for i in a12:
    message = Text(Point((50+25*i)-77.5,950), i)
    message.setFill("white")
    message.setStyle("bold")
    message.setSize(18)
    message.draw(otherWin)
for i in b12:
    message = Text(Point((25*i),850), i)
    message.setFill("white")
    message.setStyle("bold")
    message.setSize(18)
    message.draw(otherWin)
for i in c12:
    message = Text(Point(22.5+(25*i),750), i)
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

slot0 = Text(Point(0,0), "zixuan is the best <3")
slot0.setSize(22)
slot0.setTextColor("orange")
slot0.draw(wheel)
while True:
    click = otherWin.getMouse()
    spinBall()