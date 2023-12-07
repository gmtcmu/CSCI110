import turtle


     

wn = turtle.Screen()        
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

turtle.hideturtle()
# def draw_square(turtle,sz):
    


for i in range(4):
    turtle.forward(20)
    turtle.left(90)
# turtle = turtle.Turtle()      
# draw_square(turtle,20)       
turtle.penup()
turtle.left(225)
turtle.forward(20)
turtle.left(225)
turtle.pendown()
for i in range(4):
    turtle.forward(47)
    turtle.right(90)
turtle.penup()
turtle.left(135)
turtle.forward(20)
turtle.left(225)
turtle.pendown()
turtle.pencolor("red")
for i in range(4):
    turtle.forward(75)
    turtle.right(90)


wn.mainloop()