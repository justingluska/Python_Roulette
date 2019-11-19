# JUSTIN GLUSKA
# ECS102 Final
# Section M5
# Due December 5th, 2019
# Roulette Board Game

### IMPORT GRAPHICS AND MATH
from graphics import *
import math
import time
import random
############################

###############
username = ""
money = 20
winningNumber = 100
a12 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 100]
b12 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 100]
c12 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 100]
###############
classList = ["num0", "num1", "num2"]
class NumberInfo:
    def __init__(self, number, color, oddEven, row, third, half):
        self.number = number
        self.color = color
        self.oddEven = oddEven
        self.row = row
        self.third = third
        self.half = half
        
    def displayColor(self):
        print(self.color)
        
                #(num, color, odEv , row, trd, hlf)
num1 = NumberInfo("1", "red", "odd", "3", "1", "1")
num2 = NumberInfo("2", "black", "even", "2", "1", "1")
num3 = NumberInfo("3", "red", "odd", "1", "1", "1")
###############
# Draw the main labels between login, wheel, and bet

def login():
    # Login Screen Window
    loginScreen = GraphWin("Login Screen", 400, 400)
    loginScreen.setCoords(0,0,400,300)
    loginScreen.setBackground("LightGrey")
    # Name Input Box
    inputBox = Entry(Point(200,200), 15)
    inputBox.draw(loginScreen)
    # Login Button
    confirmLogin = Rectangle(Point(100,50), Point(300,150))
    confirmLogin.setFill("Crimson")
    confirmLogin.draw(loginScreen)
    confirmLoginText = Text(Point(200,100), "LOGIN")
    confirmLoginText.setFill("white")
    confirmLoginText.setSize(26)
    confirmLoginText.draw(loginScreen)
    # Login Button Label
    loginText = Text(Point(200,250), "Welcome To Roulette!\nEnter a username to get started!")
    loginText.setFill("crimson")
    loginText.setStyle("bold")
    loginText.setSize(18)
    loginText.draw(loginScreen)
    
    ##################
    nameEnter = False
    while nameEnter == False:
        loginClick = loginScreen.getMouse()
        if loginClick.getX() >= 100 and loginClick.getX() <= 300:
            if loginClick.getY() >= 50 and loginClick.getY() <= 150:
                if len(inputBox.getText()) > 0:
                    username = inputBox.getText()
                    infile = open("playerinfo.txt", "r")
                    createNew = 0
                    userList = []
                    for line in infile:
                        line.strip('\n')
                        userList.append(str(line))
                    for line in userList:
                        print(userList)
                        if createNew == 0:        
                            if username in line and createNew == 0:
                                print(line)
                                nameEnter = True
                                loginScreen.close()
                                break
                            else:
                                createNew = 1
                                break
                    if createNew == 1:
                        tempSet = username + ",1000"
                        money = 1000
                        outfile = open("playerinfo.txt", "a")
                        outfile.write("\n")
                        outfile.write(tempSet)
                        outfile.close()
                        infile.close()
                        nameEnter = True
                        loginScreen.close()

###############

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
##### DISPLAY AMOUNT OF MONEY USER HAS ######
moneyLabel = Text(Point(500,135), "You Have: $")
moneyDisplay = Text(Point(500,100), money)

def displayInitialMoney():
    moneyLabel.setStyle("bold")
    moneyLabel.setFill("white")
    moneyLabel.draw(otherWin)
    moneyDisplay.setFill("orange")
    moneyDisplay.setStyle("bold")
    moneyDisplay.setSize(36)
    moneyDisplay.draw(otherWin)
    
def updateMoney():
    moneyDisplay.setText(money)

# def updateMoneyFile():
#      infile = open("playerinfo.txt", "r")
#      tempList = []
#      #outfile = open("playerinfo.txt", "w")
#      for name in infile:
#          tempVar = name.split()
#          tempList = tempList + tempVar
#      infile.close()
#      print(tempList)
#      #outfile.close()
# updateMoneyFile()
#############################################
def convertBetId(ID):
    #return resultID and use that in runBets
    ID = str(ID)
    resultId = -1
    if ID == "0" or ID == "00":
        print("0 or 00")
        return 0
    elif ID == "ROW1":
        return 41
    elif ID == "ROW2":
        return 42
    elif ID == "ROW3":
        return 43
    else:
        for x in range(1,37,1):
            if ID == str(x):
                return x # returns 1 to 36
### Bet functions ###
def runBets(winningNumber, betAmount):
    # add if function to check if boxes both have stuff inside them
    betId = betIdBox.getText()
    betAmount = int(betBox.getText())
    global money
    #####
    # bets for rows working
    if 1 <= convertBetId(betId) <= 36:
        if int(winningNumber) == convertBetId(betId):
            money = money + (betAmount * 36)
            updateMoney()
    if convertBetId(betId) == 41:
        if int(winningNumber)%3 == 0 and not winningNumber == "0" and not winningNumber == "00":
            money = money + (betAmount * 2)
            updateMoney()
        ## ROW1
        
    #winningNumberConvert = "num", winningNumber, ".row"
    #print(winningNumberConvert)
    #if newBetId == winningNumberConvert:
    #    print("cvt")
    # Single Digit Bets
#     for x in range(1,37,1):
#         if betId == str(x):
#             if betId == str(winningNumber):
#                 winTemp = "WIN ON SINGLE: ", winningNumber
#                 money = money + (betAmount * 36)
#                 updateMoney()
#                 #updateWin()
#                 #updateLoss()
#     # 0 or 00 Bets (same concept as single)
#     if betId == str(winningNumber):
#         winTemp = "WIN ON SINGLE: ", winningNumber
#         money = money + (betAmount * 36)
#         updateMoney()
        # ROW3
        #classList[winningNumber]
    #print(classList[winningNumber].row)
    #if betId == classList[winningNumber].row:
    #    winTemp = "WIN ON SINGLE: ", winningNumber
    #    money = money + (betAmount * 36)
    #    updateMoney()
#############################################
#def updateWin():
#def updateLoss():
def spinBall():
    betAmount = int(betBox.getText())
    global money
    if betAmount <= money:
        betId = betIdBox.getText()
        convertBetId(betId)
        money = money - betAmount
        moneyDisplay.setText(money)
        ball = Circle(Point(63.4,5.5), 3)
        ballColors = ["orange", "red", "green", "yellow", "Spring Green", "pink", "grey"]
        ballColorSelect = random.randrange(6)
        ball.setFill(ballColors[ballColorSelect])
        ball.draw(wheel)
        #30 31 lands on 1
        # actual wheel (38,380)
        spinCount = random.randrange(30,31)
        print(spinCount)
        k = 0
        final = 0
        for i in range(1,spinCount):
            j = i/spinCount
            if j >= .95:
                time.sleep((j/1.5)/2)
            elif j >= .90:
                time.sleep((j/3)/2)
            elif j >= .80:
                time.sleep((j/6)/2)
            elif j >= .70:
                time.sleep((j/12)/2)
            elif j < 70:
                time.sleep(.025)
            elif j < 55:
                time.sleep(.010)
            elif j < 35:
                time.sleep(.005)
            ball.move(-1*math.sin(0.165346981767014*i)*10.5,math.cos(0.165346981767014*i)*10.5)
        if spinCount+20 > 38:
            k = spinCount
            while k+20 >= 38:
                k = k - 38
        ball.setFill("Light Gray")
        winningNumber = numberList[k+20]
        runBets(winningNumber, betAmount)
        console.setText(numberList[k+20])
        #ball.undraw()
    elif betAmount > money:
        console.setText("Error! You can't bet more than you have")
#############################################

#############################################
def drawBettingWheel():
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
def drawBottomRow():
    bottomValues = ["1-18", "EVEN", "", "0", "00", "", "ODD", "19-36"]
    for i in range(8):
        bottomRow = Rectangle(Point(115.3846153847*i,500), Point(115.3846153847*(i+1),600))
        bottomRow.draw(otherWin)
        bottomRow.setFill("gray")
    # pos1
    bottomPos1 = Text(Point(57.6923076924,550), bottomValues[0])
    bottomPos1.setFill("white")
    bottomPos1.setStyle("bold")
    bottomPos1.setSize(18)
    bottomPos1.draw(otherWin)
    # pos2
    bottomPos2 = Text(Point(57.6923076924*3,550), bottomValues[1])
    bottomPos2.setFill("white")
    bottomPos2.setStyle("bold")
    bottomPos2.setSize(18)
    bottomPos2.draw(otherWin)
    # pos3
    bottomPos3 = Rectangle(Point(115.3846153847*2,500), Point(115.3846153847*(2+1),600))
    bottomPos3.setFill("black")
    bottomPos3.draw(otherWin)
    # pos4
    bottomPos4 = Text(Point(57.6923076924*7,550), bottomValues[3])
    bottomPos4.setFill("white")
    bottomPos4.setStyle("bold")
    bottomPos4.setSize(18)
    bottomPos4.draw(otherWin)
    # pos5
    bottomPos5 = Text(Point(57.6923076924*9,550), bottomValues[4])
    bottomPos5.setFill("white")
    bottomPos5.setStyle("bold")
    bottomPos5.setSize(18)
    bottomPos5.draw(otherWin)
    # pos6
    bottomPos6 = Rectangle(Point(115.3846153847*5,500), Point(115.3846153847*(5+1),600))
    bottomPos6.setFill("maroon")
    bottomPos6.draw(otherWin)
    # pos7
    bottomPos7 = Text(Point(57.6923076924*13,550), bottomValues[6])
    bottomPos7.setFill("white")
    bottomPos7.setStyle("bold")
    bottomPos7.setSize(18)
    bottomPos7.draw(otherWin)
    # pos8
    bottomPos8 = Text(Point(57.6923076924*15,550), bottomValues[7])
    bottomPos8.setFill("white")
    bottomPos8.setStyle("bold")
    bottomPos8.setSize(18)
    bottomPos8.draw(otherWin)

#####
def createUserControls():
    # Behind Shadow
    spinButtonShadow = Rectangle(Point(708,67), Point(958,417))
    spinButtonShadow.setFill("Black")
    # Front Facing Button
    spinButton = Rectangle(Point(700,75), Point(950,425))
    spinButton.setFill("Crimson")
    # Front Facing Button Text
    spinButtonText = Text(Point(825,250), "SPIN!")
    spinButtonText.setFill("White")
    spinButtonText.setStyle("bold")
    spinButtonText.setSize(36)
    # Betting Extry Box
    betBoxLabel = Text(Point(500,400), "Enter Bet $:")
    betBoxLabel.setSize(16)
    betBoxLabel.setStyle("bold")
    betBoxLabel.setFill("white")
    betBoxIdLabel = Text(Point(500,300), "Enter Bet ID:")
    betBoxIdLabel.setSize(16)
    betBoxIdLabel.setStyle("bold")
    betBoxIdLabel.setFill("white")
    # Username Display
    usernameDisplay = Text(Point(500,40), "Logged In As: " + username.upper())
    # Draw To Window
    betBoxLabel.draw(otherWin)
    betBox.draw(otherWin)
    betIdBox.draw(otherWin)
    betBoxIdLabel.draw(otherWin)
    usernameDisplay.draw(otherWin)
    spinButtonShadow.draw(otherWin)
    spinButton.draw(otherWin)
    spinButtonText.draw(otherWin)

#####
def drawBettingColors():
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
    
def awardPlayer():
    print()
#############################################    
##### PROGRAM RUN #####
#############################################
login()
### SET WHEEL WINDOW CONDITIONS
wheel = GraphWin("Roulette Wheel", 750, 750)
wheel.setCoords(-90, -90, 90, 90)
wheel.setBackground("Steel Blue")
#############################################
### CREATE BET CONTROL & COMMAND WINDOW
#############################################
otherWin = GraphWin("Bet Controls", 750, 750)
otherWin.setBackground("Teal")
otherWin.setCoords(0,0,1000,1000)

#     console = Text(Point(0,0), "Welcome to Roulette!")
#     console.setSize(22)
#     console.setTextColor("orange")
#     console.draw(wheel)

betBox = Entry(Point(500,350), 15)
betIdBox = Entry(Point(500,250), 15)


createUserControls()
createWheel()
createLabels()
displayInitialMoney()
drawBettingWheel()
drawBottomRow()
drawBettingColors()
##### MAKE BETTING WINDOW
#############################################
splitter = Line(Point(0,500), Point(1000,500))
splitter.draw(otherWin)
console = Text(Point(0,0), "ajaahahhaah")
console.setStyle("bold")
console.setSize(24)
console.setFill("yellow")
console.draw(wheel)        
betId = 0
key = Text(Point(200,275), "BET IDS:\n TYPE ONE TO SELECT\n\n '#' (1-38)\n'0' or '00'\n 'ROW#' (1-3)\n'1to18'\nor '19to36'\n'1to12'\nor '13to24'\nor '25to36'\n'EVEN' or 'ODD'\n'BLACK' or 'RED'")
key.setSize(18)
key.setFill("white")
key.setFace("courier")
key.draw(otherWin)


while True:
    click = otherWin.getMouse()
    x = click.getX()
    y = click.getY()
    if x >= 700 and x <= 950:
        if y >= 75 and y <= 425:
            spinBall()