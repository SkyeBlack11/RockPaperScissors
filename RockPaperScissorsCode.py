import turtle
import random
import time

screen = turtle.Screen()
screen.bgcolor("lightblue") #There was No Reason for this to be down there

rock = "Rock.gif"
paper = "Paper.gif"
scissors = "Scissors.gif"

screen.addshape(rock)
screen.addshape(paper)
screen.addshape(scissors)

player = turtle.Turtle() #Create the Turtles
computer = turtle.Turtle()
pen = turtle.Turtle()
pscore = turtle.Turtle()
cscore = turtle.Turtle()

pen.hideturtle() #Hide the Turtles
pscore.hideturtle()
cscore.hideturtle()

pen.penup() #Pens Up
pscore.penup()
cscore.penup()
player.penup()
computer.penup()

player.backward(200) #Turtle Movements
pscore.backward(200)
pscore.left(90)
pscore.forward(200)
computer.forward(200)
cscore.forward(200)
cscore.left(90)
cscore.forward(200)

global playscore
global computscore
playscore = 0
computscore = 0
def r(): #Rock
    global playscore
    global computscore
    pscore.clear()
    cscore.clear()
    computhand = [rock, paper, scissors]
    computchoice = random.choice(computhand)
    pen.write("3", align='left', font=('Arial', 36, 'normal'))
    time.sleep(1)
    pen.clear()
    pen.write("2", align='left', font=('Arial', 36, 'normal'))
    time.sleep(1)
    pen.clear()
    pen.write("1", align='left', font=('Arial', 36, 'normal'))
    time.sleep(1)
    pen.clear()
    player.shape(rock)
    computer.shape(computchoice)
    if computchoice == scissors:
        playscore = playscore + 1
        pscore.write(playscore, align='left', font=('Arial', 36, 'normal'))
        cscore.write(computscore, align='left', font=('Arial', 36, 'normal'))
    elif computchoice == paper:
        computscore = computscore + 1
        pscore.write(playscore, align='left', font=('Arial', 36, 'normal'))
        cscore.write(computscore, align='left', font=('Arial', 36, 'normal'))
    else:
        pscore.write(playscore, align='left', font=('Arial', 36, 'normal'))
        cscore.write(computscore, align='left', font=('Arial', 36, 'normal'))

def p(): #Paper
    global playscore
    global computscore
    pscore.clear()
    cscore.clear()
    computhand = [rock, paper, scissors]
    computchoice = random.choice(computhand)
    pen.write("3", align='left', font=('Arial', 36, 'normal'))
    time.sleep(1)
    pen.clear()
    pen.write("2", align='left', font=('Arial', 36, 'normal'))
    time.sleep(1)
    pen.clear()
    pen.write("1", align='left', font=('Arial', 36, 'normal'))
    time.sleep(1)
    pen.clear()
    player.shape(paper)
    computer.shape(computchoice)
    if computchoice == rock:
        playscore = playscore + 1
        pscore.write(playscore, align='left', font=('Arial', 36, 'normal'))
        cscore.write(computscore, align='left', font=('Arial', 36, 'normal'))
    elif computchoice == scissors:
        computscore = computscore + 1
        pscore.write(playscore, align='left', font=('Arial', 36, 'normal'))
        cscore.write(computscore, align='left', font=('Arial', 36, 'normal'))
    else:
        pscore.write(playscore, align='left', font=('Arial', 36, 'normal'))
        cscore.write(computscore, align='left', font=('Arial', 36, 'normal'))

def s(): #Scissors
    global playscore
    global computscore
    pscore.clear()
    cscore.clear()
    computhand = [rock, paper, scissors]
    computchoice = random.choice(computhand)
    pen.write("3", align='left', font=('Arial', 36, 'normal'))
    time.sleep(1)
    pen.clear()
    pen.write("2", align='left', font=('Arial', 36, 'normal'))
    time.sleep(1)
    pen.clear()
    pen.write("1", align='left', font=('Arial', 36, 'normal'))
    time.sleep(1)
    pen.clear()
    player.shape(scissors)
    computer.shape(computchoice)
    if computchoice == paper:
        playscore = playscore + 1
        pscore.write(playscore, align='left', font=('Arial', 36, 'normal'))
        cscore.write(computscore, align='left', font=('Arial', 36, 'normal'))
    elif computchoice == rock:
        computscore = computscore + 1
        pscore.write(playscore, align='left', font=('Arial', 36, 'normal'))
        cscore.write(computscore, align='left', font=('Arial', 36, 'normal'))
    else:
        pscore.write(playscore, align='left', font=('Arial', 36, 'normal'))
        cscore.write(computscore, align='left', font=('Arial', 36, 'normal'))

screen.onkey(r, "r") #Choose your player
screen.onkey(p, "p")
screen.onkey(s, "s")
screen.listen() #Listens for Keys
screen.mainloop() # Wait for user to close window
