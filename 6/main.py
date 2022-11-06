import turtle

turtle.setworldcoordinates(-10, -10, 10, 10)
for i in range(10):
    for j in range(10):
        turtle.penup()
        turtle.goto(i, -j)
        turtle.pendown()
        turtle.dot(2, "black")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
for i in range(4):
    turtle.forward(10)
    turtle.right(90)
turtle.right(30)
for i in range(5):
    turtle.forward(6)
    turtle.right(60)
    turtle.forward(6)
    turtle.right(120)
turtle.exitonclick()
