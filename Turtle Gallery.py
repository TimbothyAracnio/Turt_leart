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
    for i in range(1):
        turtle.right(90)
        turtle.forward(80)
        turtle.right(90)
        turtle.forward(20)
        turtle.color("yellow")
        turtle.left(40)
        turtle.forward(8)
        turtle.right(180)
        turtle.forward(1)




flagb()
scicle()



turtle.exitonclick()