import turtle

t = turtle.Turtle()
t.speed(20) 


screen = turtle.Screen()
size = 5
t.penup()
# t.goto(200,-200)   #the border is 400 by 400
# t.pendown()
# t.goto(200,200)
# t.goto(-200,200)
# t.goto(-200,-200)
# t.goto(200,-200)    #the out most triangle    #well this is clearly unnecessary
t.left(90)
t.goto(200,-200)
for i in range(80):
    for _ in range(4):
        t.forward(size)
        t.right(90)     
    t.penup()
    t.goto(200-(5*i), -200)  
    t.pendown()
    size += 5

turtle.done()
