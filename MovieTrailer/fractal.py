import turtle

loadWindow = turtle.Screen()
turtle.colormode(255)

turtle.speed(0)



def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)
        
for i in range(50):
    shape(2*i, i)
    turtle.left(i)
    
turtle.exitonclick()



