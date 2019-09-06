import turtle

turtle.shape("turtle")


def flagb():
    for i in range(1):
        turtle.color("red")
        turtle.begin_fill()
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(120)
        turtle.right(90)
        turtle.forward(200)
        turtle.end_fill()

def scicle():
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(20)
    turtle.color("yellow")
    turtle.left(40)
    turtle.begin_fill()
    turtle.forward(13)
    turtle.right(100)

    for i in range(40):
        turtle.forward(1)
        turtle.left(5)

    turtle.right(90)
    turtle.forward(2)
    turtle.right(90)

    for i in range(47):
        turtle.forward(1)
        turtle.right(4)

    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(4)
    turtle.end_fill()


def hammer():
    turtle.penup()
    turtle.right(130)
    turtle.forward(23)
    turtle.left(130)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(8)
    turtle.right(90)
    turtle.forward(6)
    turtle.right(90)
    turtle.forward(21)
    turtle.right(90)
    turtle.forward(6)
    turtle.right(90)
    turtle.forward(8)
    turtle.left(90)
    turtle.forward(20)
    turtle.end_fill()








flagb()
scicle()
hammer()

turtle.penup()
turtle.goto(100,0)


turtle.exitonclick()