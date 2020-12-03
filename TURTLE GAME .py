import turtle              # 1. import the modules
import random
import time
wn = turtle.Screen()       # 2. Create a screen
wn.setup(width = 320, height = 320, startx = 0, starty = 0)
turtle.color("blue")
turtle.speed(10)
turtle.setpos(-140,200)
turtle.write("Vidyavardhini's Turtle Race",font=("Arial", 30, "bold"))
turtle.penup()
turtle.pendown()
chandan = turtle.Turtle()    # 3. Create 4 turtles
venkatesh = turtle.Turtle()
chinmay = turtle.Turtle()
mankrit = turtle.Turtle()
landscape = turtle.Turtle()

chandan.ht()
venkatesh.ht()
chinmay.ht()
mankrit.ht()

#Road setup
landscape.speed(3)
landscape.pensize(3)
landscape.ht()
landscape.up()
landscape.setpos(-200,-200)
landscape.down()
landscape.color("White","DarkGray")

landscape.begin_fill()#landscape.fill(True)
for square in range(2):
    landscape.forward(400)
    landscape.left(90)
    landscape.forward(120)
    landscape.left(90)
landscape.end_fill()#landscape.fill(False)

landscape.up()
landscape.setpos(-200,-200)
for line in range(4):
    landscape.left(90)
    landscape.forward(30)
    landscape.right(90)
    for lot_of_paint in range(10):
        landscape.down()
        landscape.forward(20)
        landscape.up()
        landscape.forward(20)
    landscape.backward(400)
    
landscape.setpos(-200,-200)
landscape.pensize(5)
for line in range(2):
    landscape.down()
    for lot_of_paint in range(20):
        landscape.color("red")
        landscape.forward(10)
        landscape.color("white")
        landscape.forward(10)
    landscape.up()
    landscape.backward(400)  
    landscape.setpos(-200,-80)
    
landscape.setpos(180,-80)
landscape.pensize(8)
landscape.seth(270)
landscape.shape("square")

flag1 = 1                            
for line in range(4):
    landscape.down()
    if ((flag1 % 2) != 1):
        for lot_of_paint in range(10):
            landscape.color("black")
            landscape.forward(6)
            landscape.color("white")
            landscape.forward(6)
    else:
        for lot_of_paint in range(10):
            landscape.color("white")
            landscape.forward(6)
            landscape.color("black")
            landscape.forward(6)
    flag1 = flag1 + 1
    landscape.up()
    landscape.backward(120)  
    landscape.left(90)
    landscape.forward(6)
    landscape.right(90)
    
wn.bgcolor('orange')
    
landscape.speed(5)
landscape.up()
landscape.goto(-100,100)
landscape.color("yellow")
landscape.pensize(3)
landscape.speed(0)

for number_of_positions in range(1, 47, 1):    
    landscape.forward(60)         
    landscape.up()   
    landscape.forward(-60)
    landscape.down()
    landscape.right(8)

landscape.up()       
landscape.setpos(-90,-77)
landscape.pensize(1)
landscape.shape("arrow")  
landscape.color("black","green")

landscape.begin_fill()#landscape.fill(True)
landscape.seth(45)
landscape.down()
landscape.forward(100)
for degree in range(135):   
    landscape.right(1)
    landscape.forward(1)
landscape.forward(30)
landscape.end_fill()#landscape.fill(False)

landscape.begin_fill()#landscape.fill(True)
landscape.seth(90)
landscape.forward(200)
for degree in range(180):  
    landscape.right(1)
    landscape.forward(1)
landscape.forward(200)
landscape.end_fill()#landscape.fill(False)
landscape.penup()

#Getting the turtles ready
chandan.shape('turtle')
venkatesh.shape('turtle')
chinmay.shape("turtle")
mankrit.shape("turtle")

chandan.color('Olive')
venkatesh.color('yellow')
chinmay.color("Green")
mankrit.color("blue")

chandan.st()
venkatesh.st()
chinmay.st()
mankrit.st()

chandan.up()
venkatesh.up()                 
chinmay.up()
mankrit.up()

chandan.goto(-190,-95)
venkatesh.goto(-190,-125)
chinmay.setpos(-190,-155)
mankrit.setpos(-190,-185)

chandan.speed(2)
venkatesh.speed(2)
mankrit.speed(2)
chinmay.speed(2)

#Starting the race
landscape.shape("circle")
landscape.color("red")
landscape.setpos(-188,-60)
landscape.seth(0)

for countdown in range(3):
    landscape.st()
    time.sleep(0.5)
    landscape.ht()
    time.sleep(0.5)
   
landscape.color("LawnGreen")
landscape.st()
time.sleep(1.5)
landscape.ht()

chandan_winner = 0
venkatesh_winner = 0
chinmay_winner = 0
mankrit_winner = 0

winners_flag = 0
for i in range(50):
    if (chandan.xcor()<200):
        chandan.forward(random.randrange(1,50))
    else:
        if (winners_flag == 0):
            if (chandan_winner == 0):
                print("chandan is the first place")
                chandan_winner = 1
                winners_flag = 1       
        elif (winners_flag == 1):
            if (chandan_winner == 0):
                print("chandan is the second place")
                lance_winner = 1
                winners_flag = 2
        elif (winners_flag == 2):
            if (chandan_winner == 0):
                print("chandan is the third place")
                chandan_winner = 1
                winners_flag = 3
        elif (winners_flag == 3):
            if (chandan_winner == 0):
                print("chandan is the fourth place")
                chandan_winner = 1
                winners_flag = 4
    
    if (venkatesh.xcor()<200):
        venkatesh.forward(random.randrange(1,50))
    else:
        if (winners_flag == 0):
            if (venkatesh_winner == 0):
                print("venkatesh is the first place")
                venkatesh_winner = 1
                winners_flag = 1       
        elif (winners_flag == 1):
            if (venkatesh_winner == 0):
                print("venkatesh is the second place")
                venkatesh_winner = 1
                winners_flag = 2
        elif (winners_flag == 2):
            if (venkatesh_winner == 0):
                print("venkatesh is the third place")
                venkatesh_winner = 1
                winners_flag = 3
        elif (winners_flag == 3):
            if (venkatesh_winner == 0):
                print("venkatesh is the fourth place")
                venkatesh_winner = 1
                winners_flag = 4       
        
    if (chinmay.xcor()<200):
        chinmay.forward(random.randrange(1,50))
    else:
        if (winners_flag == 0):
            if (chinmay_winner == 0):
                print("chinmay is the first place")
                chinmay_winner = 1
                winners_flag = 1       
        elif (winners_flag == 1):
            if (chinmay_winner == 0):
                print("chinmay is the second place")
                chinmay_winner = 1
                winners_flag = 2
        elif (winners_flag == 2):
            if (chinmay_winner == 0):
                print("chinmay is the third place")
                chinmay_winner = 1
                winners_flag = 3
        elif (winners_flag == 3):
            if (chinmay_winner == 0):
                print("chinmay is the fourth place")
                chinmay_winner = 1
                winners_flag = 4  
     
    if (mankrit.xcor()<200):
        mankrit.forward(random.randrange(1,50))
    else:
        if (winners_flag == 0):
            if (mankrit_winner == 0):
                print("mankrit is the first place")
                mankrit_winner = 1
                winners_flag = 1       
        elif (winners_flag == 1):
            if (mankrit_winner == 0):
                print("mankrit is the second place")
                mankrit_winner = 1
                winners_flag = 2
        elif (winners_flag == 2):
            if (mankrit_winner == 0):
                print("mankrit is the third place")
                mankrit_winner = 1
                winner_flag=3
        elif (winners_flag == 3):
            if (mankrit_winner == 0):
                print("mankrit is the fourth place")
                mankrit_winner = 1
                winners_flag = 4   
