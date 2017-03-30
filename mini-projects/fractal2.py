import turtle

window = turtle.Screen()
window.bgcolor("black")
turtle.color("white")

turtle.speed(500)
x=60

for counter2 in range (0,150):
    for counter in range(0,6):
        turtle.forward(x)
        turtle.left(60)
    x += 1
    turtle.left(3)
    
