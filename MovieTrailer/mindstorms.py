import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_spiral():
    window = turtle.Screen()
    window.bgcolor("red")
    #create some_turtle "brad"
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

draw_spiral()

#def draw_circle():
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)


#draw_square()
#draw_circle()


