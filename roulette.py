############################
# roulette.py
# Justin Gluska
# Section M5
# jgluska   @syr.edu
#
# Roulette Board Game
# ECS102 Final

############################
########## IMPORTS #########
from graphics import *
import math
import time
import random

############################
#### STATISTICS OF GAME ####

# (CLOD) - CLASS TO TRACK STAT/PCT%
class Stats:
    # Initializes stats
    def __init__(self, value):
        self.value = value
        
    # Simply returns object value
    def display(self):
        return self.value
    # Increases value by 1
    def increase(self):
        self.value += 1

# (LOOD) - OBJECTS FOR STATS WITH INITIAL CHANCE
statOdd = Stats(0.00)
statEven = Stats(0.00)
statRed = Stats(0.00)
statBlack = Stats(0.00)
statGreen = Stats(0.00)
statTotal = Stats(0.00)

############################
# Draw the main labels between login, wheel, and bet

def login(moneyDisplay):
    # (GW) LOGIN SCREEN WINDOW
    loginScreen = GraphWin("Roulette Login", 400, 400)
    loginScreen.setCoords(0,0,400,300)
    loginScreen.setBackground("Light Sky Blue")
    # Name Input Box
    inputBox = Entry(Point(200,200), 15)
    inputBox.draw(loginScreen)
    # Login Button
    confirmLoginShadow = Rectangle(Point(103,47), Point(303,147))
    confirmLoginShadow.setFill("black")
    confirmLoginShadow.draw(loginScreen)
    confirmLogin = Rectangle(Point(100,50), Point(300,150))
    confirmLogin.setFill("Crimson")
    confirmLogin.draw(loginScreen)
    confirmLoginText = Text(Point(200,100), "LOGIN")
    confirmLoginText.setStyle("bold")
    confirmLoginText.setFill("white")
    confirmLoginText.setSize(26)
    confirmLoginText.draw(loginScreen)
    # Login Button Label
    loginText = Text(Point(200,250), "Welcome To Roulette!\nEnter a username to get started!")
    loginText.setFill("black")
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
                    global username
                    username = inputBox.getText()
                    # (IFL) - GETS MONEY TO START GAME WITH
                    infile = open("playerinfo.txt", "r")
                    for x in infile:
                        global money
                        money = int(x.split()[1])
                    infile.close()
                    loginScreen.close()
                    nameEnter = True
                    updateMoney(moneyDisplay)

#################################
### CREATE ROULETTE WHEEL
                    
def createWheel(wheel):
    rouletteCircle = Circle(Point(0,0), 90)
    rouletteCircle.draw(wheel)
    # Creates the 38 sections of a roulette wheel
    for x in range(38):
        temp = (math.pi*x)/180
        temp2 = (math.pi*(x+1))/180
        aLine = Polygon(Point(0,0), Point(90*math.cos(temp*9.4736842105),90*math.sin(temp*9.4736842105)), Point(90*math.cos(temp2*9.4736842105),90*math.sin(temp2*9.4736842105)))
        # Fills in section color with corresponding values
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
    

#############################################
### DRAW POINTS ON WHEEL

# Creates the individual points on the wheel
numberList = ["21","6","18","31","19","8","12","29","25","10","27","00","1","13","36","24","3","15","34","22","5","17","32","20","7","11","30","26","9","28","0","2","14","35","23","4","16","23"]
def createLabels(wheel):
    for x in range(38):
        temp = ((math.pi*x)/180)-5
        text = Text(Point((83*(math.cos(temp*9.4736842105))),(83*math.sin(temp*9.4736842105))), numberList[x])
        text.setSize(18)
        text.setTextColor("white")
        text.draw(wheel)

# Takes file value and displays it
def displayInitialMoney(moneyLabel, otherWin, moneyDisplay):
    moneyLabel.setStyle("bold")
    moneyLabel.setFill("white")
    moneyLabel.draw(otherWin)
    moneyDisplay.setFill("orange")
    moneyDisplay.setStyle("bold")
    moneyDisplay.setSize(36)
    moneyDisplay.draw(otherWin)
   
# Gets new money and displays it
def updateMoney(moneyDisplay):
    moneyDisplay.setText(money)

def updateMoneyFile():
    # (OFL) - UPDATES MONEY/ERASES TO FILE
    outfile = open("playerinfo.txt", "a")
    toFile = "\n" + str(username) + ", " + str(money)
    outfile.write(toFile)
    outfile.close()

#############################################
####### CONVERT BET TO NUM ID #######
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
    elif ID == "1to12":
        return 44
    elif ID == "13to24":
        return 45
    elif ID == "25to36":
        return 46
    elif ID == "1to18":
        return 47
    elif ID == "19to36":
        return 48
    elif ID == "EVEN":
        return 50
    elif ID == "ODD":
        return 51
    elif ID == "BLACK":
        return 52
    elif ID == "RED":
        return 53
    elif 1<=int(ID)<=36:
        for x in range(1,37,1):
            if ID == str(x):
                return x # returns 1 to 36
    else:
        console.setText("Error! Please enter a valid Bet ID")
        
######################
### Lose Function ####
def playerLost(console):
    console.setText("You Lost! Try again!")
    
#####################
### Bet functions ###
    
def runBets(winningNumber, betAmount, betBox, betIdBox, console, moneyDisplay):
    if betBox.getText().isdigit():
        betAmount = int(betBox.getText())
    else:
        betAmount = 1
        console.setText("Invalid Bet Amount. Set to $1")
    betId = betIdBox.getText()
    global money
    if 1 <= convertBetId(betId) <= 36: # Single Digit 1-36 ID
        if int(winningNumber) == convertBetId(betId):
            money = money + (betAmount * 36)
        else:
            playerLost(console)
    elif convertBetId(betId) == 41: # ROW 1 ID
        if int(winningNumber)%3 == 0 and not winningNumber == "0" and not winningNumber == "00":
            money = money + (betAmount * 3)
        else:
            playerLost(console)
    elif convertBetId(betId) == 42: # ROW 2 ID
        if (int(winningNumber)+1)%3 == 0 and not winningNumber == "0" and not winningNumber == "00":
            money = money + (betAmount * 3)
        else:
            playerLost(console)
    elif convertBetId(betId) == 43: # ROW 3 ID
        if (int(winningNumber)-1)%3 == 0 and not winningNumber == "0" and not winningNumber == "00":
            money = money + (betAmount * 3)
        else:
            playerLost(console)
    elif convertBetId(betId) == 44: # 1 to 12 ID
        array = [1,2,3,4,5,6,7,8,9,10,11,12]
        for x in array:
            if x == int(winningNumber):
                money = money + (betAmount * 3)
    elif convertBetId(betId) == 45: # 13 to 24 ID
        array = [13,14,15,16,17,18,19,20,21,22,23,24]
        for x in array:
            if x == int(winningNumber):
                money = money + (betAmount * 3)
    elif convertBetId(betId) == 46: # 25 to 36 ID
        array = [25,26,27,28,29,30,31,32,33,34,35,36]
        for x in array:
            if x == int(winningNumber):
                money = money + (betAmount * 3)
    elif convertBetId(betId) == 47: # 1 to 18 ID
        array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        for x in array:
            if x == int(winningNumber):
                money = money + (betAmount * 2)
    elif convertBetId(betId) == 48: # 19 to 36 ID
        array = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        for x in array:
            if x == int(winningNumber):
                money = money + (betAmount * 2)
    elif convertBetId(betId) == 50: # Even Bets ID
        if int(winningNumber) % 2 == 0 and not int(winningNumber) == 0 and not winningNumber == "00":
            money = money + (betAmount * 2)
    elif convertBetId(betId) == 51 : # Odd Bets ID
        if int(winningNumber) % 2 == 1 and not int(winningNumber) == 0 and not winningNumber == "00":
            money = money + (betAmount * 2)
    elif convertBetId(betId) == 52: # Black Colors
        array = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        for x in array:
            if x == int(winningNumber):
                money = money + (betAmount * 2)
    elif convertBetId(betId) == 53: # Red Colors
        array = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        for x in array:
            if x == int(winningNumber):
                money = money + (betAmount * 2)
    else:
        console.setText("Error! Please enter a valid Bet ID")
    ##### Cannot make this shorter ^ #####
    didTheyWin(winningNumber, moneyDisplay)

def didTheyWin(winningNumber, moneyDisplay):
    if int(winningNumber) % 2 == 0 and not winningNumber == "0" and not winningNumber == "00":
        statEven.increase()
    if int(winningNumber) % 2 == 1 and not winningNumber == "0" and not winningNumber == "00":
        statOdd.increase()
    if winningNumber == "0" or winningNumber == "00":
        statGreen.increase()
    else:
        blackArray = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        for x in blackArray:
            if x == int(winningNumber):
                statBlack.increase()
        redArray = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        for x in redArray:
            if x == int(winningNumber):
                statRed.increase()
    statTotal.increase()
    updateMoney(moneyDisplay)
#############################################
############### SPIN THE BALL ###############
    
# (FNC) - CHECKS VALID PARAMETERS & SPINS THE BALL
def spinBall(betBox, betIdBox, moneyDisplay, console, wheel, otherWin, oddL, evenL, redL, blackL, greenL):
    # exactly 50 lines of code (excluding comments and spaces)
    if betBox.getText().isdigit():
        betAmount = int(betBox.getText())
    else:
        betAmount = 1
        console.setText("Invalid Bet Amount. Set to $1")
    global money
    if betAmount <= int(money) and not betIdBox == "" and int(money) > 0:
        betId = betIdBox.getText()
        validId = ["0","1","2","3","4","5","6","7","8","9","10",
               "11","12","13","14","15","16","17","18","19",
               "20","21","22","23","24","25","26","27","28",
               "29","30","31","32","33","34","35","36",
               "ROW1", "ROW2", "ROW3", "00", "1to18", "19to36",
               "1to12", "13to24", "25to36", "EVEN", "ODD", "BLACK", "RED"]
        valid = False
        # If the user entered a valid bet id, do this:
        for x in validId:
            if x == betId:
                valid = True
                betBox.undraw()
                betIdBox.undraw()
                convertBetId(betId)
                money = money - betAmount
                moneyDisplay.setText(money)
                betIdLabel = "Bet On: " + str(betId)
                console.setText(betIdLabel)
                ball = Circle(Point(63.4,5.5), 3)
                generateBall(wheel, ball)
                #30 31 lands on 1
                # actual wheel (38,380)
                # (RND) - WILL GENERATE 2-10 RANDOM WHEEL SPINS
                spinCount = random.randrange(76,380)
                k = 0
                final = 0
                # SPEED OF BALL
                # Ball gets slower as closer to end
                k = speedBall(spinCount, ball, k)
                # Sets the winning number after spinning
                winningNumber = numberList[k+20]
                runBets(winningNumber, betAmount, betBox, betIdBox, console, moneyDisplay)
                betBox.draw(otherWin)
                betIdBox.draw(otherWin)
                winningNumberLabel = "Landed on: " + str(winningNumber)
                console.setText(winningNumberLabel)
                updateMoneyFile()
                updateStatLabels(otherWin, oddL, evenL, redL, blackL, greenL)
                if money <= 0:
                    otherWin.close()
                    wheel.close()
                    resetMoney()
            elif betAmount > int(money):
                console.setText("Error! You can't bet more than you have")
        if valid == False:
            console.setText("Error: Enter Valid Bet ID")
####
def generateBall(wheel, ball):
    ballColors = ["orange", "red", "green", "yellow", "Spring Green", "pink", "grey", "cyan", "Dark Orange", "Firebrick", "Fuchsia", "Indigo", "Sienna", "Yellow Green"]
    ballColorSelect = random.randrange(len(ballColors))
    ballOutlineSelect = random.randrange(len(ballColors))
    ball.setOutline(ballColors[ballColorSelect])
    ball.setFill(ballColors[ballOutlineSelect])
    ball.draw(wheel)
#############################################
def speedBall(spinCount, ball, k):
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
        elif j > 70:
            time.sleep(.025)
        elif j > 55:
            time.sleep(.010)
        elif j > 35:
            time.sleep(.005)
        ball.move(-1*math.sin(0.165346981767014*i)*10.5,math.cos(0.165346981767014*i)*10.5)
    if spinCount+20 > 38:
        k = spinCount
        while k+20 >= 38:
            k = k - 38
    ball.setFill("")
    ball.setOutline("grey")
    return k
            
############# RESET MONEY ON 0 ##############
            
def resetMoney():
    lossWin = GraphWin("You Lost!", 400, 400)
    lossWin.setCoords(0, 0, 1000, 1000)
    displayLoss = Text(Point(500,500), "You Lost! Click anywhere to close program. Thanks for playing!")
    lossWin.setBackground("crimson")
    displayLoss.setFill("white")
    displayLoss.draw(lossWin)
    resetFile = open("playerinfo.txt", "w")
    resetFile.write("DEFAULTMONEY, 1000")
    resetFile.close()
    lossWin.getMouse()
    lossWin.close()
    
#############################################
######### DRAW BET WHEEL & SHAPES ###########
    
def drawBettingWheel(otherWin, a12, b12, c12):
    for i in range(3):
        twoOne = Rectangle(Point(76.9230769231*12,700+(i*100)),Point(1000,800+(i*100)))
        twoText = Text(Point(960,750+(i*100)), "3:1")
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
    # Draws labels for 12's
    drawLabel12(otherWin)
    ### DRAW RECTANGLE OF NOTHINGNESS
    nothing = Rectangle(Point(923.0769230772,500), Point(1000,700))
    nothing.setFill("black")
    nothing.draw(otherWin)
    
def drawLabel12(otherWin):
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
#########
def drawBottomRow(otherWin):
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

#########################################
######## CREATE USER BUTTONS ############
    
def createUserControls(otherWin, betBox, betIdBox):
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

#################################
######## DRAW BET COLORS ########
    
def drawBettingColors(otherWin, a12, b12, c12):
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

def updateStatLabels(otherWin, oddL, evenL, redL, blackL, greenL):
    # (OTXT) - CONSOLE IS THE DISPLAY OF MESSAGES    
    betId = 0
    key = Text(Point(200,275), "BET IDS:\n TYPE ONE TO SELECT\n\n '#' (1-38)\n'0' or '00'\n 'ROW#' (1-3)\n'1to18'\nor '19to36'\n'1to12'\nor '13to24'\nor '25to36'\n'EVEN' or 'ODD'\n'BLACK' or 'RED'")
    key.setSize(18)
    key.setFill("white")
    key.setFace("courier")
    key.draw(otherWin)
    if not int(round(statOdd.display())) == 0 or not int(round(statEven.display())) == 0 or not int(round(statBlack.display())) == 0 or not int(round(statRed.display())) == 0 or not int(round(statGreen.display())) == 0:
        t1 = "Odds:\n" + str(round((statOdd.display() / statTotal.display()), 4) * 100) + "%"
        oddL.setText(t1)
        t2 = "Evens:\n" + str(round((statEven.display() / statTotal.display()), 4) * 100) + "%"
        evenL.setText(t2)
        t3 = "Reds:\n" + str(round((statRed.display() / statTotal.display()), 4) * 100) + "%"
        redL.setText(t3)
        t4 = "Blacks:\n" + str(round((statBlack.display() / statTotal.display()), 4) * 100) + "%"
        blackL.setText(t4)
        t5 = "Greens:\n" + str(round((statGreen.display() / statTotal.display()), 4) * 100) + "%"
        greenL.setText(t5)

    ############################
#### Set Stat Labels Settings ####
    
def labelSettings(oddL, evenL, redL, blackL, greenL, wheel):
    oddL.draw(wheel)
    oddL.setFill("white")
    oddL.setStyle("bold")
    oddL.setSize(19)
    evenL.draw(wheel)
    evenL.setFill("white")
    evenL.setStyle("bold")
    evenL.setSize(19)
    redL.draw(wheel)
    redL.setOutline("crimson")
    redL.setStyle("bold")
    blackL.draw(wheel)
    blackL.setFill("black")
    blackL.setStyle("bold")
    greenL.draw(wheel)
    greenL.setFill("Dark Green")
    greenL.setStyle("bold")
    greenL.setSize(19)
#############################################    
################ PROGRAM RUN ################
    
def main(): #61 - 14 = 47 Lines of Code
    
    ############################
    ### SET VARIABLES & ROWS ###
    username = ""
    money = 0
    winningNumber = 100
    a12 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 100]
    b12 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 100]
    c12 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 100]
    #############################################
    ##### DISPLAY AMOUNT OF MONEY USER HAS ######
    moneyLabel = Text(Point(500,135), "You Have: $")
    moneyDisplay = Text(Point(500,100), money)
    login(moneyDisplay)
    ### SET WHEEL WINDOW CONDITIONS
    wheel = GraphWin("Roulette Wheel", 750, 750)
    wheel.setCoords(-90, -90, 90, 90)
    wheel.setBackground("Steel Blue")
    #############################################
    ### CREATE BET CONTROL & COMMAND WINDOW
    otherWin = GraphWin("Bet Controls", 750, 750) #750
    otherWin.setBackground("Teal")
    otherWin.setCoords(0,0,1000,1000)
    #############################################
    oddL = Text(Point(-70,80), "Odds:\n0.00%")
    evenL = Text(Point(70,80), "Even:\n0.00%")
    redL = Text(Point(-80,-70), "Red:\n0.00%")
    blackL = Text(Point(-80,-80), "Black\n0.00%")
    greenL = Text(Point(70,-80), "Green\n0.00%")
    labelSettings(oddL, evenL, redL, blackL, greenL, wheel)
    # (IEB) - ENTER BET ID & BET AMOUNT
    betBox = Entry(Point(500,350), 15)
    betIdBox = Entry(Point(500,250), 15)
    createUserControls(otherWin, betBox, betIdBox)
    createWheel(wheel)
    createLabels(wheel)
    displayInitialMoney(moneyLabel, otherWin, moneyDisplay)
    drawBettingWheel(otherWin, a12, b12, c12)
    drawBottomRow(otherWin)
    drawBettingColors(otherWin, a12, b12, c12)
    console = Text(Point(0,0), "Set Bet ID & Money then Spin!")
    console.setStyle("bold")
    console.setSize(24)
    console.setFill("Lavender")
    console.draw(wheel)
    #############################################
    ############ MAKE BETTING WINDOW ############
    splitter = Line(Point(0,500), Point(1000,500))
    splitter.draw(otherWin)
    updateStatLabels(otherWin, oddL, evenL, redL, blackL, greenL)
    ########################################
    ############# BET W MONEY ##############
    while True:
        # (IMS) - CHECKS IF VALID BUTTON CLICK (IN SPIN BTN)
        click = otherWin.getMouse()
        x = click.getX()
        y = click.getY()
        if x >= 700 and x <= 950:
            if y >= 75 and y <= 425:
                spinBall(betBox, betIdBox, moneyDisplay, console, wheel, otherWin, oddL, evenL, redL, blackL, greenL)

# Ahh, behold... the start switch:
main()

### PROGRAM END