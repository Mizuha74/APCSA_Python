import turtle as squirtle
import time
#1
def square():
    squirtle.fillcolor("blue")
    squirtle.begin_fill()
    squirtle.right(45)
    squirtle.forward(100)
    squirtle.right(90)
    squirtle.forward(100)
    squirtle.right(90)
    squirtle.forward(100)
    squirtle.right(90)
    squirtle.forward(100)
    squirtle.right(90)
    squirtle.forward(200)
    squirtle.left(90)
    squirtle.forward(100)
    squirtle.left(90)
    squirtle.forward(100)
    squirtle.left(90)
    squirtle.forward(100)
    squirtle.end_fill()
    

#2
def triangle():
    squirtle.left(45)
    squirtle.forward(150)
    squirtle.right(90)
    squirtle.forward(150)
    squirtle.right(135)
    squirtle.forward(215)
    
    squirtle.fillcolor("blue")
    squirtle.begin_fill()
    squirtle.right(155)
    squirtle.forward(120)
    squirtle.right(50)
    squirtle.forward(120)
    squirtle.right(155)
    squirtle.forward(150)
    squirtle.end_fill()

#3
def prism():
    squirtle.forward(100)
    squirtle.right(90)
    squirtle.forward(100)
    squirtle.right(90)
    squirtle.forward(100)
    squirtle.right(90)
    squirtle.forward(100)
    squirtle.right(135)
    squirtle.forward(282)
    squirtle.right(135)
    squirtle.forward(100)
    squirtle.right(90)
    squirtle.forward(100)
    squirtle.right(90)
    squirtle.forward(100)
    squirtle.right(90)
    squirtle.forward(100)
    squirtle.right(180)
    squirtle.forward(100)
    squirtle.left(45)
    squirtle.forward(141)
    squirtle.left(45)
    squirtle.forward(100)
    squirtle.left(90)
    squirtle.forward(100)
    squirtle.left(45)
    squirtle.forward(141)
 
    
#4
def rings():
    squirtle.penup()
    squirtle.goto(-40,20)
    squirtle.pendown()
    squirtle.circle(20)
    
    squirtle.penup()
    squirtle.goto(-20,0)
    squirtle.pendown()
    squirtle.circle(20)
    
    squirtle.penup()
    squirtle.goto(-0,20)
    squirtle.pendown()
    squirtle.circle(20)
    
    squirtle.penup()
    squirtle.goto(20,0)
    squirtle.pendown()
    squirtle.circle(20)
    
    squirtle.penup()
    squirtle.goto(40,20)
    squirtle.pendown()
    squirtle.circle(20)

#5
def compass():
    squirtle.forward(200)
    squirtle.right(180)
    squirtle.forward(400)
    squirtle.right(180)
    squirtle.forward(200)

    squirtle.right(90)
    squirtle.forward(200)
    squirtle.right(180)
    squirtle.forward(400)

    squirtle.penup()
    squirtle.goto(50,0)
    squirtle.pendown()
    squirtle.circle(50)

    squirtle.penup()
    squirtle.goto(0,215)
    squirtle.write("North")

    squirtle.goto(215,0)
    squirtle.write("East")

    squirtle.goto(0,-215)
    squirtle.write("South")

    squirtle.goto(-215,0)
    squirtle.write("West")

def dotsquare():
    squirtle.penup()
    squirtle.goto(-100,100)
    squirtle.pendown()
    squirtle.dot()
    squirtle.right(45)
    squirtle.forward(141)
    squirtle.dot()
    squirtle.forward(141)
    squirtle.dot()
    squirtle.left(135)
    squirtle.forward(200)
    squirtle.dot()
    squirtle.left(90)
    
    squirtle.forward(20)
    squirtle.penup()
    squirtle.forward(20)
    squirtle.pendown()
    squirtle.forward(50)
    squirtle.penup()
    squirtle.forward(20)
    squirtle.pendown()
    squirtle.forward(50)
    squirtle.penup()
    squirtle.forward(20)
    squirtle.pendown()
    squirtle.forward(20)
    
    squirtle.left(90)
    squirtle.forward(200)
    squirtle.dot()
    squirtle.left(90)
    
    squirtle.forward(20)
    squirtle.penup()
    squirtle.forward(20)
    squirtle.pendown()
    squirtle.forward(50)
    squirtle.penup()
    squirtle.forward(20)
    squirtle.pendown()
    squirtle.forward(50)
    squirtle.penup()
    squirtle.forward(20)
    squirtle.pendown()
    squirtle.forward(20)
    
    squirtle.left(90)
    squirtle.forward(200)
    squirtle.left(135)
    squirtle.forward(282)
    


def main():
    square(); #1
    time.sleep(1);
    squirtle.clearscreen();


    triangle(); #2
    time.sleep(1);
    squirtle.clearscreen();

    prism(); #3
    time.sleep(1);
    squirtle.clearscreen();
    
    rings(); #4
    time.sleep(1);
    squirtle.clearscreen();
    
    compass(); #5
    time.sleep(1);
    squirtle.clearscreen();
    
    dotsquare(); #6
    time.sleep(1);
    squirtle.clearscreen();
    
main();




squirtle.hideturtle()
print ("END")
input("press to end")